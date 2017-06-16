.. :changelog:

History
-------

PENDING
-------

* (Insert new release notes below this line)

0.1.6 (2017-06-16)
------------------

* Add support for ``ALTER TABLE .. CHANGE COLUMN`` statements (contributed by [@jgysland](https://github.com/jgysland))

0.1.5 (2016-08-23)
------------------

* Change the licence from ``AGPLv3`` to ``MIT`` licence.


0.1.4 (2016-02-28)
------------------

* Brought back ``HISTORY.rst``.
* Add ``mysqlparse.parse`` function.
* Add ``six`` as a dependency to make writing Py2 and Py3 compatible code easier.
* Add support for ``ALTER TABLE .. MODIFY [COLUMN]`` statements.
* Add support for ``ALTER TABLE .. DROP *`` statements.
* Move version string from ``setup.py`` into ``mysqlparse``.


0.1.3 (2016-02-20)
------------------

* Updated ``README.rst``.
* Add support for ``ALTER TABLE ... ADD INDEX`` statements.


0.1.2 (2016-02-16)
------------------

* A little tidy up.
* Removed ``defaultValue`` parse action.
* Improved ``NULL`` handling.
* Updated tests to pass.


0.1.1 (2016-02-15)
------------------

* Fixed packaging configuration.


0.1.0 (2016-02-15)
------------------

* First release with code parsing some of ``ALTER TABLE ... ADD COLUMN`` statements.
