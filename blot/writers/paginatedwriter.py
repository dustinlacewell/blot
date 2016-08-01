import math

from blot import utils


class PageHelper(object):
    '''
    Utility class that providers an iterator that returns slices of the underlying list.
    '''
    def __init__(self, items, size):
        self.items = items
        self.size = size
        self.length = math.ceil(len(items) / float(size))

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        index = float(index)
        if index >= self.length:
            raise IndexError("PageHelper has no {} page.".format(index))
        start = int(index * self.size)
        return self.items[start:start + self.size]

    def __iter__(self):
        index = 0
        while index < self.length:
            yield self[index]
            index += 1


class PaginatedWriter(object):
    '''
    Writer that paginates the underlying assets and renders a template for each page.

    PaginatedWriter takes divides its assets into groups of the specified size and
    renders the specified template for each group. The global context variable will
    point to the URL of the first page.

    The context when rendering each of the pages contains a number of variables for
    navigating between the pages.
    '''

    def __init__(self, assets, variable_name, template, path, size=10):
        self.assets = assets
        self.variable_name = variable_name
        self.template = template
        self.path = path
        self.size = size
        self.helper = PageHelper(assets, size)

    def pathfor(self, index):
        '''generate the target path for a given page'''
        postfix = index + 1 if index > 0 else ''
        return self.path.format(page=postfix)

    def target(self, context):
        path = self.pathfor(0)  # get path for first page
        context[self.variable_name] = utils.pathurl(path)

    def render(self, original_context):
        template_path = original_context.get('TEMPLATE_PATH', './')
        helper = PageHelper(self.assets, self.size)
        for index, assets in enumerate(helper):
            context = original_context.copy()
            context['assets'] = assets
            context['page_number'] = index + 1
            context['first_page'] = self.pathfor(0)
            context['last_page'] = self.pathfor(len(self.helper) - 1)
            if index > 0:
                context['previous_page'] = self.pathfor(index - 1)
            else:
                context['previous_page'] = None
            if index < len(self.helper) - 1:
                context['next_page'] = self.pathfor(index + 1)
            else:
                context['next_page'] = None
            path = self.pathfor(index)
            output = utils.render(template_path, self.template, context)
            yield (path, output)

