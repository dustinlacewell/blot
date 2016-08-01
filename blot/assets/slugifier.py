from slugify import Slugify


class Slugifier(object):
    '''
    Processor that slugifies an asset metadata property.
    '''
    def __init__(self, source_attr='title'):
        super(Slugifier, self).__init__()
        self.slugifier = Slugify(to_lower=True)
        self.source_attr = source_attr

    def process(self, context):
        for asset in context['assets']:
            md = asset.metadata
            md['slug'] = self.slugifier(md[self.source_attr])
