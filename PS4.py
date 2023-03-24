Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import matplotlib.pyplot as plt
... 
... # Read in the Excel file
... Updated = pd.read_excel("C:/Users/User/Desktop/Updated.xlsx")
... 
... # View the dataframe
... print(Updated.head())
... 
... # Print the column names
... print(Updated.columns)
... 
... # Create a bar plot of maximum temperature by state using ggplot2 syntax
... plt.figure(figsize=(10,6))
... plt.bar(Updated["State"], Updated["Max temp"], color="blue")
... plt.xlabel("State")
... plt.ylabel("Max temp")
... plt.title("Maximum Temperature by State")
... plt.xticks(rotation=90, ha="right")
... plt.show()
