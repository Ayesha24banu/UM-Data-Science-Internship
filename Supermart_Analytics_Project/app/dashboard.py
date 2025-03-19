import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data = pd.read_csv('data/cleaned_supermart_data.csv')

st.title("Supermart Sales Dashboard")
st.write("### Cleaned Data Preview")
st.dataframe(data.head())

st.write("### Sales Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data['Sales'], bins=30, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

st.write("### Sales by Category")
fig2, ax2 = plt.subplots(figsize=(10, 6))
# Get the counts per category
category_counts = data['Category'].value_counts()

# Plot with hue set to the same as x and remove the legend.
sns.barplot(x=category_counts.index, 
            y=category_counts.values, 
            palette='viridis', 
            ax=ax2,
            hue=category_counts.index,
            dodge=False)
# Remove the legend as it's not needed
if ax2.get_legend() is not None:
    ax2.get_legend().remove()

st.pyplot(fig2)

# Yearly Sales Trend (Line Plot)
st.write("### Yearly Sales Trend")
fig3, ax3 = plt.subplots(figsize=(10, 6))
# Group the data by Order_Year and sum up the Sales
yearly_sales = data.groupby('Order_Year')['Sales'].sum().reset_index()
sns.lineplot(x='Order_Year', y='Sales', data=yearly_sales, marker='o', color='coral', ax=ax3)
ax3.set_title('Yearly Sales Trend')
ax3.set_xlabel('Year')
ax3.set_ylabel('Total Sales')
st.pyplot(fig3)