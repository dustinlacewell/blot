import unittest

import mock

from blot.writers import staticwriter
from blot.assets import ContentAsset
from blot.utils import pathurl


class StaticWriterCase(unittest.TestCase):
    def setUp(self):
        self.asset = ContentAsset("/foo.css", None, metadata=dict(basename="foo.css"))
        self.assets = [self.asset]
        self.writer = staticwriter.StaticWriter(self.assets, '/static/{basename}')

    def test_target(self):
        context = {}
        self.writer.target(context)
        assert self.asset.target == "/static/foo.css"

    def test_render(self):
        context = {'assets': self.assets}
        self.writer.target(context)
        results = list(self.writer.render(context))
        assert context['asset'] == self.asset
        assert results == [('/static/foo.css', None)]
