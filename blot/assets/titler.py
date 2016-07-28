from titlecase import titlecase


class Titler(object):
    def __init__(self, source_attr):
        super(Titler, self).__init__()
        self.source_attr = source_attr

    def process(self, context):
        for asset in context['assets']:
            md = asset.metadata
            title = md[self.source_attr]
            title = title.replace("_", " ")
            title = title.replace("-", " ")
            md['title'] = titlecase(title)
