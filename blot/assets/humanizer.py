import dateparser
import humanize


class Humanizer(object):
    def __init__(self, attr='date'):
        super(Humanizer, self).__init__()
        self.attr = attr

    def process(self, context):
        for asset in context['assets']:
            value = asset[self.attr]
            datetime = dateparser.parse(value)
            asset[self.attr] = humanize.naturaltime(datetime)
