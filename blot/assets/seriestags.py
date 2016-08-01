class SeriesTags(object):
    '''
    Processor that adds to each Series for a Content Type, all the Tags of its assets.
    '''
    def process(self, context):
        for asset in context['assets']:
            series = asset.get('series')
            tags = asset.get('tags')
            if series and tags:
                series['tags'] = series.get('tags', [])
                for tag in tags:
                    if tag not in series['tags']:
                        series['tags'].append(tag)
