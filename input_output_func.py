import pandas as pd

def read_input_file(filename: str) -> pd.DataFrame:
    return pd.read_excel(
        filename, 
        header=[1], 
        usecols=['Date', 'Name Of Client', 'Code', 'Counter', 'Quantity', 'Net Amount'],
    )
