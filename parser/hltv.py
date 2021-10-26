import requests
from bs4 import BeautifulSoup

base_url = 'http://www.hltv.org'

url = 'https://www.hltv.org/events/6207/pgl-major-stockholm-2021-challengers-stage'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


teams = soup.find('div', class_='teams-attending grid').find_all('div', class_='standard-box team-box supports-hover')


for team in teams:
    name = team.find('div', class_='text').text
    t_url = base_url + team.find('a').get('href')
    rank = team.find('div', class_='event-world-rank').text
    players = team.find_all('div', class_='flag-align player')

    print(f"Team: {name}; Rank: {rank}; url: {t_url}.")

    for player in players:
        profile = player.find('a')
        nickname = profile.text
        p_url = base_url + profile.get('href')
        country = player.find('img').get('alt')
        print(f'---> nickname: {nickname}; country: {country}; url: {p_url}')
