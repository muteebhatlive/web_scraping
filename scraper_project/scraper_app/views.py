from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


# Create your views here.
@api_view(['POST'])
def scrape_website(request):
    print('started')
    url = request.data.get('url')
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        scraped_data = str(soup)  # Customize this to extract specific data
        # If you want to save data to the database, create a model instance and save it here
        return Response({'data': scraped_data})
    except Exception as e:
        return Response({'error': str(e)}, status=400)