import allkitpy
import pandas as pd
import tempfile
import os


def test_csv():

    tmp = tempfile.gettempdir()

    filename = os.path.join(
        tmp,
        "sample.csv"
    )

    df = pd.DataFrame(
        {
            "a": [1, 2]
        }
    )

    allkitpy.data.csv.write(
        df,
        filename
    )

    loaded = allkitpy.data.csv.read(
        filename
    )

    assert len(loaded) == 2