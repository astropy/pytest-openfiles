# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os

import pytest

PKG_DATA_DIR = os.path.dirname(__file__)

fd1 = None
fd2 = None


def test_open_file_detection():
    # This test is hard-coded in plugin.py as having one dangling open file
    global fd1
    fd1 = open(os.path.join(PKG_DATA_DIR, 'data/open_file_detection.txt'))


def test_open_file_detection_closed_in_teardown():
    # The file handle here should be closed in the teardown function so we
    # don't expect and error
    global fd2
    fd2 = open(os.path.join(PKG_DATA_DIR, 'data/open_file_detection.txt'))


@pytest.mark.openfiles_ignore
def test_skip_open_file_detection():
    # This test would normally fail the check for open files but we have
    # decorated it in a way so as to ignore the open file error.
    global fd1
    fd1 = open(os.path.join(PKG_DATA_DIR, 'data/open_file_detection.txt'))


def teardown():
    if fd2 is not None:
        fd2.close()


class TestClass:

    def setup_method(self, method):
        self.fd = open(os.path.join(PKG_DATA_DIR, 'data/open_file_detection.txt'))

    def teardown_method(self, method):
        self.fd.close()
        self.fd = None

    def test_pass(self):
        self.fd.read(1)
