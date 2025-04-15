class DataCleaner:
    def __init__(self, df):
        self.df = df

    def handle_missing_values(self, strategy='mean'):
        """Handle missing values using specified strategy."""
        if strategy == 'mean':
            return self.df.fillna(self.df.mean())
        elif strategy == 'drop':
            return self.df.dropna()
        return self.df

    def remove_duplicates(self):
        """Remove duplicate rows from the dataframe."""
        return self.df.drop_duplicates()
