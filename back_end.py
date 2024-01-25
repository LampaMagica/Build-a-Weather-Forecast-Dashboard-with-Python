import requests
import pandas as pd

# Add API KEY
api = '2243213ada6eb4f2f91c966d964e9c10'

def get_data(location, days=1, kind=None):



    # Build the API request URL using the provided location and API key
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api}'
    
    # Make a GET request to the OpenWeatherMap API
    request = requests.get(url)
    
    # Parse the JSON response into a Python dictionary
    data = request.json()
    
    # Extract the 'list' attribute from the dictionary and limit the data to the specified number of days
    data = data['list'][:8 * days]
    
    if str(kind) == 'Temperature':
        # Flatten the nested structures in the DataFrame using json_normalize
        data_json = pd.json_normalize(data)
        
        # Extract specific columns from the flattened DataFrame (temperature and date/time)
        temperature = data_json['main.temp'] / 10  # Divide by 10 
        date_time = data_json['dt_txt']
        
        # Return a tuple containing the temperature and date/time data
        return temperature, date_time
    
    elif str(kind) == 'Weather':
        data = pd.DataFrame(data)
        data_weather = []
        if 'weather' in data:
            for i in range(len(data['weather'])):
                full_data = data.loc[i,'weather'][0]
                icon = full_data.get('icon')
                _ = {
                    'icon' : f'http://openweathermap.org/img/w/{icon}.png',
                    'time' : f'{data.loc[i,"dt_txt"]}'
                }
                data_weather.append(_)
        else:
            print("'Weather' key not found in data")
        return data_weather