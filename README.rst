=======================
 Repeater Test Service
=======================

This is a small service for testing Repeaters / CommCare HQ Data
Forwarding.

It is written in Python + `Quart`_.

It supports the following features:

* GET or POST to a root endpoint, e.g. ``https://api.example.com/``:
  Returns a 200 response.

* Rate-limit requests per second: For example,
  ``https://api.example.com/rps/5/`` returns a 200 response, or a 429
  response if more than 5 requests are received per second from the
  same IP address.

* Rate-limit requests per minute: Like rate-limit requests per second.
  e.g. ``https://api.example.com/rpm/300/``.

* Return a given status code: e.g. ``https://api.example.com/code/418/``
  will return status code 418.

* Return a given status code with a given possibility: e.g.
  ``https://api.example.com/code/418/percent/50/`` will return status
  code 418 on 50% of requests, and 200 the rest of the time.


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


Running
-------

To run the service, use the following command:

.. code-block:: bash

    $ cd src/
    $ export QUART_APP=rep_test_srv:app
    $ quart run


Testing
-------

To run the tests, use the following command:

.. code-block:: bash

    $ cd src/
    $ export QUART_APP=rep_test_srv:app
    $ pytest


.. _Quart: https://quart.palletsprojects.com/
