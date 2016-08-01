Writers
=======

Writers are responsible for performming asset targetting and rendering. Some writers produce multiple output files some produce a single ouputs. Some writers involve templated rendering that involve the global context but that isn't nessecary.

The same assets may be passed to multiple writers, but only one targeting writer per set of assets should be used. If multiple targeting writers are used, only the targeting that is performed last will apply.

Targetting Writers
==================

Targeting writers perform targeting on the assets passed to them, updating their `target` properties. This affects how links to assets are generated.


ListWriter
----------

:py:class:`blot.writers.ListWriter <blot.assets.listwriter.ListWriter>` will perform targeting on each asset based on the provided path pattern. For each asset, its metadata will be used to interpolate the path pattern and this should result in a path unique to the asset. If not, assets will overwrite each other. The output will be the result of rendering the specified template against the global context. The following context updates are made for each asset's rendering:

    :code:`assets` a list of all the assets the type shared by the currently rendering asset

    :code:`asset` the currently rendered asset


Non-targetting Writers
======================

Since Non-targetting writers do not update asset targets it is safe to use multiple of them against any given assets.


StaticWriter
-----------

:py:class:`blot.writers.StaticWriter <blot.writers.staticwriter.StaticWriter>` writes each asset without any rendering of the content whatsoever. And so it takes only a target path pattern that should contain some differentiating interpolation variables.


IndexWriter
-----------

:py:class:`blot.writers.IndexWriter <blot.writers.indexwriter.IndexWriter>` should take a non-interpolated destination path where the provided template will be rendered. This is the only output file and it is rendered with only a single context update:

    :code:`assets` a list of all the writer's assets

Additionally, during targeting this writer will update the global context with a key specified by `variable_name` that points to the URL linking to the output file making it available globally to rendering of all writers.

PaginatedWriter
---------------

:py:class:`blot.writers.PaginatedWriter <blot.assets.paginatedwriter.PaginatedWriter>` takes an interpolatable destination path pattern. This pattern requires the inclusion of an interpolation variable named `{page}`.

Based on the `size` parameter, this writer will render multiple outputs based on simple pagination. For each page it will render the given template with the following context updates:

 :code:`assets` the subset of assets in the current page
 :code:`page_number` the current page number
 :code:`first_page` url to the first page
 :code:`last_page` url to the last page
 :code:`previous_page` url to the page before the current one
 :code:`next_page` url to the page after the current one




