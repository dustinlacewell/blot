.. blot documentation master file, created by
   sphinx-quickstart on Sun Jul 31 16:26:30 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to blot's documentation!
================================

Blot is a static site generator built upon an idea of generalized content
processing. It has no pre-concieved notions of the kinds of content sources you have or
how they should be utilized in site generation. Instead, the problem of site-generation is modeled as a general problem of content transformation. In Blot the problem model is something like:

  - What types of content are there?
  - For a given content type, where should we get the content?
  - How should content sources be parsed into assets?
  - What kinds of asset transformations should be made?
  - How do assets relate to output content?
  - How should output content be rendered?
  - How should output content be written?


At a high-level this problem can be broken into two steps:

  - **Content Reading** where content sources are discovered, parsed and processed. The
    result is a context object containing all the resulting content assets.
  - **Asset Writing** where the resulting file-system location of assets are determined
    and they are rendered to disk.

Blot site-configuration reflects this process and consists of defining pipelines that answer all of these questions. Luckily, nice abstractions make it easy for you to define such pipelines for your needs.


.. toctree::
   :caption: User Guide
   :glob:
   :titlesonly:
   :hidden:
   :maxdepth: 2

   Installation <guide/installation>
   Basic Concepts <guide/basic_concepts>
   Reading Content <guide/reading_content>
   Writing Assets <guide/writing_assets>


.. toctree::
   :glob:
   :titlesonly:
   :hidden:

   API Documentation <autodoc/blot>


.. toctree::
   :caption: Tutorials
   :glob:
   :titlesonly:
   :hidden:
   :maxdepth: 2

   Building a Blog <tutorials/building_a_blog>

