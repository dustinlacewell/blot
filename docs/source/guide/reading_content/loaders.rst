Loaders
=======

Loaders are responsible for discovering source content on disk and determining which of those sources are relevant to its content type.


BasicLoader
-----------

Blot comes with a fairly simple loader that finds files on disk and filters them based on extension and some simple exclusion and inclusion rules.

.. autoclass:: blot.loaders.BasicLoader
