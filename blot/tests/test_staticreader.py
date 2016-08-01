import unittest

import mock

from blot.readers import staticreader


class StaticReaderCase(unittest.TestCase):
    def test_read_path(self):
        reader = staticreader.StaticReader()
        mockopen = mock.mock_open(read_data="content")
        with mock.patch("__builtin__.open", mockopen):
            assets = reader.read(["/foo.css"])
            asset = assets[0]
            assert asset.source == "/foo.css"
            assert asset.content == "content"
            assert asset.metadata == {}
