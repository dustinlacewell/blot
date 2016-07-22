
class ConsoleWriter(object):
    def __init__(self, source_only=False, metadata_only=False, no_content=False):
        self.source_only = source_only
        self.metadata_only = metadata_only
        self.no_content = no_content

    def write(self, asset_types, type_name):
        assets = asset_types[type_name]
        for asset in assets:
            if self.source_only:
                print asset.source
            elif self.metadata_only:
                print asset.metadata
            elif self.no_content:
                print asset.source
                print asset.metadata
            else:
                print asset.source
                print asset.metadata
                print asset.content

        # context = dict(asset_types=asset_types, assets=assets)
        # for asset in assets:
        #     context['asset'] = asset
