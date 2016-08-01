Readers
=======

Readers are responsible for parsing the content sources passed on by the loader. For each content source, the Reader attempts to produce a :py:class:`blot.assets.ContentAsset`:

.. autoclass:: blot.assets.ContentAsset


StaticReader
------------

The simplest reader in Blot is the :py:class:`blot.readers.staticreader.StaticReader` which performs no parsing on source content. Therefore it also produces no metadata.

.. autoclass:: blot.readers.StaticReader
   :members:


MarkdownReader
--------------

A reader which parses source content as Markdown. If the content source contains a "fenced block" of key-value properties, these will be parsed as the metadata for the asset::

  ---
  title: Awesome Post!
  ---

  Reasons to read this post:
    - it is awesome!
    - because!

.. autoclass:: blot.readers.MarkdownReader
   :members:
