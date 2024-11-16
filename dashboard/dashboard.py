# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("Bike Sharing Analysis Dashboard")

# Mendapatkan path absolut dari file dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
day_csv_path = os.path.join(base_dir, "day.csv")
hour_csv_path = os.path.join(base_dir, "hour.csv")

# Membaca dataset
day_data = pd.read_csv(day_csv_path)
hour_data = pd.read_csv(hour_csv_path)

day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

st.sidebar.header("Select Analysis")
analysis_type = st.sidebar.selectbox(
    "Choose the analysis type:",
    ["Overview", "Monthly and Weekly Patterns", "Hourly Patterns"]
)

if analysis_type == "Overview":
    st.header("Dataset Overview")
    st.write("### Day Dataset Sample")
    st.dataframe(day_data.head())
    st.write("### Hour Dataset Sample")
    st.dataframe(hour_data.head())
    st.write("### Key Statistics")
    st.write(day_data.describe())

# Monthly and Weekly Patterns Section
elif analysis_type == "Monthly and Weekly Patterns":
    st.header("Monthly and Weekly Patterns")

    # Monthly Rentals
    st.subheader("Total Rentals by Month")
    monthly_rentals = day_data.groupby('mnth')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='mnth', y='cnt', data=monthly_rentals, ax=ax)
    ax.set_title('Total Rentals by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Rentals')
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.pyplot(fig)

    # Weekly Rentals
    st.subheader("Average Rentals by Day of the Week")
    weekly_rentals = day_data.groupby('weekday')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='weekday', y='cnt', data=weekly_rentals, ax=ax)
    ax.set_title('Average Rentals by Day of the Week')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Average Rentals')
    ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    st.pyplot(fig)

# Hourly Patterns Section
elif analysis_type == "Hourly Patterns":
    st.header("Hourly Patterns")

    # Hourly Rentals
    st.subheader("Average Rentals by Hour")
    hourly_rentals = hour_data.groupby('hr')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', data=hourly_rentals, marker='o', ax=ax)
    ax.set_title('Average Rentals by Hour')
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Average Rentals')
    st.pyplot(fig)

    # Time of Day Rentals
    st.subheader("Average Rentals by Time of Day")
    hour_data['time_of_day'] = hour_data['hr'].apply(
        lambda x: 'Morning' if 5 <= x < 12 else
                  'Afternoon' if 12 <= x < 17 else
                  'Evening' if 17 <= x < 21 else 'Night'
    )
    time_of_day_rentals = hour_data.groupby('time_of_day')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='time_of_day', y='cnt', data=time_of_day_rentals, order=['Morning', 'Afternoon', 'Evening', 'Night'], ax=ax)
    ax.set_title('Average Rentals by Time of Day')
    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Average Rentals')
    st.pyplot(fig)

# Footer
st.write("### Developed by: Bernadetta Sri Endah")

