import unittest

import mock

from blot.writers import listwriter
from blot.assets import ContentAsset
from blot.utils import pathurl


class ListWriterCase(unittest.TestCase):
    def setUp(self):
        self.asset = ContentAsset("/foo.md", None, metadata=dict(filename="foo"))
        self.assets = [self.asset]
        self.writer = listwriter.ListWriter(
            self.assets, 'foo.html', '/{filename}/index.html')

    def test_target(self):
        context = {}
        self.writer.target(context)
        assert self.asset.target == "/foo/index.html"

    def test_render(self):
        context = {
            'TEMPLATE_PATH': "templates",
            'assets': self.assets}
        mockrender = mock.Mock()
        origrender = listwriter.utils.render
        listwriter.utils.render = mockrender
        list(self.writer.render(context))
        mockrender.assert_called_with('templates', 'foo.html', context)
        listwriter.utils.render = origrender

    def test_default_template_path(self):
        context = {'assets': self.assets}
        mockrender = mock.Mock()
        origrender = listwriter.utils.render
        listwriter.utils.render = mockrender
        list(self.writer.render(context))
        mockrender.assert_called_with('./', 'foo.html', {
            "assets": self.assets, "asset": self.asset})
        listwriter.utils.render = origrender
