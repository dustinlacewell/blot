import unittest

import mock

from blot.writers import indexwriter
from blot.utils import pathurl


class IndexWriterCase(unittest.TestCase):
    def setUp(self):
        self.writer = indexwriter.IndexWriter(
            None, 'foo', 'foo.html', '/foo/index.html')

    def test_target(self):
        context = {}
        self.writer.target(context)
        assert context['foo'] == pathurl('/foo/index.html')

    def test_render(self):
        context = {
            'TEMPLATE_PATH': "templates",
            'assets': None}
        mockrender = mock.Mock()
        origrender = indexwriter.utils.render
        indexwriter.utils.render = mockrender
        list(self.writer.render(context))
        mockrender.assert_called_with('templates', 'foo.html', context)
        indexwriter.utils.render = origrender

    def test_default_template_path(self):
        context = {'assets': None}
        mockrender = mock.Mock()
        origrender = indexwriter.utils.render
        indexwriter.utils.render = mockrender
        list(self.writer.render(context))
        mockrender.assert_called_with('./', 'foo.html', {"assets": None})
        indexwriter.utils.render = origrender
