import os

from blot.assets import ContentAsset


class StaticReader(object):
    def __init__(self, extensions, asset_class=ContentAsset):
        self.asset_class = asset_class
        # add periods to extensions (since splitext returns extensions that way)
        self.extensions = ["." + e if e[0] != "." else e for e in extensions]

    def read(self, paths):
        assets = []
        for path in paths:
            _, ext = os.path.splitext(path)
            if ext in self.extensions:
                with open(path, 'r') as fobj:
                    content = fobj.read()
                asset = self.asset_class(path, content, {})
                assets.append(asset)
        return assets
