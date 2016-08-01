Basic Concepts
==============

With a typical site generator you would probably write a declarative configuration file that specified to the generator framework a bunch of settings like where your posts are, how you want categories and tags setup and so on. It may even be flexible enough to let you specify where your content should be loaded from and how it should be layed out when rendered.

However, you're usually specifying essentially configuration variables to built-in mechanisms within the framework. If there is no configuration expressable to get those mechanisms to generate the site precisely how you'd like the only usual solutions are plugin systems or forking.


Composable Pipelining
---------------------

What if we could ease out those internal mechanisms and make them composable? If we could, we wouldn't be limited only to the behaviors available from built-in mechanisms. We can simply use a different mechanism that serves the same role but more how we'd like.

This results in a much more procedural build process. Instead of writing a long list of configuration variables, you're specifying the mechanisms of the pipeline for each kind of content you have.


Site Generation Process
-----------------------

Site generation is modeled as a generic process of "content transformation". A site may contain various kinds of content:

  - chronological articles
  - static pages
  - structured data
  - media assets (css, js, images)

For the purposes of site generation, the concerns for each of these content types are the same:

  - where is the content source coming from?
  - how is the content source parsed?
  - how should parsed content assets be processed?
  - how should output content be rendered?
  - where should output content be written?

In each case the need to load some stuff from disk, maybe do stuff to it, maybe render it into something else, and to write it somewhere is universal. We can visualize the pipeline for a given content type as::

    +-------------------+        +------------------+       +------------------+
    |                   |        |                  |       |                  |
    |  Content Sources  +------> |  Content Assets  +-----> |  Output Content  |
    |                   |        |                  |       |                  |
    +-------------------+        +------------------+       +------------------+

Asset Processing
----------------

Once content sources have been loaded from disk and potentially parsed, the resulting content assets are objects that contain the content and optional metadata. Its easy to imagine then, those assets finding their way to the disk at the end of the pipeline.

For example, we might have some articles written in Markdown, which are loaded and parsed into content assets. Those articles are then written out as html in a convienent place. But what about other kinds of content that don't have source files on disk? Categories are good example.

If you have a category assigned in the metadata of each article, you probably want pages generated that index the articles belonging to that category. But so far, we've only seen that content assets that come from content sources can be written out. However, during asset processing, additional asset types can be generated. This allows your content sources to "fan out" to multiple logical asset types, each with its own distinct output configuration::


                                  +------------------+       +------------------+
                                  |                  |       |                  |
                                  | Generated Assets +-----> |  Output Content  |
                                  |                  |       |                  |
                                  +---------^--------+       +------------------+
                                            |
     +-------------------+        +------------------+       +------------------+
     |                   |        |                  |       |                  |
     |  Content Sources  +------> |  Content Assets  +-----> |  Output Content  |
     |                   |        |                  |       |                  |
     +-------------------+        +------------------+       +------------------+
                                            |
                                  +---------v--------+       +------------------+
                                  |                  |       |                  |
                                  | Generated Assets +-----> |  Output Content  |
                                  |                  |       |                  |
                                  +------------------+       +------------------+

Output Configurations
---------------------
Similarly to the "fan out" possible between content sources and the asset types generated from them; multiple output configurations can target the same asset types. It should start to be apparent the flexibility of Blog's ability to generate static content::


                                                              +------------------+
                                                              |                  |
                                                          +---> Category Index   |
                                   +------------------+   |   |                  |
                                   |                  |   |   +------------------+
                                   | Category Assets  +---+
                                   |                  |   |   +------------------+
                                   +---------^--------+   |   |                  |
                                             |            +---> Category Details |
                                             |                |                  |
                                             |                +------------------+
                                             |
                                             |                +------------------+
                                             |                |                  |
                                             |            +---> Article Index    |
      +-------------------+        +------------------+   |   |                  |
      |                   |        |                  |   |   +------------------+
      | Markdown Sources  +------> |  Article Assets  +---+
      |                   |        |                  |   |   +------------------+
      +-------------------+        +------------------+   |   |                  |
                                             |            +---> Article Details  |
                                             |                |                  |
                                             |                +------------------+
                                             |
                                             |                +------------------+
                                             |                |                  |
                                             |            +---> Tag Index        |
                                   +---------v--------+   |   |                  |
                                   |                  |   |   +------------------+
                                   |    Tag Assets    +---+
                                   |                  |   |   +------------------+
                                   +------------------+   |   |                  |
                                                          +---> Tag Details      |
                                                              |                  |
                                                              +------------------+

