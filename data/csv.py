import pandas as pd


def read(filename):
    """
    Read CSV file.
    """

    return pd.read_csv(filename)


def write(dataframe, filename):
    """
    Save CSV.
    """

    dataframe.to_csv(
        filename,
        index=False
    )