from . import loaders, readers, assets, writers


def build(content_types):
    # asset generation
    asset_types = {}
    for type_name, settings in content_types.items():
        loader = settings["loader"]
        reader = settings["reader"]
        processors = settings["processors"]
        paths = loader.load()
        assets = reader.read(paths)
        for processor in processors:
            assets = processor.process(assets)
        asset_types[type_name] = assets

    # rendering and writing
    for type_name, settings in content_types.items():
        renderer = settings['renderer']
        writer = settings['writer']
        output = renderer.render(asset_types, type_name)
        writer.write(output)
