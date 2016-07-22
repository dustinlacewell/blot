import os


class PathMetadata(object):
    def __init__(self, attrs=[]):
        self.target_attrs = attrs

    def process(self, assets):
        assets = list(assets)
        for asset in assets:
            md = asset.metadata
            dirname, basename = os.path.split(asset.source)
            filename, extension = os.path.splitext(basename)
            ancestry, parent = os.path.split(dirname)
            md.update(dict(
                dirname=dirname, basename=basename,
                filename=filename, extension=extension,
                ancestry=ancestry, parent=parent,
            ))
        return assets
