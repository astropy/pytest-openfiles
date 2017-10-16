# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os

PKG_DATA_DIR = os.path.dirname(__file__)

fd = None


def test_open_file_detection():
    global fd
    fd = open(os.path.join(PKG_DATA_DIR, 'data/open_file_detection.txt'))


def teardown():
    if fd is not None:
        fd.close()
