import sys 
import os
from subprocess import call
from tempfile import mkdtemp
from .utils import show_results

if len(sys.argv) != 2:
    raise AssertionError('No file name provided to be executed')

temp_dir = mkdtemp()
profile_file = f"{temp_dir}/profile.prof"
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