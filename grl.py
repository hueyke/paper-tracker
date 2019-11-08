#!/usr/bin/env python
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import auth
import re

def getName():
    return 'GRL'

def getArticleStatus():
    domain = 'https://grl-submit.agu.org/'
    main_link = 'https://grl-submit.agu.org/cgi-bin/main.plex'
    payload = {'form_type': 'login_results',
               'j_id': '279',
               'ms_id_key': '',
               'login': auth.getGRLUsername(),
               'password': auth.getGRLPassword(),
               'submit_login': 'Login'}
    try:
        with requests.Session() as session:
            res = session.get(main_link)
            soup = BeautifulSoup(res.content, "html.parser")
            payload['ms_id_key'] = soup.find('input', {'id': 'ms_id_key'}).get('value')
            res = session.post(main_link, data=payload)
            soup = BeautifulSoup(res.content, "html.parser")
            links = soup.find_all('a')
            manuscript_link = ''
            for link in links:
                if 'Manuscripts (1)' in link.text:
                    manuscript_link = link.attrs['href']
                    break
            res = session.get(domain + manuscript_link)
            soup = BeautifulSoup(res.content, "html.parser")
            links = soup.find_all('a')
            manuscript_link = ''
            for link in links:
                if 'Check Status' in link.text:
                    manuscript_link = link.attrs['href']
                    break
            if manuscript_link == '':
                raise Exception('RR')
            res = session.get(domain + manuscript_link)
            soup = BeautifulSoup(res.content, "html.parser")
            table = soup.find('table', {'class': 'dump_history_table'})
            table = str(table)
            status = re.findall('<tr><td>(.*?)</td><td>', table)
            time = re.findall('</td><td>(.*?)</td></tr>', table)
            # for i in range(len(status)):
            #     print('%s:\t%s' % (status[i], time[i]))
    except:
        with requests.Session() as session:
            res = session.get(main_link)
            soup = BeautifulSoup(res.content, "html.parser")
            payload['ms_id_key'] = soup.find('input', {'id': 'ms_id_key'}).get('value')
            res = session.post(main_link, data=payload)
            soup = BeautifulSoup(res.content, "html.parser")
            links = soup.find_all('a')
            manuscript_link = ''
            for link in links:
                if 'Check Status' in link.text:
                    manuscript_link = link.attrs['href']
                    break
            res = session.get(domain + manuscript_link)
            soup = BeautifulSoup(res.content, "html.parser")
            table = soup.find('table', {'class': 'dump_history_table'})
            table = str(table)
            status = re.findall('<tr><td>(.*?)</td><td>', table)
            time = re.findall('</td><td>(.*?)</td></tr>', table)
    
    return '%s %s' % (status[0], time[0])
        

if __name__ == '__main__':
    getArticleStatus()
