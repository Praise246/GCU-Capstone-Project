import pandas as pd
from modules.data_loader import DataLoader  # Loads datasets
from modules.data_exploration import DataExplorer  # Performs EDA
from modules.data_quality_detection import DataQualityDetector
from modules.data_visualization import visualize_data  # Import visualization module

def main():
    # Correct file path for Windows/Linux compatibility
    file_path = "PGYR2023_P01302025_01212025/OP_DTL_OWNRSHP_PGYR2023_P01302025_01212025.csv"

    # Instantiate DataLoader and load the dataset
    data_loader = DataLoader()
    df = data_loader.load_from_file(file_path)  # Fixed incorrect usage

    # Perform Exploratory Data Analysis
    DataExplorer(df)

    # Detect Data Quality Issues
    print("\nRunning Data Quality Checks...")
    dq_detector = DataQualityDetector(df)
    quality_report = dq_detector.generate_quality_report()

    # Save Data Quality Report to CSV
    report_path = "data_quality_report.csv"
    quality_report.to_csv(report_path, index=False)
    print(f"\nData Quality Report saved at: {report_path}")

    # Generate visualizations using the module
    visualize_data(df)

if __name__ == "__main__":
    main()
