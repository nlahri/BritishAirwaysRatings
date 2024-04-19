import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('British Airways Rating by Travel Class')

BA_AirlineReviews = pd.read_csv('BA_AirlineReviews.csv')

BA_AirlineReviews_filtered = BA_AirlineReviews.dropna(subset=['SeatType'])
BA_AirlineReviews_filtered = BA_AirlineReviews_filtered[BA_AirlineReviews_filtered['SeatType'] != 'NONE']

travel_classes = BA_AirlineReviews_filtered['SeatType'].unique()

selected_class = st.sidebar.selectbox('Select Travel Class', travel_classes)

filtered_data = BA_AirlineReviews_filtered[BA_AirlineReviews_filtered['SeatType'] == selected_class]

overall_rating_count = filtered_data['OverallRating'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
overall_rating_count.plot(kind='bar', color='blue')
plt.xlabel('Overall Rating')
plt.ylabel('Count')
plt.title(f'Ratings For {selected_class}')
plt.xticks(rotation=0)
st.pyplot(plt.gcf())