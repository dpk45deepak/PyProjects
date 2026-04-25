

# Original code
# import pandas as pd
# from pathlib import Path

# DATA_PATH = Path(__file__).resolve().parent.parent / "data"

# def load_dataset(filename="dataset.csv"):
#     file_path = DATA_PATH / filename
#     df = pd.read_csv(file_path)
#     return df




# Refactored code with better structure and path handling

import pandas as pd
from pathlib import Path

def load_dataset(filename="dataset.csv"):
    base = Path.cwd()
    data_path = base / "data" / filename
    return pd.read_csv(data_path)