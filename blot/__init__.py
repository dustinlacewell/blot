import os

from . import loaders, readers, writers


def _generate_type_context(type_config):
    context = {}

    loader = type_config['loader']
    reader = type_config['reader']
    processors = type_config['processors']

    # discover content
    content_paths = loader.load()
    # parse content meta-data assets
    context['assets'] = reader.read(content_paths)
    # process asset meta-data and context
    for processor in processors:
        processor.process(context)
    return context


def read(context, content_types):
    for type_name, type_config in content_types.items():
        context[type_name] = _generate_type_context(type_config)
    return context


def write(context, writers, build_path="output"):
    for writer in writers:
        writer.target(context)

    for writer in writers:
        for target, content in writer.render(context.copy()):
            full_target = os.path.join(build_path, target)
            path, _ = os.path.split(full_target)

            if not os.path.exists(path):
                os.makedirs(path)

            with open(full_target, 'w') as fobj:
                fobj.write(content)
