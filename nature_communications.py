#!/usr/bin/env python
from __future__ import print_function
import requests
import re
from bs4 import BeautifulSoup
import auth

def getArticleStatus():
    home_url = 'https://www.nature.com/ncomms/'
    domain = 'http://mts-ncomms.nature.com/'
    login_url = domain + 'cgi-bin/main.plex'
    payload = {'form_type': 'login_results',
               'j_id': '18',
               'ms_id_key': '',
               'login': auth.getNatureUsername(),
               'password': auth.getNaturePassword(),
               'submit_login': 'Login'}
    with requests.Session() as session:
        print('get ' + home_url)
        res = session.get(home_url)
        print('get ' + login_url)
        res = session.get(login_url)
        soup = BeautifulSoup(res.content, "lxml")
        payload['ms_id_key'] = soup.find('input', {'id': 'ms_id_key'}).get('value')
        res = session.post(login_url, data=payload)
        print('login')
        soup = BeautifulSoup(res.content, "lxml")
        ms_url = soup.find('span', {'class': 'BODY'}).find('a').get('href')
        print('get ' + domain + ms_url)
        res = session.get(domain + ms_url)
        soup = BeautifulSoup(res.content, "lxml")
        for link in soup.find_all('a'):
            if 'Live Manuscripts' in link.text:
                ms_url = link.get('href')
                break
        print('get ' + domain + ms_url)
        res = session.get(domain + ms_url)
        soup = BeautifulSoup(res.content, "lxml")
        print(soup.find('table', {'border', '"5"'}))

if __name__ == '__main__':
    getArticleStatus()
