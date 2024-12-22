=======================
 Repeater Test Service
=======================

This is a small HTTP response service, created for testing CommCare HQ
Data Forwarding, a.k.a. Repeaters.

It supports the following features:

* GET or POST to a root endpoint, e.g. ``https://api.example.com/``:
  Returns a 200 response.

* Rate-limit requests per second: For example,
  ``POST https://api.example.com/rps/5/`` returns a 200 response, or a
  429 response if more than 5 requests are received per second from the
  same IP address.

* Rate-limit requests per minute: Like rate-limit requests per second.
  e.g. ``POST https://api.example.com/rpm/300/``.

* Return a given status code: e.g.
  ``POST https://api.example.com/status/418/`` will return status code
  418.

* Return a given status code with a given possibility: e.g.
  ``POST https://api.example.com/status/418/percent/50/`` will return
  status code 418 on 50% of requests, and 200 the rest of the time.

For everything else, you probably want `httpbin`_.

The Repeater Test Service is built using `Quart`_, the asyncio web
microframework based on Flask.


Requirements
------------

The Repeater Test Service requires Redis, and is tested using Python
3.12, although it probably works with other versions.


Installing a development environment
------------------------------------

1. Clone this repository.

2. Create a virtual environment and activate it:

   .. code-block:: bash

      $ python3.12 -m venv venv
      $ source venv/bin/activate

3. Install the dependencies, including testing dependencies:

   .. code-block:: bash

      $ pip install -e '.[test]'

4. Set the ``QUART_REDIS_URI`` environment variable. e.g.

   .. code-block:: bash

      $ export QUART_REDIS_URI='redis://localhost:6379/0'

   The use of ``.env`` is supported. e.g.

   .. code-block:: bash

      $ echo "QUART_REDIS_URI = 'redis://localhost:6379/0'" > .env


Running
-------

To run the service, use the following command:

.. code-block:: bash

   $ export QUART_APP=http_resp:app
   $ quart run


Testing
-------

To run the tests, use the following command:

.. code-block:: bash

   $ export QUART_APP=http_resp:app
   $ pytest


.. _httpbin: https://httpbin.org/
.. _Quart: https://quart.palletsprojects.com/
