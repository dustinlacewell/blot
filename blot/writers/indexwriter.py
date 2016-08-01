from blot import utils


class IndexWriter(object):
    '''
    Writer that renders a single jinja2 template. The global context is updated with a
    URL to the rendered file during targetting. All assets are passed into the context
    as `assets` during rendering.

    '''
    def __init__(self, assets, variable_name, template, path):
        self.assets = assets  # targetted assets
        self.variable_name = variable_name  # global context variable for URL
        self.template = template  # filename of template to use
        self.path = path  # filesystem path to write to

    def target(self, context):
        # update global context with URL to this index
        context[self.variable_name] = utils.pathurl(self.path)

    def render(self, context):
        path = context.get('TEMPLATE_PATH', './')
        # add this index's assets to the context
        context['assets'] = self.assets
        output = utils.render(path, self.template, context)
        yield (self.path, output)

