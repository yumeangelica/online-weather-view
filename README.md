# 🌤️ Weather Forecast App

A Django-based web application that provides real-time weather data and a 3-day weather forecast for cities worldwide. The application integrates with the OpenWeatherMap API and Weather API to display accurate and up-to-date information.

## Features
- 🌍 **Search by City**: Enter a city name to retrieve current weather data and a detailed 3-day forecast.
- ⛅ **Current Weather**: Displays the temperature, feels-like temperature, humidity, wind speed, UV index, and cloudiness.
- 📅 **3-Day Forecast**: Shows an hourly breakdown of temperature, wind speed, humidity, and UV index for the next three days.
- 🌞 **Sunrise & Sunset Times**: Provides the local times for sunrise and sunset.
- ⚡ **UV Index**: Check the UV index for the current day and forecast days.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (with responsive design)
- **APIs**: [OpenWeatherMap API](https://openweathermap.org/api) and [Weather API](https://www.weatherapi.com/)

## Setup & Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yumeangelica/online-weather-view.git
    ```

2. Navigate to the project directory:
    ```bash
    cd online-weather-view
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Get your API keys:
   - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and [Weather API](https://www.weatherapi.com/signup.aspx) to obtain API keys.
   - Create a `.env` file:
     ```bash
     touch .env
     ```
   - Add the following content to the `.env` file:
     ```
     OWM_API_KEY=your_openweathermap_api_key
     UV_API_KEY=your_weather_api_key
     ```

5. Run database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and visit:
    ```
    http://127.0.0.1:8000
    ```

## How It Works
1. **Search**: Type the name of any city.
2. **Select an Option**: Choose between current weather or 3-day forecast.
3. **View Weather Data**: See real-time weather data or a detailed forecast.


## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. For more information, see the LICENSE file in this repository.

