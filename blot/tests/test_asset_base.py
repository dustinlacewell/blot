import unittest

from mock import Mock

from blot.utils import pathurl
from blot.assets import ContentAsset, Aggregate, Aggregator


class ContentAssetCase(unittest.TestCase):
    def test_access(self):
        asset = ContentAsset("/foo.md", "foo", metadata={"bar": "baz"})
        assert asset["bar"] == asset.get("bar")
        asset["bar"] = "boz"
        assert asset["bar"] == "boz"

    def test_url_property(self):
        asset = ContentAsset("/foo.md", "")
        url = pathurl("/foo/")
        asset.target = url
        assert asset.url == url


class AggregateCase(unittest.TestCase):
    def test_str(self):
        asset = Aggregate("foo")
        assert str(asset) == "foo"
        assert repr(asset) == "foo"


class AggregatorPatternCase(unittest.TestCase):
    def setUp(self):
        self.agger = Aggregator("key", "(.*)")
        self.asset = ContentAsset("/foo.md", "content", {"key": "value"})

    def test_values(self):
        assert self.agger.get_values(self.asset) == ["value"]
        self.agger.process({'assets': [self.asset]})
