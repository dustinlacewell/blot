from blot import utils


class ListWriter(object):
    '''
    Writer that renders a jinja2 template for each targetted asset.
    '''
    def __init__(self, assets, template, path):
        self.assets = assets  # targetted assets
        self.template = template  # filename of template to use
        self.path = path  # filesystem path pattern to render to

    def target(self, context):
        # render the path pattern with each asset's metadata
        for asset in self.assets:
            # set the result on each asset
            asset.target = self.path.format(**asset.metadata)

    def render(self, context):
        # render each of the assets out to its target
        path = context.get('TEMPLATE_PATH', './')
        context['assets'] = self.assets
        for asset in self.assets:
            context['asset'] = asset
            output = utils.render(path, self.template, context)
            yield (asset.target, output)
