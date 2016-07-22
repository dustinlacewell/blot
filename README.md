# Overview

Blot is a static site generator with configuration focused on flexibility. Blot has no
pre-concieved notions of the kinds of content that your site will have. Content types
are defined as pipelines which transform source materials into assets useful for
rendering. Assets are then mapped back to the file-system and rendering take place.

The central idea behind Blot is the seperation between the three following concerns:

  - content discovery
  - context processing
  - targetted rendering

Content discovery describes gathering, filtering, and parsing content sources for a
given content type. The result are asset objects with parsed content and associated
meta-data.

Context processing allows for modules to process the loaded assets in various way to
update their metadata, create pagnination indexes and other transformations. Even
wholly new asset objects can be derrived from ones loaded from disk.

Targetted rendering refers to the act of mapping processed content assets to disk by
way of template rendering. This decouples the source assets from how they are
integrated into the site.
