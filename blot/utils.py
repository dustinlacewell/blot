import re
from operator import itemgetter

import jinja2


def get_values(asset, key, pattern="(*.)"):
    '''
    Returns values extracted from a metadata property of an asset named by key.
    '''
    if isinstance(pattern, basestring):
        pattern = re.compile(pattern)
    source = asset.get(key, '')
    return [v.strip() for v in pattern.findall(source) if v]


def render(path, template, context):
    '''
    Uses Jinja2 to render a template relative to the path with the given context.
    '''
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path)
    ).get_template(template).render(context)


def pathurl(path):
    '''
    Returns a nicer URL for the path on disk for webservers that treat URLs missing a
    filename to be requesting index.html

    If the path ends in `/index.html`, make it end with `/`.

    Make every path absolute.
    '''
    if path.endswith("/index.html"):
        path = path.replace("/index.html", "/")
    if not path.startswith("/"):
        path = "/" + path
    return path


def _calculate_totals(aggregates):
    '''
    From a list of Aggregates return a sorted list of tuples containing each Aggregate
    and how many content assets it has.
    '''
    totals = []
    for aggregate in aggregates:
        assets = aggregate['assets']
        totals.append([aggregate, len(assets)])
    return sorted(totals, key=itemgetter(1), reverse=True)


def generate_cloud(items, minsize=0.8, maxsize=1.0):
    '''
    From a list of Aggregates return a list of tuples containing each Aggregate and its
    relative "size" in a tag cloud normalized to 1.0.

    This is useful for rendering into a <span> tag's `style` attribute to affect
    font-size.
    '''
    totals = _calculate_totals(items)
    raw_totals = [i[1] for i in totals]
    max_total = float(max(raw_totals) if raw_totals else 1)
    cloud = []  # generate sizes
    for item, total in totals:
        size = round(((total - 1) / (max_total - 1 or 1)) * (maxsize - minsize) + minsize, 2)
        cloud.append((item, size))
    return cloud
