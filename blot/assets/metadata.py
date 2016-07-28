import os

from blot.utils import splitall


class PathMetadata(object):
    def process(self, context):
        for asset in context['assets']:
            md = asset.metadata
            dirname, basename = os.path.split(asset.source)
            filename, extension = os.path.splitext(basename)
            ancestry, parent = os.path.split(dirname)
            ancestry = splitall(ancestry).reverse()
            md.update(dict(
                dirname=dirname, basename=basename,
                filename=filename, extension=extension,
                ancestry=ancestry, parent=parent,
            ))
