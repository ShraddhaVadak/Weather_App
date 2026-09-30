import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv(WEATHER_API_KEY)

API_KEY = 'dfb704e6473ed38a9a399e358706124d'
st.set_page_config(page_title='Weather App', page_icon="🌥️")

st.title('Weather App 🌥️')

st.write('Enter the city name and click on the button to featch weather data')
#To create input box for taking input from user
city = st.text_input('Enter the city name')

if(st.button('featch weather data')):
        
        API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(API_URL)
        if(response.status_code == 400):
                st.success('weather data featch successfully')
                #Convert api data in jsin that is in dictionary format
                data = response.json()
                #Extract the data in variable
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                condition = data['weather'][0]['main']
                country = data['sys']['country']
                name = data['name']
                #Display the data
                st.header(f'{name} , {country}')
                #To display in column format
                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)
                
                col1.metric('Temperature' ,f'{temperature}°C🌡️')
                col2.metric('Humidity' ,f'{humidity}%💦')
                col3.metric('wind_speed ',f'{wind_speed} m/s🍃')
                col4.metric('condition' , f'{condition}⛈️')
        else:
                st.error('Invalid city name')
        

