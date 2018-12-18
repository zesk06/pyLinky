
pyLinky
=======

.. image:: https://travis-ci.org/Pirionfr/pyLinky.svg?branch=master
    :target: https://travis-ci.org/Pirionfr/pyLinky

.. image:: https://img.shields.io/pypi/v/pyLinky.svg
    :target: https://pypi.python.org/pypi/pyLinky

.. image:: https://img.shields.io/pypi/pyversions/pyLinky.svg
    :target: https://pypi.python.org/pypi/pyLinky

.. image:: https://requires.io/github/Pirionfr/pyLinky/requirements.svg?branch=master
    :target: https://requires.io/github/Pirionfr/pyLinky/requirements/?branch=master
    :alt: Requirements Status

Get your consumption data from your Enedis account (www.enedis.fr)

This library This is based on jeedom_linky, created by Outadoc (https://github.com/Asdepique777/jeedom_linky)

Installation
------------

The easiest way to install the library is using `pip <https://pip.pypa.io/en/stable/>`_::

    pip install pylinky

You can also download the source code and install it manually::

    cd /path/to/pylinky/
    python setup.py install

Usage
-----
Print your current data

    pylink -u <USERNAME> -p <PASSWORD>

Alternatively, you can create a ``.dotenv`` file that contains
your username and password:

.. codeblock:: env

    # .env file permit to define per folder env-var
    PYLINKY_USERNAME="myUsername@somewhere.com"

    PYLINKY_PASSWORD="WhatAWonderfullPassword"

And launch pylink from the same folder.

    # print hourly/daily/monthly/yearly consumption datas as json
    pylink

    # print only daily consumption as json
    pylink --daily

    # print only daily consumption as csv
    pylink --daily --csv


Dev env
-------
create virtual env and install requirements

    virtualenv -p /usr/bin/python3.5 env
    pip install -e .[dev]

