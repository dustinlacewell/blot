import os

from markdown import Markdown

from blot.assets import ContentAsset


class MarkdownReader(object):
    def __init__(self,
                 asset_class=ContentAsset,
                 file_extensions=['md', 'markdown', 'mkd', 'mdown'],
                 markdown_extensions=['markdown.extensions.meta']):
        self.asset_class = asset_class
        # add periods to extensions (since splitext returns extensions that way)
        self.file_extensions = ["." + e if e[0] != "." else e for e in file_extensions]
        self.markdown = Markdown(extensions=markdown_extensions)

    def read_path(self, path):
        with open(path, 'r') as fobj:
            data = fobj.read()
            content = self.markdown.convert(data)
            metadata = self.markdown.Meta
            for k, v in metadata.items():
                if len(v) == 1:
                    metadata[k] = v[0]
            self.markdown.reset()
            return self.asset_class(path, content, metadata)

    def read(self, paths):
        assets = []
        for path in paths:
            _, ext = os.path.splitext(path)
            if ext in self.file_extensions:
                asset = self.read_path(path)
                assets.append(asset)
        return assets
