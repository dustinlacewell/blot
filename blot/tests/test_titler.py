from blot.assets import titler, ContentAsset


def test_titler():
    processor = titler.Titler("title")
    asset = ContentAsset("/foo.md", "content", {"title": "Foo bar-baz the bon_bon"})
    context = dict(assets=[asset])
    processor.process(context)
    assert asset["title"] == "Foo Bar Baz the Bon Bon"
