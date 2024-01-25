import requests
import pandas as pd

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
    
    if kind != None:
    # Flatten the nested structures in the DataFrame using json_normalize
    data_json = pd.json_normalize(data)
    
    # Extract specific columns from the flattened DataFrame (temperature and date/time)
    temperature = data_json['main.temp'] / 10  # Divide by 10 
    date_time = data_json['dt_txt']
    
    # Return a tuple containing the temperature and date/time data
    return temperature, date_time


if __name__ == '__main__':
    data = get_data('Marrakesh')
    data_0 = data.get('list')[0]

    data_with_date = get_data(location='Marrakesh',days=3)



    print(len(data.get('list')))
    print(data_0.get('dt_txt'))


# data = pd.DataFrame(data)

# temp = [20,23,18,18,14]
# days = [1,2,3,4,5]

# Create DataFrame using pd.DataFrame constructor
# data_tralala = pd.DataFrame(data=tralala, columns=col_)

# Plot using Plotly Express
# pdt = px.line(x=days, y=temp, labels={'x': 'Days', 'y': 'Temp'})

# st.plotly_chart(pdt)