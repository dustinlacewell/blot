from blot.assets import categorytags, ContentAsset, Categories, Tags


def test_categorytags():
    processor = categorytags.CategoryTags()
    asset = ContentAsset("/foo.md", "content", {"category": "value", "tags": "foo"})
    context = dict(assets=[asset])
    Categories().process(context)
    Tags().process(context)
    processor.process(context)
    category = context['categories'][0]
    assert category["tags"] == asset["tags"]
