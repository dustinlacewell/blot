from blot.writers import utils
from blot.utils import pathurl


class Index(object):
    def __init__(self, assets, variable_name, template, path):
        self.assets = assets
        self.variable_name = variable_name
        self.template = template
        self.path = path

    def target(self, context):
        context[self.variable_name] = pathurl(self.path)

    def render(self, context):
        path = context.get('TEMPLATE_PATH', './')
        context['assets'] = self.assets
        output = utils.render(path, self.template, context)
        yield (self.path, output)

