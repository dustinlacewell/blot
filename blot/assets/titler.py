from titlecase import titlecase


class Titler(object):
    '''
    Processor that titlecases an asset metadata property.
    '''
    def __init__(self, source_attr):
        super(Titler, self).__init__()
        self.source_attr = source_attr

    def process(self, context):
        for asset in context['assets']:
            md = asset.metadata
            title = md[self.source_attr]
            title = title.replace("-", " ")
            title = title.replace("_", " ")
            md['title'] = titlecase(title)
