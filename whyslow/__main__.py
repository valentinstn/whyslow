import sys 
import os
from subprocess import call
from .utils import show_results, get_profile_file_path

if len(sys.argv) != 2:
    raise AssertionError('No file name provided to be executed')

profile_file = get_profile_file_path()
call([sys.executable, '-m', 'cProfile', '-o', profile_file, *sys.argv[1:]])

if os.path.exists(profile_file):
    show_results(
        profile_file=profile_file,
        open_flamechart=True,
        print_stats=False,
        verbose=False
    )
else:
    raise AssertionError('No profiling results')