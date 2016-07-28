import os

from blot.writers import utils


class List(object):
    def __init__(self, assets, template, path):
        self.assets = assets
        self.template = template
        self.path = path
        if path.endswith("/"):
            self.path += "index.html"

    def target(self, context):
        for asset in self.assets:
            asset.target = self.path.format(**asset.metadata)

    def render(self, context):
        path = context.get('TEMPLATE_PATH', './')
        context['assets'] = self.assets
        for asset in self.assets:
            context['asset'] = asset
            output = utils.render(path, self.template, context)
            yield (asset.target, output)
