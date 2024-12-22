import pytest
import pytest_asyncio

from ..counter import (
    get_minute_count,
    get_second_count,
    increment_minute_counter,
    increment_second_counter,
)
from ..rep_test_srv import app


@pytest_asyncio.fixture(name='test_app', scope='function')
async def app_():
    async with app.test_app() as test_app_:
        yield test_app_


@pytest.mark.asyncio
async def test_minute_counter(test_app):
    ip_addr = '1.1.1.1'
    count = await get_minute_count(ip_addr)
    assert count == 0
    await increment_minute_counter(ip_addr)
    count = await get_minute_count(ip_addr)
    assert count == 1


@pytest.mark.asyncio
async def test_second_counter(test_app):
    ip_addr = '2.2.2.2'
    count = await get_second_count(ip_addr)
    assert count == 0
    await increment_second_counter(ip_addr)
    count = await get_second_count(ip_addr)
    assert count == 1
