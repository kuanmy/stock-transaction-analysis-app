from datetime import datetime
from typing import List, Optional
import pandas as pd


class TransactionAnalyser:
    """ Process and analyse transaction data. """

    def __init__(self, data: pd.DataFrame):
        """ Constructor.

        Parameters
        ----------
        data: Input dataframe data to be analysed. Expected columns: 
            Date, Name Of Client, Code, Counter, Quantity, Net Amount, 
            Price
        """
        
        self.data = data
        self._clean_data()
        # Initialize filtered data as copy of data
        self.filtered = self.data.copy()
        self.compute_result()

    def _clean_data(self):
        """ Clean data by removing rows with empty values. """
        self.data = self.data.dropna(how="any")

    def compute_result(self):
        """ Compute result of analysis based on filtered data.
        Output columns: Code, Name of Client, Counter, Quantity, Loss/Profit, 
            Average Cost
        Compute sum of quantity (Quantity), sum of net amount (Loss/Profit),
            and Net Amount / Quantity (Average Cost) grouped by Code, Name
            of Client and Counter
        """
        # Compute results
        result = self.filtered.groupby([
                'Code', 'Name Of Client', 'Counter'
            ]).agg({
                'Quantity': 'sum',
                'Net Amount': 'sum',
            }).assign(
                Average = lambda d: d['Net Amount'] / d['Quantity']
            )
        # Rename columns
        result.columns = ['Quantity', 'Loss/Profit', 'Average Cost']
        # Format decimal data
        result = result.style.format({
            "Quantity": "{:,.0f}",
            "Loss/Profit": "{:,.2f}",
            "Average Cost": "{:,.5f}"
        })
        self.result = result

    def filter_data(self, filter_from: Optional[str], filter_to: Optional[str], filter_client_codes: List[str], filter_counters: List[str]):
        """ Filter data based on Date (from and to), Code and Counter. """
        conditions = []
        if filter_from:
            filter_from = datetime.strptime(filter_from, "%Y-%m-%d").date()
            conditions.append(self.data['Date'] >= filter_from)
        if filter_to:
            filter_to = datetime.strptime(filter_from, "%Y-%m-%d").date()
            conditions.append(self.data['Date'] <= filter_to)
        if filter_client_codes:
            conditions.append(self.data['Code'].isin(filter_client_codes))
        if filter_counters:
            conditions.append(self.data['Counter'].isin(filter_counters))
        
        filtered = self.data.copy()
        for condition in conditions:
            filtered = filtered[condition]
        self.filtered = filtered

    def get_client_code_options(self) -> List[str]:
        """ Get unique client code options (sorted alphabetically). """
        return sorted(self.data['Code'].unique())
      
    def get_counter_options(self) -> List[str]:
        return sorted(self.data['Counter'].unique())

    def get_filtered(self) -> pd.DataFrame:
        return self.filtered
      
    def get_result(self) -> pd.DataFrame:
        return self.result