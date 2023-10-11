from functools import wraps
from .utils import show_results, record_stats


class profile:
    """
    A profiling decorator and context manager. It uses cProfile to profile the 
    execution of Python code and uses snakeviz to visualize the results in a 
    developer-friendly way.
    """
    def __init__(
            self, 
            output_dir=None,
            open_flamechart=True,
            print_stats=False,
            verbose=False) -> None:
        self.output_dir = output_dir
        self.temp_dir = None
        self.profile_file = None
        self.profiler = None
        self.open_flamechart = open_flamechart
        self.print_stats = print_stats
        self.verbose = verbose

    def __call__(self, func):
        @wraps(func)
        def profiled_func(*args, **kwargs):
            self.profiler = record_stats()
            result = func(*args, **kwargs)
            self._dump_stats_and_analyze()
            return result

        return profiled_func

    def __enter__(self):
        self.profiler = record_stats()

    def __exit__(self, exc_type, exc_value, traceback):
        self._dump_stats_and_analyze()

    def _dump_stats_and_analyze(self):
        print(f'\nNew profiling result')
        if not self.max_profile_limit_reached:
            print(f'Run "python -m snakeviz {self.profile_file}" to re-render '
                  'the flame chart.')

            self.profiler.disable()
            self.profiler.dump_stats(self.profile_file)

            show_results(
                profile_file=self.profile_file,
                open_flamechart=self.open_flamechart,
                print_stats=self.print_stats,
                verbose=self.verbose
            )
        print('\n')