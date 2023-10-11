import os
import sys
import subprocess
import pstats
from tempfile import mkdtemp
from cProfile import Profile

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROCESS_KILLER_PATH = os.path.join(BASE_DIR, 'process_killer.py')


def record_stats() -> Profile:
    profiler = Profile()
    profiler.enable()
    return profiler


def show_results(
        profile_file: str, 
        open_flamechart: bool, 
        print_stats: bool,
        verbose: bool) -> None:
    """Shows the profiling results, either as flamechart, and/or as text output"""
    if open_flamechart:
        print('Opening flamechart now.')
        # Start snakeviz to show the results
        process = subprocess.Popen(
            [sys.executable, '-m', 'snakeviz', profile_file], 
            stdout=None if verbose else subprocess.DEVNULL
        )

        # Shutdown snakeviz process after the browser had time to open the results
        subprocess.Popen(
            [sys.executable, PROCESS_KILLER_PATH, str(process.pid)]
        )
        
    # Print the profiling statistics
    if print_stats:
        stats = pstats.Stats(profile_file)
        stats.print_stats()


def get_profile_file_path() -> str:
    """Creates a temporary directory and returns the file for the profiling results"""
    temp_dir = mkdtemp()
    profile_file = f"{temp_dir}/profile.prof"
    return profile_file