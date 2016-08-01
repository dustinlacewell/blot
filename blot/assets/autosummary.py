import bs4

from blot.summarize import summarize_blocks


class AutoSummary(object):
    '''
    Generates a summary from an asset's content.
    '''
    def __init__(self, key="summary"):
        self.key = key  # where to store the summary

    def process(self, context):
        for asset in context['assets']:
            # don't generate a summary if one has been manually written
            if asset.get(self.key):
                continue

            html = bs4.BeautifulSoup(asset.content, 'html.parser')
            summaries = summarize_blocks(map(lambda p: p.text, html.find_all('p')[2:3]))
            asset[self.key] = summaries[0]  # get the first summary
