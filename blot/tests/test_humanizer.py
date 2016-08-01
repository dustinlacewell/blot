import time

from blot.assets import humanizer, ContentAsset


def test_humanizer():
    processor = humanizer.Humanizer()
    date = time.strftime("%c")
    asset = ContentAsset("/foo.md", "content", {"date": date})
    context = dict(assets=[asset])
    processor.process(context)
    assert asset["date"] == "now"
