PURPOSE:

The purpose of this script is to process a dataset stored in a CSV file, 
calculate summary statistics on a specific column, filter data based on a criteria, 
generate a histogram and bar chart from the dataset, save the filtered data to a new CSV file, 
and print the summary statistics.

We read the dataset using pd.read_csv(), and save it in the variable df.
We calculate the mean, median, and standard deviation of the 'value' column using the corresponding 
pandas functions.
We generate a histogram using plt.hist() with the filtered 'value' values as the input.
We generate a bar chart using plt.bar() with the counts of each category as the input.
We save the filtered data to a new csv file named 'filtered_products.csv' using filtered_df.to_csv().
The script is encapsulated inside a function called process_dataset which takes the file path as an 
input parameter. This allows you to run the script multiple times with different datasets by simply 
calling the process_dataset function with the appropriate file path.


How to Run the Script:

1)Open a Python environment or IDE of your choice.

2)Install the dependencies by running the following commands in your terminal or command prompt:
pip install pandas
pip install matplotlib

3)Copy the script code provided to a Python file (e.g., data_processing.py).

4)Specify the file path of the dataset you want to process by assigning the variable file_path with the correct file path. For example:
file_path = r"C:\Users\ashmita\Desktop\Product_v5.csv"

5)Execute the script by running the Python file.


Dependencies:

pandas: A powerful data manipulation library that allows easy handling of data structures.

matplotlib: A data visualization library used to generate histograms and bar charts.

Make sure to install these dependencies before running the script.


