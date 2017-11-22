================
pytest-openfiles
================

This package provides a plugin for the `pytest`_ framework that allows
developers to detect whether any file handles or other file-like objects were
inadvertently left open at the end of a unit test. It has been moved from the
core `astropy`_ project since it is of use more generally.

.. _pytest: https://pytest.org/en/latest/
.. _astropy: https://astropy.org/en/latest/

**NOTE**: This plugin is not supported with Py2.7 on Win32 platforms.

Motivation
----------

The `pytest-openfiles`_ plugin allows for the detection of open I/O resources
at the end of unit tests.  This is particularly useful for testing code that
manipulates file handles or other I/O resources. It allows developers to ensure
that this kind of code properly cleans up I/O resources when they are no longer
needed.

Installation
------------

The ``pytest-openfiles`` plugin can be installed using ``pip``::

    $ pip install pytest-openfiles

It is also possible to install the latest development version from the source
repository::

    $ git clone https://github.com/astropy/pytest-openfiles
    $ cd pytest-openfiles
    $ python ./setup.py install

In either case, the plugin will automatically be registered for use with
``pytest``.

Usage
-----

This plugin adds the ``--open-files`` option to the ``pytest`` command.  When
running tests with ``--open-files``, if a file is opened during the course of a
unit test but that file is not closed before the test finishes, the test will
fail.

Development Status
------------------

.. image:: https://travis-ci.org/astropy/pytest-openfile.svg
    :target: https://travis-ci.org/astropy/pytest-openfiles
    :alt: Travis CI Status

.. image:: https://ci.appveyor.com/api/projects/status/944gtt7n0o1d6826/branch/master?svg=true 
    :target: https://ci.appveyor.com/project/Astropy/pytest-openfiles/branch/master
    :alt: Appveyor Status

Questions, bug reports, and feature requests can be submitted on `github`_.

.. _github: https://github.com/astropy/pytest-openfiles

License
-------
This plugin is licensed under a 3-clause BSD style license - see the
``LICENSE.rst`` file.
