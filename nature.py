#!/usr/bin/env python
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import auth

def getArticleStatus():
    payload = {'form_type': 'login_results',
               'j_id': '10',
               'ms_id_key': '',
               'login': auth.getNatureUsername(),
               'password': auth.getNaturePassword(),
               'submit_login': 'Login'}
    with requests.Session() as session:
        res = session.get('http://mts-nature.nature.com/cgi-bin/main.plex')
        soup = BeautifulSoup(res.content, "lxml")
        payload['ms_id_key'] = soup.find('input', {'id': 'ms_id_key'}).get('value')
        res = session.post('http://mts-nature.nature.com/cgi-bin/main.plex', data=payload)
        soup = BeautifulSoup(res.content, "lxml")
        print(soup.find('span', {'class': 'TITLE'}).text)

if __name__ == '__main__':
    getArticleStatus()
