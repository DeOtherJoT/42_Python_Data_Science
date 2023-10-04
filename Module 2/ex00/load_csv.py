import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Loads a csv specified by <path> to a DataFrame object'''

    try:
        assert (isinstance(path, str)), "Argument must be a string."
        dt = pd.read_csv(path, index_col='country')
        print(f"Loading dataset of dimensions {dt.shape}")
        return (dt)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
