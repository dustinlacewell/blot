from blot.assets import Aggregator, AggregateCloud


class Categories(Aggregator):
    def __init__(self, key='category', pattern='(.*)'):
        super(Categories, self).__init__(key, pattern)

    def process_aggregate(self, category, asset):
        asset['category'] = category

    def finish(self, context, categories):
        context['categories'] = categories.values()
        context['categories_cloud'] = AggregateCloud(categories)
