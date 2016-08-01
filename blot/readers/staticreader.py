import os

from blot.assets import ContentAsset


class StaticReader(object):
    '''
    Simple reader which performs no content or metadata parsing.
    '''
    def __init__(self, asset_class=ContentAsset):
        self.asset_class = asset_class

    def read(self, paths):
        assets = []
        for path in paths:
            with open(path, 'r') as fobj:
                content = fobj.read()
                asset = self.asset_class(path, content, {})
                assets.append(asset)
        return assets
