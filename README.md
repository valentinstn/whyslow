<h1 align="center">WhySlow?</h1>
<p align="center">
    <em>Developer-friendly performance profiling utilities for Python</em>
</p>

`WhySlow` simplifies the usage of [`cProfile`](https://docs.python.org/3/library/profile.html) and [`snakeviz`](https://github.com/jiffyclub/snakeviz). It offers the fastes way to get from slow code to flame chart and start the performance optimization adventure.

<p align="center">
    <img src="flamechart.png">
</p>



## Installation

```
pip install whyslow
```

## Usage

There are three ways to use this profiler.

### As decorator to profile a function call

```py
from whyslow import profile

@profile
def my_slow_function():
    # do expensive operations
```

### As context manager to profile any code

```py
from whyslow import profile

with profile():
    # some expensive operations
```

### As module to profile a script

```sh
$ python -m whyslow my-slow-script.py
```

## License

MIT License