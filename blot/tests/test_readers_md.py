import unittest

import mock

from blot.readers import MarkdownReader

markdown = "Foo: bar\nBiz: baz\nBiz: boz\n\n## Header\nContent"

class MarkdownReaderCase(unittest.TestCase):
    def test_read_path(self):
        reader = MarkdownReader()
        mockopen = mock.mock_open(read_data=markdown)
        with mock.patch("__builtin__.open", mockopen):
            asset = reader.read_path("foo.md")
            assert asset.source == "foo.md"
            assert asset.content == "<h2>Header</h2>\n<p>Content</p>"
            assert asset.metadata == dict(foo="bar", biz=["baz", "boz"])

    def test_extensions(self):
        reader = MarkdownReader()
        mockopen = mock.mock_open(read_data=markdown)
        with mock.patch("__builtin__.open", mockopen):
            assets = reader.read(["/foo.md", "/bar.rst"])
            assert len(assets) == 1
