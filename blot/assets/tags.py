from slugify import slugify

from blot.assets import Aggregator


class Tags(Aggregator):
    '''
    Simple multi-value Aggregator which splits the named metadata property by comma.
    '''
    def __init__(self, key='tags', pattern="([^,]+)"):
        super(Tags, self).__init__(key, pattern)

    def process_aggregate(self, tag, asset):
        tag['name'] = slugify(tag['name'])
        asset_tags = asset.get('tags')
        if not isinstance(asset_tags, list):
            asset['tags'] = []
        asset['tags'].append(tag)

    def finish(self, context, tags):
        context['tags'] = tags.values()
