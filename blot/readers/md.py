import os

import markdown2

from blot.assets import ContentAsset


class MarkdownReader(object):
    def __init__(self,
                 asset_class=ContentAsset,
                 extensions=['md', 'markdown', 'mkd', 'mdown'],
                 extras=['metadata', 'fenced-code-blocks']):
        self.asset_class = asset_class
        # add periods to extensions (since splitext returns extensions that way)
        self.extensions = ["." + e if e[0] != "." else e for e in extensions]
        self.extras = extras

    def read_path(self, path):
        with open(path, 'r') as fobj:
            data = fobj.read()
            content = markdown2.markdown(data, extras=self.extras)
            metadata = content.metadata
            for k, v in metadata.items():
                if isinstance(v, list) and len(v) == 1:
                    metadata[k] = v[0]
            self.markdown.reset()
            return self.asset_class(path, content, metadata)

    def read(self, paths):
        assets = []
        for path in paths:
            _, ext = os.path.splitext(path)
            if ext in self.extensions:
                asset = self.read_path(path)
                assets.append(asset)
        return assets
