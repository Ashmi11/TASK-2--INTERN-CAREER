import pandas as pd
import matplotlib.pyplot as plt

def process_dataset(file_path):
    df = pd.read_csv(file_path)

    # Calculate summary statistics for the value column
    mean_value = df['value'].mean()
    median_value = df['value'].median()
    std_dev = df['value'].std()

    # Filter the data based on number stored in value
    filtered_data = df[df['value'] > 500]

    # Generate a histogram of value scores
    plt.hist(df['value'], bins=10)
    plt.xlabel('Value Scores')
    plt.ylabel('Number of Data Points')
    plt.title('Histogram of the column: value')
    plt.show()

    # Generate a bar chart
    category_counts = df['category.code'].value_counts()
    plt.bar(category_counts.index, category_counts.values)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Bar Chart of Categories')
    plt.xticks(rotation=90)
    plt.show()

    # Save the processed data to a new CSV file
    filtered_data.to_csv('filtered_data.csv', index=False)

    # Print the summary statistics
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_dev}")

# Example usage
file_path = r"C:\Users\ashmita\Desktop\Product_v5.csv"
process_dataset(file_path)

