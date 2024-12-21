import os
import time

from dotenv import load_dotenv
from redis.asyncio.client import Redis as AsyncRedis

load_dotenv()
redis = AsyncRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=int(os.getenv('REDIS_DB', 0)),
)


async def increment_minute_counter(client_ip):
    current_minute = int(time.time() // 60)
    key = f'minutes:{client_ip}:{current_minute}'
    await redis.incr(key)
    await redis.expire(key, 61)


async def get_minute_count(client_ip):
    current_minute = int(time.time() // 60)
    key = f'minutes:{client_ip}:{current_minute}'
    count = await redis.get(key)
    return int(count) if count else 0


async def increment_second_counter(client_ip):
    current_second = int(time.time())
    key = f'seconds:{client_ip}:{current_second}'
    await redis.incr(key)
    await redis.expire(key, 2)


async def get_second_count(client_ip):
    current_second = int(time.time())
    key = f'seconds:{client_ip}:{current_second}'
    count = await redis.get(key)
    return int(count) if count else 0
