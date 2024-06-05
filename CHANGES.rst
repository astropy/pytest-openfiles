0.6.0 (2024-06-05)
==================

- Replaced ``distutils`` with ``packaging``; the latter now a required
  dependency. [#43]

- Dropped support for Python 3.6. [#46]

0.5.0 (2020-04-16)
==================

- Updated package infrastructure. [#29]

- Force garbage collection before checking for open files. [#30]

0.4.0 (2019-07-20)
==================

- Added the ability to use ``*`` and ``?`` wildcards in
  ``open_files_ignore``. [#22]

- Fixed compatibility with pytest 4.2. [#20]

0.3.2 (2019-01-07)
==================

- Replace deprecated method to allow for compatibility with ``pytest-4.1`` and
  later. [#19]

0.3.1 (2018-11-26)
==================

- Fix a minor packaging issue. [#13]

0.3.0 (2018-04-20)
==================

- Add decorator to skip detection of open files for particular tests. [#10]

- Fix packaging error: do not include tests in package distribution. [#11]


0.2 (2017-12-07)
================

- Remove test dependency on astropy. [#4]

0.1 (2017-10-09)
================

- Alpha release.
