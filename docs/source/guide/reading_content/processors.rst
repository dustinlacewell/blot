Processors
==========

After all the content sources have been parsed by readers into content assets they are fed through a pipeline of processors. Each processor defined for the content type are in order.

Processing Context
------------------

For each content type a private context dictionary is created while processing for that content type takes place. The content assets produced by the reader are stored under the :code:`assets` key. As each processor is ran, it receives this context dictionary and can retrieve the content type's assets through that key.

Asset Modification
------------------

One use of processors is to iterate over the content assets and modify them in some way. The changes made by one processor will be visible processors later in the pipeline. In this way, changes introduced by asset processing are cummulative.

Context Modification
--------------------

Processors are also free to change the content type context dictionary in anyway, including adding or removing keys or modifying the values that they point to.

Generated Assets
----------------

Processors may also produce completely new sets of content assets and store them under keys in the context dictionary. These assets can be targetted for output just like the core content type assets.


Basic Processors
================

AutoSummary
-----------

:py:class:`blot.assets.AutoSummary <blot.assets.autosummary.AutoSummary>` will attempt to parse asset contents as HTML and automatically generate a summary. The summary will be stored on the asset's :code:`summary` metadata property by default.

Humanizer
---------

:py:class:`blot.assets.Humanizer <blot.assets.humanizer.Humanizer>` will apply a humanizing transformation to date, time and other numerical metadata properties.

PathMetadata
------------

:py:class:`blot.assets.PathMetadata <blot.assets.metadata.PathMetadata>` will derive a number of metadata properties from various aspects of the asset's source path.


Slugifier
---------

:py:class:`blot.assets.Slugifier <blot.assets.slugifier.Slugifier>` will slugify a named metadata property and store the result on another metadata property.


Aggregation Processors
======================

A certain kind of processor is useful for generating new types of "aggregate assets" from those being processed. These new assets contain a list of all the original assets that share a specific metadata property value. These generated :py:class:`blot.assets.base.Aggregate` based assets can then be targetted for output independently from the original assets.

A concrete use-case would be a site that featured articles from multiple authors. It might be useful to generate a list of articles written by each author. A :py:class:`blot.assets.Aggregator` based processor could do just that. Configured to aggregate an :code:`author` metadata propety a new set of aggregate assets would be generated for each unique author. It might be then desirable to an index page of featured authors and detail pages for each author listing the articles they've written. This is no problem because generated assets can be targeted for writing the same as core content type assets.

Categories
----------

:py:class:`blot.assets.Categories <blot.assets.categories.Categories>` will aggregate assets across their :code:`category` metadata property value by default. Generated category aggregates will be stored in the content type context dictionary under the :code:`categories` key. Each aggregated asset in a category will have its :code:`category` property updated with the corresponding Category instance.

Series
------

:py:class:`blot.assets.Series <blot.assets.series.Series>` will aggregate assets across their :code:`series` metadata property value by default. Generated series aggregates will be stored in the content type context dictionary under the :code:`series` key. Each aggregated asset in a series will have its :code:`series` property updated with the corresponding Series instance. Unlike Categories, Series are only generated if it contains 2 or more aggregated assets.

Tags
----

:py:class:`blot.assets.Tags <blot.assets.tags.Tags>` will aggregate assets across their :code:`tags` metadata property value by default. The metadata property is split on a comma and aggregation takes place for each individual tag. Generated tag aggregates will be stored in the content type context dictionary under the :code:`tags` key. Each aggregated asset that has at least one tag will have its :code:`tags` property updated with a list of corresponding Tag instances.


CategoryTags
------------

:py:class:`blot.assets.CategoryTags <blot.assets.categorytags.CategoryTags>` will attempt to aggregate all of the Tags for all assets in a given Category and store this superset of tags on the Category's :code:`tags` metadata property.

SeriesTags
------------

:py:class:`blot.assets.SeriesTags <blot.assets.seriestags.SeriesTags>` will attempt to aggregate all of the Tags for all assets in a given Series and store this superset of tags on the Series' :code:`tags` metadata property.




