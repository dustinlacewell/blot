# Overview

Blot is a static site generator with configuration focused on flexibility. Blot has no
pre-concieved notions of the kinds of content that your site will have. Content types
are defined as pipelines which transform source materials into assets useful for
rendering. Assets are then mapped back to the file-system and rendering takes place.

The central idea behind Blot is the seperation between the three following concerns:

  - **Content discovery** Gathering, filtering, and parsing content sources from
      diskinto asset objects containing parsed content and associated meta-data.
  - **Context processing** Validating, post-processing, aggregation and other
      manipulations of loaded asset objects and the global rendering context.
  - **Targetted rendering** Mapping content assets to templates and resulting
      location on disk.
