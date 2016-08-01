import os


class PathMetadata(object):
    '''
    Generates a number of metadata properties based on an asset's source path.
    '''
    def process(self, context):
        for asset in context['assets']:
            md = asset.metadata
            dirname, basename = os.path.split(asset.source)
            filename, extension = os.path.splitext(basename)
            ancestry, parent = os.path.split(dirname)
            md.update(dict(
                dirname=dirname, basename=basename,
                filename=filename, extension=extension,
                ancestry=ancestry, parent=parent,
            ))
