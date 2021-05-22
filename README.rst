funchain - chaining of functional
=====================================

Functional processing for Python without the hassle of variable handling.

Maybe the least overloaded implementation.

Why do I need it?
---------------------

You rely heavily on functional python, e.g. `map`, `filter`, `reduce`. 
Your code usually looks like the following

.. code-block:: python

  with os.scandir(BASE_DIR) as it:
      dirs = filter(lambda i: i.is_dir(follow_symlinks=False), it)
      valid_dirs = filter(is_valid_dir, dirs)
      tasks_packages = map(PackageKind.from_dir_entry, valid_dirs)
      valid_only = filter(lambda i: i[1] != PackageKind.NOTHING, tasks_packages)
      task_files = itertools.chain.from_iterable(map(get_task_files, valid_only))
      tasks = [to_package_names(e) for e in task_files]

So you have the mess with the intermediate variables. It becomes worse
if you need to add a step somewhere in between.

Now consider the `funchain` variant of the same logic

.. code-block:: python

  with os.scandir(BASE_DIR) as it:
      task_files = Chain(it)\
         .filter(lambda i: i.is_dir(follow_symlinks=False))\
         .filter(is_valid_dir)\
         .map(PackageKind.from_dir_entry)\
         .filter(lambda i: i[1] != PackageKind.NOTHING)\
         .map(get_task_files)\
         .map_by(itertools.chain.from_iterable)
      tasks = [to_package_names(e) for e in task_files]

The code is not a full representation of all available functionals, but will growth with time.

In case one wants to split the instructions into multiple lines but doesn't like the line continuation operator
at the ends, it is possible to put the chain into braces. Example

.. code:: python

  with os.scandir(BASE_DIR) as it:
      task_files = (Chain(it)
         .filter(lambda i: i.is_dir(follow_symlinks=False))
         .filter(is_valid_dir)
      )

Installation
----------------
Currently it is not a fully fledged package yet. Hence the installation goes directly from github

.. code:: bash

    pip install git+https://github.com/eugenma/funchain.git#egg=funchain
