from django.shortcuts import render
import requests
import datetime
import json

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'vanderbijlpark'
    
    # Weather API
    WEATHER_API_KEY = 'e10509d95010984ff189ac3856c334cd'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    PARAMS = {'units': 'metric'}
    
    # Google Custom Search API (for background images)
    GOOGLE_API_KEY = 'AIzaSyAkVaxxk6cZtlX0P7jEcCI3uZ3nnlsVpfw'
    SEARCH_ENGINE_ID = 'b775acf1f7ef84088'
    query = city + " city 1920x1080"
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}&searchType=image"
    
    image_url = None
    
    try:
        # Get city image
        search_response = requests.get(search_url)
        if search_response.status_code == 200:
            search_data = search_response.json()
            if 'items' in search_data and len(search_data['items']) > 0:
                image_url = search_data['items'][0]['link']
        
        # Get weather data
        weather_response = requests.get(weather_url, params=PARAMS)
        weather_data = weather_response.json()
        
        if weather_response.status_code == 200:
            description = weather_data['weather'][0]['description']
            icon = weather_data['weather'][0]['icon']
            temp = weather_data['main']['temp']
            day = datetime.date.today()
            
            return render(request, 'weatherapp/index.html', {
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'city': city,
                'image_url': image_url,
                'exception_occurred': False
            })
        else:
            return render(request, 'weatherapp/index.html', {
                'error': 'City not found. Please enter a valid city.',
                'exception_occurred': True
            })
    except requests.exceptions.RequestException as e:
        return render(request, 'weatherapp/index.html', {
            'error': f'Network error: {str(e)}. Please try again later.',
            'exception_occurred': True
        })
    except Exception as e:
        return render(request, 'weatherapp/index.html', {
            'error': f'An unexpected error occurred: {str(e)}',
            'exception_occurred': True
        })