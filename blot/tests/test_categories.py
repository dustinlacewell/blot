from blot.assets import categories, ContentAsset


def test_categories():
    processor = categories.Categories()
    asset = ContentAsset("/foo.md", "content", {"category": "value"})
    context = dict(assets=[asset])
    processor.process(context)
    assert context['categories'][0]['name'] == "value"
    assert asset['category']["name"] == "value"
