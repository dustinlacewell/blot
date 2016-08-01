import unittest

import mock

from blot.assets import PathMetadata, ContentAsset

class PathMetadataCase(unittest.TestCase):
    def test_process(self):
        processor = PathMetadata()
        asset = ContentAsset("/foo/bar.md", None)
        context = dict(assets=[asset])
        processor.process(context)
        assert asset["dirname"] == "/foo"
        assert asset["basename"] == "bar.md"
        assert asset["filename"] == "bar"
        assert asset["extension"] == ".md"
        assert asset["ancestry"] == "/"
        assert asset["parent"] == "foo"
