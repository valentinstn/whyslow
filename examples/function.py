import pandas as pd
from whyslow import profile


# As decorator
@profile()
def slow_function():
    df = pd.DataFrame()
    for i in range(10000):
        df = df * 2

slow_function()

# As context manager
def slow_function():
    with profile():
        df = pd.DataFrame()
        for i in range(10000):
            df = df * 2

slow_function()


