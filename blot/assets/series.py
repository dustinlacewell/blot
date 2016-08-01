import re
from operator import itemgetter


from titlecase import titlecase

from blot.utils import get_values
from blot.assets import Aggregator


class Series(Aggregator):
    '''
    Aggregator which attempts to automatically discover multi-part content series.

    Like other Aggregators the Series processor generates a new set of assets based on
    values extracted from a specified key of some target assets. However, the Series
    processor will only generate new assets for aggregate values found across two or
    more target assets.

    For each Series generated a number of metadata properties are added to target
    assets. These properties contain the first, last, previous and next target assets
    in the Series. This allows a theme to construct navigation between each asset in
    the Series.

    In addition to the normal aggregation metadata property, the Series processor
    requires direction for deriving the order of assets in the Series. So the
    `part_key` and `part_pattern` are used to select this value from the metadata of
    target assets. If the extracted part value is 'index.html' it will automatically be
    converted to 1, putting it as the first part in the series.

    '''

    def __init__(self, key='parent', pattern="(.*)",
                 part_key='filename', part_pattern="(.*)"):
        super(Series, self).__init__(key, pattern)
        self.part_key = part_key
        self.part_pattern = re.compile(part_pattern)

    def process_aggregate(self, series, asset):
        '''generate a title for the series itself'''
        title = series['name'].replace("-", " ")
        title = title.replace("_", " ")
        series['title'] = titlecase(title)

    def get_part_number(self, asset):
        '''derive the part number of an asset'''
        part_number = get_values(asset, self.part_key, self.part_pattern)[0]
        if part_number == 'index':
            return 1
        else:
            return int(part_number)

    def finish(self, context, series):
        # only aggregates containing 2 or more assets are valid series
        valid_series = []
        for name, series_obj in series.items():
            assets = series_obj['assets']
            asset_count = len(assets)
            if asset_count > 1:
                # if the series is actually valid, then update its assets
                for asset in assets:
                    asset['series'] = series
                    asset['part_count'] = asset_count
                    asset['part_number'] = self.get_part_number(asset)
                # once part numbers are known, sort the series assets
                assets.sort(key=itemgetter('part_number'))
                # add relative parts for navigation
                for index, asset in enumerate(assets):
                    asset['first_part'] = assets[0]
                    asset['last_part'] = assets[-1]
                    asset['next_part'] = assets[(index + 1) % asset_count]
                    asset['previous_part'] = assets[index - 1]
                valid_series.append(series_obj)
        # add the series to the target content type's context
        context['series'] = valid_series
