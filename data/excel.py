import pandas as pd


def read(filename, sheet=0):
    """
    Read Excel.
    """

    return pd.read_excel(
        filename,
        sheet_name=sheet
    )


def write(dataframe, filename):
    """
    Save Excel.
    """

    dataframe.to_excel(
        filename,
        index=False
    )