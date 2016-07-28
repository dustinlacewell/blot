from re import compile
from operator import itemgetter

from blot.utils import pathurl


class ContentAsset(object):
    def __init__(self, source, content, metadata={}):
        self.source = source
        self.content = content
        self.metadata = metadata
        self.target = None

    def __getitem__(self, key):
        return self.metadata[key]

    def __setitem__(self, key, value):
        self.metadata[key] = value

    def get(self, key, default=None):
        return self.metadata.get(key, default)

    @property
    def url(self):
        return pathurl(self.target)


class Aggregate(ContentAsset):
    def __init__(self, name):
        super(Aggregate, self).__init__(None, None, dict(name=name, assets=[]))

    def __str__(self):
        return self.get('name', '')

    def __repr__(self):
        return str(self)

class Aggregator(object):
    def __init__(self, key, pattern, asset_class=Aggregate):
        self.key = key
        self.pattern = compile(pattern)
        self.asset_class = asset_class

    def get_values(self, asset):
        source = asset.get(self.key, '')
        return [v.strip() for v in self.pattern.findall(source) if v]

    def process_aggregate(self, aggregate, asset):
        pass

    def finish(self, context, aggregates):
        pass

    def process(self, context):
        aggregates = dict()
        for asset in context['assets']:
            values = self.get_values(asset)
            for value in values:
                aggregate = aggregates.get(value) or self.asset_class(value)
                aggregate['assets'].append(asset)
                self.process_aggregate(aggregate, asset)
                aggregates[value] = aggregate
        self.finish(context, aggregates)


class AggregateCloud(object):
    def __init__(self, aggregates):
        self.aggregates = aggregates
        self.totals = self.calculate_totals(aggregates)

    def calculate_totals(self, aggregates):
        totals = []
        for name, aggregate in aggregates.items():
            assets = aggregate['assets']
            totals.append([name, len(assets)])
        return sorted(totals, key=itemgetter(1), reverse=True)

    def __call__(self, minsize=0.8, maxsize=1.0, count=None, items=None):
        if items:
            aggregates = {k: v for k, v in self.aggregates.items() if v in items}
            totals = self.calculate_totals(aggregates)
            totals = totals[:count]
        else:
            totals = self.totals[:count]
        raw_totals = [i[1] for i in totals]
        max_total = max(raw_totals) if raw_totals else 1
        # generate sizes
        cloud = []
        for name, total in totals:
            size = (total / max_total) * (maxsize - minsize) + minsize
            cloud.append((self.aggregates[name], size))
        return cloud
