import os

from . import loaders, readers, assets, writers

def _generate_type_context(type_config):
    '''
    Generate a context dictionary specific to a Content-Type.

    Takes a content type configuration dictionary and produces
    a content type specific context for rendering. This
    involves loading and reading any discoverable content
    sources and applying all of the configured asset processors
    against each.

    The resulting context's `assets` key will contain a list
    of the processed Content Asset objects. Other keys may be
    populated by Processors with secondary Processed Assets.

    Processors may also add keys not containing assets.
    '''
    context = {}
    loader = type_config['loader']
    reader = type_config['reader']
    processors = type_config['processors']

    # discover content with loader
    content_paths = loader.load()
    # parse source for content and metadata
    context['assets'] = reader.read(content_paths)
    # process content assets and update context
    for processor in processors:
        processor.process(context)
    return context


def read(context, content_types):
    '''
    Stage 1 of site generation.

    For each defined content type:
      - use loader to discover input content
      - use reader to parse input content into content assets
      - run each processor against the assets
      - return resulting context dictionary containing everything

    '''
    for type_name, type_config in content_types.items():
        # each content type produces a distinct context which is
        # stored under the name of the content type in the global
        # rendering context
        context[type_name] = _generate_type_context(type_config)
    # return the now asset populated global context
    return context


def write(context, writers, build_path="output"):
    '''
    Stage 2 of site generation.

    For each specified writer:
      - Resolve each asset's target output location on disk

    For each specified writer:
      For each asset fed to the writer:
        - Render the asset using the global context
        - Write the asset to disk

    The reason for targetting all assets before rendering is so that during rendering
    the URLS for all assets are available. This allows any templates being used to
    render a specific content type to include links to other assets of other content
    types.

    '''
    # have each Writer target all of its Content Assets
    for writer in writers:
        writer.target(context)

    # have each Writer render and write all of its Content Assets
    for writer in writers:
        context_copy = context.copy()  # rendering should be safe
        for target, content in writer.render(context_copy):
            full_target = os.path.join(build_path, target)
            path, _ = os.path.split(full_target)

            if not os.path.exists(path):
                os.makedirs(path)

            with open(full_target, 'w') as fobj:
                fobj.write(content)
