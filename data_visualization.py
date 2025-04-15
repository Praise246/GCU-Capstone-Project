import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    """Generates basic visualizations for numerical and categorical data."""
    # Set plot style
    sns.set(style="whitegrid")

    # Plot missing values heatmap
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Values Heatmap")
    plt.savefig("missing_values_heatmap.png")
    print("Missing Values Heatmap saved as missing_values_heatmap.png")

    # Plot distributions of numerical columns
    num_cols = df.select_dtypes(include=['number']).columns
    if len(num_cols) > 0:
        df[num_cols].hist(figsize=(12, 8), bins=20)
        plt.suptitle("Numerical Features Distribution")
        plt.savefig("numerical_distribution.png")
        print("Numerical Features Distribution saved as numerical_distribution.png")

    # Plot correlation heatmap
    if len(num_cols) > 1:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.savefig("correlation_heatmap.png")
        print("Correlation Heatmap saved as correlation_heatmap.png")
