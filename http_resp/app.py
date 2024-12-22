import random
from http import HTTPStatus

from quart import Quart, Response, request
from quart.cli import load_dotenv
from quart_redis import RedisHandler

from http_resp.counter import (
    get_minute_count,
    get_second_count,
    increment_minute_counter,
    increment_second_counter,
)

load_dotenv()
app = Quart(__name__)
app.config.from_prefixed_env()
redis_handler = RedisHandler(app)


@app.route('/', methods=['GET', 'POST'])
async def default():
    return Response('OK', mimetype='text/plain')


@app.route('/rps/<int:rps>/', methods=['POST'])
async def requests_per_second(rps):
    client_ip = request.remote_addr
    await increment_second_counter(client_ip)
    count = await get_second_count(client_ip)
    if count > rps:
        return Response('Too many requests', status=429, mimetype='text/plain')
    return Response('OK', mimetype='text/plain')


@app.route('/rpm/<int:rpm>/', methods=['POST'])
async def requests_per_minute(rpm):
    client_ip = request.remote_addr
    await increment_minute_counter(client_ip)
    count = await get_minute_count(client_ip)
    if count > rpm:
        return Response('Too many requests', status=429, mimetype='text/plain')
    return Response('OK', mimetype='text/plain')


@app.route('/code/<int:code>/', methods=['POST'])
async def status_code(code):
    phrase = _get_http_status_phrase(code)
    return Response(phrase, status=code, mimetype='text/plain')


@app.route('/code/<int:code>/percent/<int:percent>/', methods=['POST'])
async def status_code_sometimes(code, percent):
    if random.randrange(100) < percent:
        phrase = _get_http_status_phrase(code)
        return Response(phrase, status=code, mimetype='text/plain')
    return Response('OK', mimetype='text/plain')


def _get_http_status_phrase(status_code):
    http_status_by_value = {s.value: s for s in HTTPStatus}
    try:
        return http_status_by_value[status_code].phrase
    except KeyError:
        return '[Unknown]'


def run():
    app.run()
