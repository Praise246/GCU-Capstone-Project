class DataExplorer:
    def __init__(self, df):
        self.df = df

    def summary(self):
        """Print summary statistics of the dataframe."""
        print(self.df.describe())

    def detect_missing_values(self):
        """Detect missing values in the dataframe."""
        print(self.df.isnull().sum())
