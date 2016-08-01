import time

from blot.assets import slugifier, ContentAsset


def test_slugifier():
    processor = slugifier.Slugifier()
    asset = ContentAsset("/foo.md", "content", {"title": "Foo bar-baz the_bon"})
    context = dict(assets=[asset])
    processor.process(context)
    assert asset["slug"] == "foo-bar-baz-the-bon"
