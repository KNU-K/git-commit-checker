from bs4 import BeautifulSoup
from urllib.request import urlopen

class Crawler:
    @staticmethod
    def run(user,timestamp):
        with urlopen('https://github.com/'+user) as response:
            soup = BeautifulSoup(response, 'html.parser')
            for e in soup.find_all('td',class_='ContributionCalendar-day'):
                if e['data-date'] == timestamp:
                    return e.get_text().split(' ')[0]
            
            
