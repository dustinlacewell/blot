class CategoryTags(object):
    def process(self, context):
        for asset in context['assets']:
            category = asset.get('category')
            tags = asset.get('tags')
            if category and tags:
                category['tags'] = category.get('tags', [])
                for tag in tags:
                    if tag not in category['tags']:
                        category['tags'].append(tag)
