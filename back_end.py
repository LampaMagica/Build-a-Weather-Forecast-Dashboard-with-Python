import requests
import pandas as pd

# ADD API HERE
api = ''

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
    
    # Check if the input 'kind' is 'Weather'
    elif str(kind) == 'Weather':
        # Convert the input data to a Pandas DataFrame
        data = pd.DataFrame(data)
        
        # Initialize an empty list to store processed weather data
        data_weather = []

        # Check if the 'weather' key exists in the DataFrame
        if 'weather' in data:
            # Loop through each entry in the 'weather' column
            for i in range(len(data['weather'])):
                # Extract relevant information from the 'weather' column
                full_data = data.loc[i, 'weather'][0]
                icon = full_data.get('icon')

                # Create a dictionary containing the icon URL and timestamp
                _ = {
                    'icon': f'http://openweathermap.org/img/w/{icon}.png',
                    'time': f'{data.loc[i, "dt_txt"]}'
                }

                # Append the dictionary to the 'data_weather' list
                data_weather.append(_)
        else:
            # Print a message if the 'weather' key is not found in the data
            print("'Weather' key not found in data")

        # Return the processed weather data
        return data_weather