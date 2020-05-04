#!/usr/bin/env python3
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import auth
import re

def getName():
    return 'GRL'

def getArticleStatus():
    domain = 'https://advances-submit.agu.org/'
    main_link = 'https://advances-submit.agu.org/cgi-bin/main.plex?el=A7On4GMHn3A1HZrq7F3A9ftdkeA3khPTT7lbvXJ05jpgZ'
    try:
        with requests.Session() as session:
            res = session.get(main_link)
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
        print('Error\n')
 
    return '%s %s' % (time[0], status[0])
        

if __name__ == '__main__':
    print(getArticleStatus())
