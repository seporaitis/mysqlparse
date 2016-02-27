.. :changelog:

History
-------

PENDING
-------

* Brought back ``HISTORY.rst``.
* Add ``mysqlparse.parse`` function.
* Add ``six`` as a dependency to make writing Py2 and Py3 compatible code easier.
* Add support for ``ALTER TABLE .. MODIFY [COLUMN]`` statements.
* Add support for ``ALTER TABLE .. DROP *`` statements.


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
