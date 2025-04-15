import pandas as pd
import numpy as np

class DataQualityDetector:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        self.quality_issues = pd.DataFrame()

    def detect_missing_values(self):
        """Detects missing values and returns a summary."""
        missing_values = self.df.isnull().sum()
        missing_ratio = missing_values / len(self.df)
        missing_df = pd.DataFrame({
            'column': self.df.columns,
            'missing_count': missing_values.values,
            'missing_ratio': missing_ratio.values
        })
        missing_df = missing_df[missing_df['missing_count'] > 0]
        missing_df['issue_type'] = 'Missing Value'
        return missing_df

    def detect_duplicates(self):
        """Detects duplicate rows."""
        duplicate_rows = self.df.duplicated(keep=False)
        duplicate_df = self.df[duplicate_rows].copy()
        duplicate_df['issue_type'] = 'Duplicate'
        return duplicate_df

    def detect_schema_drift(self, reference_df):
        """Detects schema drift by comparing the dataset to a reference schema."""
        current_schema = self.df.dtypes.astype(str)
        reference_schema = reference_df.dtypes.astype(str)
        schema_drift = (current_schema != reference_schema)
        
        schema_df = pd.DataFrame({
            'column': current_schema.index,
            'current_dtype': current_schema.values,
            'expected_dtype': reference_schema.values,
            'schema_drift': schema_drift.values
        })
        schema_df = schema_df[schema_df['schema_drift']]
        schema_df['issue_type'] = 'Schema Drift'
        return schema_df

    def detect_outliers(self):
        """Detects numerical outliers using the IQR method."""
        outlier_records = []
        for column in self.df.select_dtypes(include=['number']).columns:
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
            for index in outliers.index:
                outlier_records.append({'index': index, 'column': column, 'issue_type': 'Outlier'})

        return pd.DataFrame(outlier_records)

    def detect_incorrect_mappings(self, categorical_rules):
        """Detects incorrect categorical values based on predefined rules."""
        incorrect_mappings = []
        for column, valid_values in categorical_rules.items():
            if column in self.df.columns:
                invalid_entries = self.df[~self.df[column].isin(valid_values)]
                for index in invalid_entries.index:
                    incorrect_mappings.append({'index': index, 'column': column, 'issue_type': 'Incorrect Mapping'})

        return pd.DataFrame(incorrect_mappings)

    def generate_quality_report(self, reference_df=None, categorical_rules=None):
        """Aggregates all detected quality issues into a single report."""
        missing_report = self.detect_missing_values()
        duplicate_report = self.detect_duplicates()
        outlier_report = self.detect_outliers()
        schema_report = self.detect_schema_drift(reference_df) if reference_df is not None else pd.DataFrame()
        mapping_report = self.detect_incorrect_mappings(categorical_rules) if categorical_rules else pd.DataFrame()

        # Combine all reports
        self.quality_issues = pd.concat([
            missing_report, duplicate_report, outlier_report, schema_report, mapping_report
        ], ignore_index=True)

        return self.quality_issues

# Example usage:
if __name__ == "__main__":
    df = pd.read_csv("sample_dataset.csv")  # Load any dataset
    dq_detector = DataQualityDetector(df)
    report = dq_detector.generate_quality_report()
    print(report)
