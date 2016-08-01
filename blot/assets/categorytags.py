class CategoryTags(object):
    '''
    Processor that adds to each Category for a content type, all the Tags of its assets.
    '''
    def process(self, context):
        for asset in context['assets']:
            category = asset.get('category')
            tags = asset.get('tags')
            if category and tags:
                category['tags'] = category.get('tags', [])
                for tag in tags:
                    if tag not in category['tags']:
                        category['tags'].append(tag)
