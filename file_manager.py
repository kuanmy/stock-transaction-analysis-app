"""
Functions to manage Input/Ouput files of the Transaction Analysis Program
"""

import os
import pandas as pd

__author__ = "Kuan Meng Yi"


def read_input_file(content) -> pd.DataFrame:
    """ Read input excel content into dataframe. Expected columns: 
        Date, Name Of Client, Code, Counter, Quantity, Net Amount, Price
    """
    input = pd.read_excel(
        content,
        header=[1], 
        usecols=['Date', 'Name Of Client', 'Code', 'Counter', 'Quantity', 'Net Amount', 'Price'],
        parse_dates=[0]
    )
    input['Date'] = input['Date'].dt.date  # Cast Date column into date format
    return input


def write_output_file(output_dir: str, filename: str, result: pd.DataFrame, filtered: pd.DataFrame) -> None:
    """ Write result and filtered input into an excel file containing 
    two sheets: Result and Filtered. 
    """
    with pd.ExcelWriter(os.path.join(output_dir, filename)) as writer:  
        result.to_excel(writer, sheet_name='Result')
        filtered.to_excel(writer, sheet_name='Filtered')