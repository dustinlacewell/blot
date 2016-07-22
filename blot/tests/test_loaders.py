import unittest

import mock

from blot.loaders import BasicLoader


class BasicLoaderCase(unittest.TestCase):
    def test_check_path(self):
        loader = BasicLoader('.', excludes=["excluded"], includes=["included"])
        assert loader.check_path("/foo")
        assert loader.check_path("/excluded/included/foo")
        assert not loader.check_path("/excluded/foo")

    def test_find_files(self):
        loader = BasicLoader('/', excludes=["excluded"], includes=["included"])
        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [
                ('/', ('excluded', ), ('foo', )),
                ('/excluded', ('included', ), ('foo', )),
                ('/excluded/included', (), ('foo', ))
            ]

            files = loader.find_files()
            assert tuple(files) == ('/foo', '/excluded/included/foo')
            files = loader.load()
            assert tuple(files) == ('/foo', '/excluded/included/foo')
