from re import compile
from operator import itemgetter

from blot.utils import pathurl, get_values


class ContentAsset(object):
    '''An object with some data and associated metadata.

    ContentAssets represent the result of loading and reading content sources. The
    result of parsing the source source provides its content and optional metadata
    dictionary.

    ContentAssets are fed through a pipeline of processors where they may be modified
    in various ways. Eventually, they are passed to Writers which can render them to
    their final destinations on disk.

    A basic dictionary-like access is avaiable as a shortcut to the asset's
    metadata. Once the assets's `target` attribute has been set, its `url` property
    will become available.

    Some assets are produced by the processing of other assets and have no source.
    '''
    def __init__(self, source=None, content=None, metadata={}):
        self.content = content  # data of the asset
        self.source = source  # where the asset came from (usually a file path)
        self.metadata = metadata  # initial metadata
        self.target = None  # where this asset will live on disk during write

    def __getitem__(self, key):
        return self.metadata[key]

    def __setitem__(self, key, value):
        self.metadata[key] = value

    def get(self, key, default=None):
        return self.metadata.get(key, default)

    @property
    def url(self):
        # a url to the asset based on where it lives on disk
        return pathurl(self.target)


class Aggregate(ContentAsset):
    '''
    A special type of ContentAsset that has two known metadata properties:
      - name : The metadata value of some other ContentAsset this Aggregate is based on
      - assets : The list of ContentAssets in which this Aggregate appears
    '''

    def __init__(self, name, assets=None):
        super(Aggregate, self).__init__(
            None, None, dict(name=name, assets=assets or []))

    def __str__(self):
        return self.get('name', '')

    def __repr__(self):
        return str(self)


class Aggregator(object):
    '''Base-class for an asset processor that generates Aggregates for each value in the
    metadata of processed ContentAssets.

    When used as an asset processor, it will look at a specific metdata property of
    each ContentAsset. For each unique value found at this property, a new Aggregate
    asset will be generated.

    Each Aggregate object contains in its own metadata an `assets` key that contains a
    list of each of the ContentAssets in which the aggregated value was
    found.

    It is up to subclasses of Aggregator to make the list of generated Aggregate assets
    available. Subclasses also have the chance to update each aggregate and the asset
    it comes from.

    Generally, the original content type's context will be updated with a list of the
    Aggregates under a relevant key in the `finish` method. Check the Tags and
    Categories processors for examples.
    '''

    def __init__(self, key, pattern, asset_class=Aggregate):
        self.key = key  # metadata key to aggregate over
        self.pattern = compile(pattern)  # regular expression to extract aggregate values
        self.asset_class = asset_class  # class from which to create new aggregate assets

    def get_values(self, asset):
        '''
        Get the aggregated property value from the asset.
        '''
        return get_values(asset, self.key, self.pattern)

    def process_aggregate(self, aggregate, asset):
        pass

    def finish(self, context, aggregates):
        pass

    def process(self, context):
        '''
        Check each asset in the content Type context and aggregate discovered values
        over the specific metadata key into new assets.
        '''
        aggregates = dict()
        for asset in context['assets']:
            values = self.get_values(asset)
            for value in values:
                aggregate = aggregates.get(value) or self.asset_class(value)
                aggregate['assets'].append(asset)
                self.process_aggregate(aggregate, asset)
                aggregates[value] = aggregate
        self.finish(context, aggregates)
