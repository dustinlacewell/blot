Reading Content
===============

The first phase of the build process involves the loading and processing of source content and processed assets. The goal of this phase is to produce the context dictionary that will be used in the second phrase of writing.


Base Context
------------

The reading phase starts with the creation of a base context dictionary. This dictionary contains static information that may be useful to inside the templates of template oriented writers. Another possibility is of pipeline components basing their behavior on top-level values in the context. This is generally avoided when possible, favoring direct configuration of pipeline components, but some components do use top-level context variables as a convience in configuring many of them in a single place.

No keys in of the base context that share a name with any of your content types should be used, since this is where the assets of those content types will be stored.


Content Types
-------------

Before any part of the reading phase can begin a definition of your content types must be provided. This definition is provided as a dictionary of dictionaries. Each top-level key maps the name of a content type to its definition. Each type definition has three required keys:

  - :code:`loader` discovers the paths of candidate content sources
  - :code:`reader` parses the content of discovered sources into assets
  - :code:`processors` a list of asset processors to apply in order

A simple example for loading some Markdown articles might look something like::

  content_types = {
    'articles': {
      'loader': blot.loaders.BasicLoader('content/articles', ['md]),
      'reeader': blot.readers.MarkdownReader(),
      'processors': [
        blot.assets.PathMetadata(),
        blot.assets.AutoSummary(),
        blot.assets.Humanizer('date'),
      ]
    }
  }


Producing the Write Context
---------------------------

Once a base context and content types have been defined the reading process can be performed with :py:meth:`blot.read`::

  write_context = blot.read(base_context, content_types)

.. toctree::
    :maxdepth: 1
    :hidden:

    reading_content/loaders
    reading_content/readers
    reading_content/processors
