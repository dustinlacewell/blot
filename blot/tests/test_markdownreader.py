import unittest

import mock

from blot.readers import MarkdownReader

markdown = "---\nfoo: bar\nFoo: baz\nBiz: boz\n---\n\n## Header\nContent"

class MarkdownReaderCase(unittest.TestCase):
    def test_read_path(self):
        reader = MarkdownReader()
        mockopen = mock.mock_open(read_data=markdown)
        with mock.patch("__builtin__.open", mockopen):
            assets = reader.read(["foo.md"])
            asset = assets[0]
            assert asset.source == "foo.md"
            assert asset.content == "<h2>Header</h2>\n\n<p>Content</p>\n"
            assert asset.metadata == dict(foo="baz", biz="boz")

