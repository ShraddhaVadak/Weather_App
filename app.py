import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌥️")

st.title("Weather App 🌥️")

st.write("Enter the city name and click on the button to fetch weather data")

# Input box
city = st.text_input("Enter the city name")

if st.button("Fetch Weather Data"):

    if city:
        API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(API_URL)

        if response.status_code == 200:

            st.success("Weather data fetched successfully")

            # Convert API response to dictionary
            data = response.json()

            # Extract data
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            condition = data["weather"][0]["main"]
            country = data["sys"]["country"]
            name = data["name"]

            # Display city
            st.header(f"{name}, {country}")

            # Display data in columns
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            col1.metric("Temperature", f"{temperature} °C 🌡️")
            col2.metric("Humidity", f"{humidity}% 💦")
            col3.metric("Wind Speed", f"{wind_speed} m/s 🍃")
            col4.metric("Condition", f"{condition} ⛈️")

        else:
            st.error("Invalid city name or API key")

    else:
        st.warning("Please enter a city name")
