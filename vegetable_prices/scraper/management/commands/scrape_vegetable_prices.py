from django.core.management.base import BaseCommand
from scraper.models import VegetablePrice
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Scrapes the vegetable prices from the website and stores them in the database'

    def handle(self, *args, **kwargs):

        # Clear existing data
        VegetablePrice.objects.all().delete()
        
        url = 'https://kalimatimarket.gov.np/'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')

            if table:
                rows = table.find_all('tr')[1:]  # Skip the header row
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 4:  # Assuming the first 3 columns are name, minimum price, maximum price, and average price.
                        name = cols[0].text.strip()
                        min_price = cols[1].text.strip()
                        max_price = cols[2].text.strip()
                        avg_price = cols[3].text.strip()
                        VegetablePrice.objects.create(name=name, min_price=min_price, max_price=max_price, avg_price=avg_price)
                self.stdout.write(self.style.SUCCESS('Successfully scraped and saved the data'))
            else:
                self.stdout.write(self.style.ERROR('Table not found on the page'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to retrieve the page, status code: {response.status_code}'))
