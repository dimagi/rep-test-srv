import pytest
import pytest_asyncio

from http_resp import app


@pytest_asyncio.fixture(name='test_app', scope='function')
async def app_():
    async with app.test_app() as test_app_:
        yield test_app_


@pytest.mark.asyncio
async def test_get_default(test_app):
    async with test_app.test_client() as client:
        response = await client.get('/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'


@pytest.mark.asyncio
async def test_post_default(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'


@pytest.mark.asyncio
async def test_requests_per_second(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/rps/1/')
        assert response.status_code == 200
        response = await client.post('/rps/1/')
        assert response.status_code == 429


@pytest.mark.asyncio
async def test_requests_per_minute(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/rpm/1/')
        assert response.status_code == 200
        response = await client.post('/rpm/1/')
        assert response.status_code == 429


@pytest.mark.asyncio
async def test_status_code(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/code/404/')
        assert response.status_code == 404
        data = await response.get_data(as_text=True)
        assert data == 'Not Found'


@pytest.mark.asyncio
async def test_status_code_sometimes_100(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/code/404/percent/100/')
        assert response.status_code == 404
        data = await response.get_data(as_text=True)
        assert data == 'Not Found'


@pytest.mark.asyncio
async def test_status_code_sometimes_0(test_app):
    async with test_app.test_client() as client:
        response = await client.post('/code/404/percent/0/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'
