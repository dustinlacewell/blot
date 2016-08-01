Building a Blog
===============

This tutorial will showcase some of the ways to use Blot to build a personal blog. This blog will be quite simple but it should have enough features to convey how site generation works.

Getting Setup
-------------

Firstly, you'll need to :doc:`install Blot </guide/installation>`.

One that's done, we recommend `installing Fabric <http://www.fabfile.org/installing.html>`_ which will be useful for writing your site's build script. You can read more about Fabric `at their official overview <http://docs.fabfile.org/en/1.12/tutorial.html>`_ but essentially it is a Python library that helps you write scripts that perform local or remote operations. It then exposes those operations with a nifty cli tool. Brace yourself for the shortest Fabric tutorial in the world:

  **Step 1**: Write a Python file called :code:`fabfile.py` and put functions in it::


    # fabfile.py
    def hello(name):
        print "Hello, {}!".format(name)

  **Step 2**: Use the :code:`fab` cli tool to invoke individual functions from the fabfile::

    $ fab -l
    Available commands:

    hello

    $ fab hello:world
    Hello, world!

    Done.


Listing the Goals
-----------------

For this tutorial we want to build just enough functionality into the blog site to showcase how Blot is used. Let's stick some typical blog features:

  **Chronological Posts**
    - Each post is a markdown file in a :code:`posts` folder.
    - There should be an index of the posts sorted chronologically
    - There should be a page for each post where we can read it
  **Post Categories**
    - Each post has an assigned category
    - There should be an index of the available categories
    - There should be a detail page for each category listing the posts it contains
  **Static Assets**
    - There should be a logo image which we're able to integrate into our theme.
    - There should be a stylesheet which styles our pages

Getting Started
---------------

Create a new directory for your site and within it create a :code:`fabfile.py` file, a :code:`posts` directory and a :code:`theme` directory::

  |-- fabfile.py
  |-- posts/
  `-- theme/

In the theme directory, create the file :code:`style.css`. This will be our first content source. The goal with static files is simple: copy the file from the source to the destination.

Open your :code:`fabfile.py` and enter the following contents::

  base_context = {}

The :code:`base_context` is like the starting-point for data in the build process. Anything you add here will be subject to modification by anything in the pipeline. Settings placed here can also affect the behavior of components in the pipeline. For now, we'll leave it empty.


Content Types
-------------

Add the following to :code:`fabfile.py`::

  content_types = {
      'stylesheets': {
          'loader': blot.loaders.BasicLoader('theme', extensions=['css']),
          'reader': blot.readers.StaticReader(),
          'processors': [
              blot.assets.PathMetadata(),
          ],
      }
  }



The :code:`content_types` dictionary holds all of the content type definitions for our site. Currently, there is only a single type :code:`stylesheets`. Let's take a look at each of its keys:

loader
~~~~~~
Loaders tell Blot where to find the sources of stylesheets. :py:class:`blot.loaders.BasicLoader` supports some basic inclusion and exclusion rules including filtering by file extension.  In this case we're loading all of the files with a :code:`css` extension in the :code:`theme` directory. This should target the :code:`style.css` file.


reader
~~~~~~
The reader is responsible for parsing the content of sources to produce content assets with metadata. However, :py:class:`blot.readers.StaticReader` doesn't perform any parsing and returns source content as-is.


processors
~~~~~~~~~~
A list of asset processors that should get a chance to modify any stylesheets returned by the loader and reader. In this case, a single asset processor :py:class:`blot.assets.PathMetadata` will extract various details of the source file path and add it to the asset metadata. Things like :code:`basename`, :code`dirname`, :code`filename`, :code`extension` and so on.

From this definition we have all we need in order to find stylesheets and load them as content assets.


Reading
-------

Now that we have a base context and our content type definitions, reading can be performed with :py:meth:`blog.read`. This will load our sole stylesheet, add some metadata to it. Finally, an updated version of the base context will be returned. Add the following to :code:`fabfile.py`::

  def build():
     context = blot.read(base_context, content_types)

We now have a function in the :code:`fabfile.py` that we can invoke from the commandline. However if we do, we wont see anything meaningful just by loading content. Let's add a quick debugging print to see the results of the reading process::

  def build():
     context = blot.read(base_context, content_types)
     print context

Now we can invoke the :code:`build` function with the :code:`fab` command-line utility::

  fab build
  {'stylesheets': {'assets': [<blot.assets.base.ContentAsset object at 0x7fc3d9041c50>]}}

  Done.

We can see that the context now contains a :code:`stylesheets` key that maps to the context for that content type. Within that context is an :code:`assets` key that contains the actual processed content assets.

If we change the print statement to :code:`print context['stylesheets']['assets'][0].metadata` we can get a closer look at the asset itself and evidence of :py:class:`blot.assets.PathMetadata <blot.assets.metadata.PathMetadata>` processor at work::

  fab build
  {'ancestry': '', 'parent': 'theme', 'extension': '.css', 'basename': 'style.css', 'dirname': 'theme', 'filename': 'style'}

  Done.

For more information on loaders, readers and asset processors visit the :doc:`Reading Content </guide/reading_content>` section of the User Guide.

Writing
-------

Writing involves taking some assets and passing them to a writer. In our case we don't need to render anything so we can use the :py:class:`blot.writers.StaticWriter <blot.writers.staticwriter.StaticWriter>` to simply write our stylesheet asset contents to disk::

  def build():
      context = blot.read(base_context, content_types)

      stylesheets = context['stylesheets']['assets']
      blot.write(context, [
          blot.writers.StaticWriter(stylesheets, 'static/{basename}'),
      ])


First, we grab the stylesheet assets out of the context. Then we call :py:meth:`blot.write` while passing it the :code:`context` and a list of writers. In this case, the only writer involved.

:py:class:`blot.writers.StaticWriter <blot.writers.staticwriter.StaticWriter>` takes two arguments:

    - The assets to write
    - A path pattern describing destinations

As :code:`StaticWriter` goes to write each asset it will determine where to write it by interpolating the asset's metadata into the provided path pattern. The path pattern we're using :code:`static/{basename}` requires that the assets being written contain this metadata property. Luckily, :code:`basename`, among others, is provided by the :code:`PathMetadata` asset processor we used during reading. For our :code:`style.css` file, we should expect its destination path to be :code:`static/style.css`.


If we invoke the :code:`build` function from the commandline that is exactly what we should see in the newly created :code:`output` directory::

  $ fab build

  Done.

  $ tree output
  output
  `-- static
      `-- style.css

  1 directory, 1 file


For more information on writing visit the :doc:`Writing Assets </guide/writing_assets>` section of the User Guide.


Intermission
------------

By now you should be developing a clearer idea of how you can bring together loaders, readers, processors and writers to form a pipeline for your content sources with Blot. The process for handling the rest of our content types works just like it does for our stylesheets. Really!

At this point the tutorial will start moving a lot faster.

Before moving on, let's add small helper function to :code:`fabfile.py` to clean our output directory by deleting it. The whole script should appear as follows::

  from fabric.api import local

  import blot

  base_context = {}

  content_types = {
      'stylesheets': {
          'loader': blot.loaders.BasicLoader('theme', extensions=['css']),
          'reader': blot.readers.StaticReader(),
          'processors': [
              blot.assets.PathMetadata(),
          ],
      }
  }


  def clean():
      local("rm -r output")

  def build():
      clean()
      context = blot.read(base_context, content_types)
      stylesheets = context['stylesheets']['assets']
      blot.write(context, [
          blot.writers.StaticWriter(stylesheets, 'static/{basename}'),
      ])

We've added a :code:`clean` function which removes the output directory which allows us to invoke it from the commandline. It uses a function from the Fabric api, :code:`local`, which we've imported at the top. It makes running local shell commands very convienent. As a final note, we're calling :code:`clean` first thing from :code:`build` which gives a clean target path each time you build.


Introducing Posts
-----------------

To introduce our actual blog posts, we'll add a new :code:`posts` content type::

  content_types = {
      'stylesheets': {
          'loader': blot.loaders.BasicLoader('theme', extensions=['css']),
          'reader': blot.readers.StaticReader(),
          'processors': [
              blot.assets.PathMetadata(),
          ],
      },
      'posts': {
          'loader': blot.loaders.BasicLoader('posts', extensions=['md']),
          'reader': blot.readers.MarkdownReader(),
          'processors': [
              blot.assets.PathMetadata(),
          ],
      }
  }

This is very similar to the stylesheets content type definition, but with a few changes. First, we want to load files from the :code:`posts` directory this time and only files with a :code:`.md` file extension. Any such files will then be parsed as markdown by the :py:class:`blot.readers.MarkdownReader <blot.readers.markdownreader.MarkdownReader>`.



