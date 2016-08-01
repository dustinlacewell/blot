from blot.assets import Aggregator


class Categories(Aggregator):
    '''
    A simple single value Aggregator for organizing content assets.
    '''

    def __init__(self, key='category', pattern='(.*)'):
        super(Categories, self).__init__(key, pattern)

    def process_aggregate(self, category, asset):
        # store the derived aggregate onto the `category` property of the asset
        asset['category'] = category

    def finish(self, context, categories):
        # make the list of categories aggregated for this content type available in
        # the content type's context under `categories`
        context['categories'] = categories.values()
