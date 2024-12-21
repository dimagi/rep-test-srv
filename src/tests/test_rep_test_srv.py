import pytest
import pytest_asyncio

from ..rep_test_srv import app


@pytest_asyncio.fixture(name="my_app", scope="function")
async def my_app():
    async with app.test_app() as test_app:
        yield test_app


@pytest.mark.asyncio
async def test_get_default(my_app):
    async with my_app.test_client() as client:
        response = await client.get('/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'


@pytest.mark.asyncio
async def test_post_default(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'


@pytest.mark.asyncio
async def test_requests_per_second(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/rps/1/')
        assert response.status_code == 200
        response = await client.post('/rps/1/')
        assert response.status_code == 429


@pytest.mark.asyncio
async def test_requests_per_minute(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/rpm/1/')
        assert response.status_code == 200
        response = await client.post('/rpm/1/')
        assert response.status_code == 429


@pytest.mark.asyncio
async def test_status_code(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/code/404/')
        assert response.status_code == 404
        data = await response.get_data(as_text=True)
        assert data == 'Not Found'


@pytest.mark.asyncio
async def test_status_code_sometimes_100(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/code/404/percent/100/')
        assert response.status_code == 404
        data = await response.get_data(as_text=True)
        assert data == 'Not Found'


@pytest.mark.asyncio
async def test_status_code_sometimes_0(my_app):
    async with my_app.test_client() as client:
        response = await client.post('/code/404/percent/0/')
        assert response.status_code == 200
        data = await response.get_data(as_text=True)
        assert data == 'OK'
