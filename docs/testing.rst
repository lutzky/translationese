Testing
=======

This project is comprehensively covered by unit tests. You can run the tests
like so:

.. code-block:: bash

    $ sudo pip install nose
    $ nosetests -v

Furthermore, if you use PyDev, it is recommended to configure it to use
``nosetests`` as the test runner, and have it re-run all tests whenever a file
is saved.

Two types of tests are present:

* Integration tests, testing the complete quantification of a small sample

  * These are implemented using :mod:`unittest`, within the `tests` directory.

* Unit tests, testing the output of a utility function.

  * These are implemented, when convenient, as doctests - examples present in
    the docstring of the utility function. These are tested by nosetests as
    well.

Test utility classes
--------------------

.. automodule:: tests.util
   :members:
