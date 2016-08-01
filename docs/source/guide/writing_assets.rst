Writing Assets
==============


Once all content types have had their assets processed a final context dictionary will be produced. A key in the dictionary corresponding to each content type maps to the content type specific context dictionary that was produced during the processing of each content type. In side each content type context, the :code:`assets` key contains the content type's assets. Additionaly, the processors assigned to the context types may have also populated various keys with generated asset types::

  render_context = {
    'articles': {
      'assets': [...],
      'categories': [...],
      'tags': [...],
    },
    'staticfiles': {
      'assets': [...],
    },
    GLOBAL_VARIABLE_1: "some value",
    GLOBAL_BOOLEAN: False,
  }

Writing involves assigning writers to the various asset types, whether they be core content types or generated ones, to get them written to the filesystem where desired. The writers do this in two steps:

  - **Targeting**: Figure out where some assets should be rendered
  - **Rendering**: Rendering assets to their targetted locations on disk


Targeting
---------

Each content asset as a non-metadata attribute :code:`target` which is for storing the location on disk where the asset should be written to disk. Since Blot a static *site* generator, this location determines its URL as well. During the writing phase, all writers perform targeting on all of their assets before any writer performs rendering. This is to ensure that during rendering, the URLs of all asset types are available. Otherwise, only the URLs of assets already processed could be properly rendered.

If a writer will be rendering output for each targeted asset the target path pattern will generally contain one or more interpolation variables that name metadata properties. This allows the output path for each asset to vary uniquely so they don't overwrite each other.

Rendering
---------

Now that all assets have been properly targeted each writer undergoes rendering wherein it may process the content of assets for the last time. This will typicall involve combining the asset, with the global context and some specified template to produced a rendering of the asset. However, this isn't nessecary writers are free to do whatever or nothing at all. At this point the writer shouldn't be modifying assets or the global context at all.

Once the final content of an asset has been derived it is ready for writing to its target destination.


Performing the Writes
---------------------

With the rendering context in hand :py:meth:`blot.write` can be used to actually generate your site::

  posts = context['posts']['assets']
  categories = context['posts']['categories']
  staticfiles = context['staticfiles']['assets']

  writers = [
    blot.writers.ListWriter(posts, 'post.html', 'posts/{slug}/index.html'),
    blot.writers.IndexWriter(posts, 'posts.html', 'posts/index.html'),
    blot.writers.ListWriter(categories, 'category.html', '/{name}.html'),
    blot.writers.IndexWriter(categories, 'categories.html', 'index.html'),
    blot.writers.StaticWriter(staticfiles, 'static/{filename}'),
  ]

  blog.write(context, writers)



.. toctree::
    :Maxdepth: 1
    :hidden:

    writing_assets/writers


