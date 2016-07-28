import jinja2


def render(path, template, context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path)
    ).get_template(template).render(context)
