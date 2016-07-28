import bs4

from summarize import find_likely_body, summarize_blocks, Summary


class AutoSummary(object):
    def __init__(self, key="summary", limit=None):
        self.key = key

    def process(self, context):
        for asset in context['assets']:
            if asset.get(self.key):
                continue

            html = bs4.BeautifulSoup(asset.content, 'html.parser')
            summaries = summarize_blocks(map(lambda p: p.text, html.find_all('p')[2:3]))
            asset[self.key] = summaries[0]
