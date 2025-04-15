import pandas as pd
import requests
from io import StringIO

class DataLoader:
    def load_from_file(self, file_path):
        """Load data from a local file."""
        return pd.read_csv(file_path)

    def load_from_url(self, url):
        """Load data from a URL."""
        response = requests.get(url)
        return pd.read_csv(StringIO(response.text))
