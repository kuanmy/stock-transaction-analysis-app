import pandas as pd
import datetime

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.dropna(how="any")

def filter_data(data: pd.DataFrame, filters: dict) -> pd.DataFrame:
    conditions = []
    if filters.get('filter_from'):
        conditions.append(data['Date'] >= filters.get('filter_from'))
    if filters.get('filter_to'):
        conditions.append(data['Date'] <= filters.get('filter_to'))
    if filters.get('filter_client_codes'):
        conditions.append(data['Code'].str.upper().isin(filters.get('filter_client_codes')))
    if filters.get('filter_counters'):
        conditions.append(data['Counter'].str.upper().isin(filters.get('filter_counters')))
    
    for condition in conditions:
        data = data[condition]
    
    return data

def compute_results(data: pd.DataFrame) -> pd.DataFrame:
    result = data.groupby([
            'Code', 'Name Of Client', 'Counter'
        ]).agg({
            'Quantity': 'sum',
            'Net Amount': 'sum',
        }).assign(
            Average = lambda d: d['Net Amount'] / d['Quantity']
        )
    result.columns = ['Quantity', 'Loss/Profit', 'Average Cost']
    return result

def prepare_filters_string(filter_from: str, filter_to: str, filter_client_codes: str, filter_counters: str) -> dict:
    if (filter_from and not validate_date(filter_from)) or \
        (filter_to and not validate_date(filter_to)):
        raise ValueError('Invalid date format')
    
    return {
        'filter_from': filter_from,
        'filter_to': filter_to,
        'filter_client_codes': [s.strip().upper() for s in filter_client_codes.split(";")],
        'filter_counters': [s.strip().upper() for s in filter_counters.split(";")]
    }

def validate_date(date_string: str) -> bool:
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False