# Licensed under a 3-clause BSD style license - see LICENSE.rst
from astropy.utils.data import get_pkg_data_filename

fd = None


def test_open_file_detection():
    global fd
    fd = open(get_pkg_data_filename('data/open_file_detection.txt'))


def teardown():
    if fd is not None:
        fd.close()
