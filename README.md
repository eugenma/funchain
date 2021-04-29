# funchain - chaining of functional

Functional processing for Python without the hassle of variable handling.

It's not the nicest implementation, but one of the least overbloated.
  
See the example just for comparison. (The real meaning is not important)

In plain Python

    with os.scandir(BASE_DIR) as it:
       dirs = filter(lambda i: i.is_dir(follow_symlinks=False), it)
       valid_dirs = filter(is_valid_dir, dirs)
       tasks_packages = map(PackageKind.from_dir_entry, valid_dirs)
       valid_only = filter(lambda i: i[1] != PackageKind.NOTHING, tasks_packages)
       task_files = itertools.chain.from_iterable(map(get_task_files, valid_only))
       tasks = [to_package_names(e) for e in task_files]

One an observe the mess with the intermediate variables.

Now the `pipefun` variant

    with os.scandir(BASE_DIR) as it:
      task_files = Chain(it)\
         .filter(lambda i: i.is_dir(follow_symlinks=False))\
         .filter(is_valid_dir)\
         .map(PackageKind.from_dir_entry)\
         .filter(lambda i: i[1] != PackageKind.NOTHING)\
         .map(get_task_files)\
         .map_by(itertools.chain.from_iterable)
     tasks_2 = [to_package_names(e) for e in task_files]


The code is not a fully representation of all available functionals, but will growth with time.

