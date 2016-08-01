import time

from blot.assets import autosummary, ContentAsset

content = "<html><body><p></p><p></p><p>This is a test.</p></body></html>"

def test_autosummary():
    processor = autosummary.AutoSummary()
    asset = ContentAsset("/foo.md", content, {})
    context = dict(assets=[asset])
    processor.process(context)
    assert asset["summary"] == "This is a test."
