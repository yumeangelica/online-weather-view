from requests import get
from datetime import datetime
import pytz
from django.core.cache import cache
from weather.utils.get_uv_forecast import get_uv_forecast

def get_weather_forecast(owm_api_key: str, uv_api_key: str, city: str):

    cache_key = f'forecast_{city}'
    forecasts_by_day = cache.get(cache_key)

    if forecasts_by_day:
        return forecasts_by_day

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={owm_api_key}&units=metric&cnt=24'

    try:
        response = get(url).json()

        uv_forecast = get_uv_forecast(city, uv_api_key)
        forecasts_by_day = {}

        uv_index_by_date = {entry['date']: round(entry['uv']) for entry in uv_forecast}

        for item in response['list']:
            dt = datetime.fromtimestamp(item['dt'], pytz.utc)
            date_str = dt.strftime("%Y-%m-%d")
            formatted_date_str = dt.strftime("%a %d %b %Y")

            forecast = {
                'date': formatted_date_str,
                'hour': dt.strftime("%H"),
                'temperature': round(item['main']['temp']),
                'description': item['weather'][0]['description'],
                'humidity': round(item['main']['humidity']),
                'wind_speed': round(item['wind']['speed']),
                'icon': f"http://openweathermap.org/img/wn/{item['weather'][0]['icon']}@2x.png",
                'uv_index': uv_index_by_date.get(date_str, 'N/A')
            }

            if date_str not in forecasts_by_day:
                forecasts_by_day[date_str] = {
                    'formatted_date': formatted_date_str,
                    'forecasts': []
                }

            forecasts_by_day[date_str]['forecasts'].append(forecast)

        cache.set(cache_key, forecasts_by_day, timeout=3600)

        return forecasts_by_day

    except Exception as e:
        print(f"Error fetching weather forecast: {e}")
        return None
