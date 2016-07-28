class Static(object):
    def __init__(self, assets, path):
        self.assets = assets
        self.path = path

    def target(self, context):
        for asset in self.assets:
            asset.target = self.path.format(**asset.metadata)

    def render(self, context):
        context['assets'] = self.assets
        for asset in self.assets:
            context['asset'] = asset
            yield (asset.target, asset.content)
