import os

import markdown2

from blot.assets import ContentAsset


class MarkdownReader(object):
    '''
    Reader which parses a content source as Markdown.

    Metadata should be specified by a "fenced" yaml block at the top of the
    file. Metadata keys will be lower-cased. Duplicate keys will override ones earlier
    in the file.

    '''
    def __init__(self,
                 asset_class=ContentAsset,
                 extras=['metadata', 'fenced-code-blocks']):
        self.asset_class = asset_class
        self.extras = extras

    def read_path(self, path):
        with open(path, 'r') as fobj:
            data = fobj.read()
            content = markdown2.markdown(data, extras=self.extras)
            metadata = {k.lower(): v for k, v in content.metadata.items()}
            return self.asset_class(path, content, metadata)

    def read(self, paths):
        assets = []
        for path in paths:
            asset = self.read_path(path)
            assets.append(asset)
        return assets
