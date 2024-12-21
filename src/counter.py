import time

from quart_redis import get_redis


async def increment_minute_counter(client_ip):
    redis = get_redis()
    current_minute = int(time.time() // 60)
    key = f'minutes:{client_ip}:{current_minute}'
    await redis.incr(key)
    await redis.expire(key, 61)


async def get_minute_count(client_ip):
    redis = get_redis()
    current_minute = int(time.time() // 60)
    key = f'minutes:{client_ip}:{current_minute}'
    count = await redis.get(key)
    return int(count) if count else 0


async def increment_second_counter(client_ip):
    redis = get_redis()
    current_second = int(time.time())
    key = f'seconds:{client_ip}:{current_second}'
    await redis.incr(key)
    await redis.expire(key, 2)


async def get_second_count(client_ip):
    redis = get_redis()
    current_second = int(time.time())
    key = f'seconds:{client_ip}:{current_second}'
    count = await redis.get(key)
    return int(count) if count else 0
