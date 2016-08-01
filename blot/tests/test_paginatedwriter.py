import unittest

import mock

from blot.assets import ContentAsset
from blot.writers import paginatedwriter
from blot.utils import pathurl


class PaginatedWriterCase(unittest.TestCase):
    def setUp(self):
        self.foo = ContentAsset("/foo.md", None, metadata=dict(filename="foo"))
        self.bar = ContentAsset("/bar.md", None, metadata=dict(filename="bar"))
        self.assets = [self.foo, self.bar]
        self.writer = paginatedwriter.PaginatedWriter(
            self.assets, 'foo', 'foo.html', '/foo/index{page}.html', 1)

        self.call_1  = ('./', 'foo.html', {
            'assets': [self.foo],
            'page_number': 1,
            'first_page': '/foo/index.html',
            'previous_page': None,
            'next_page': '/foo/index2.html',
            'last_page': '/foo/index2.html',})

        self.call_2  = ('./', 'foo.html', {
            'assets': [self.bar],
            'page_number': 2,
            'first_page': '/foo/index.html',
            'previous_page': '/foo/index.html',
            'next_page': None,
            'last_page': '/foo/index2.html',})

    def test_target(self):
        context = {}
        self.writer.target(context)
        assert context['foo'] == pathurl('/foo/index.html')

    def test_default_template_path(self):
        context = {}
        mockrender = mock.Mock()
        origrender = paginatedwriter.utils.render
        paginatedwriter.utils.render = mockrender
        list(self.writer.render(context))
        first_args = list(mockrender.call_args_list[0])[0]
        second_args = list(mockrender.call_args_list[1])[0]
        assert first_args == self.call_1
        assert second_args == self.call_2
        paginatedwriter.utils.render = origrender


    def test_missing_page(self):
        with self.assertRaises(IndexError):
            self.writer.helper[2]
