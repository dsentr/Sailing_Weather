#GLERL (Great Lakes Environment Research Laboratory) data from https://www.glerl.noaa.gov/metdata/chi/
#This is data from the Harrison-Dever Water Crib

import requests
import sys
from bs4 import BeautifulSoup

URLa = "https://www.glerl.noaa.gov/metdata/chi/"

#request headers, spoofed to avoid bot detection
headersa = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Referer': 'https://www.google.com/'}

requesta = requests.get(URLa, headers = headersa)
requesta1 = requesta.text
soup1 = BeautifulSoup(requesta1, 'html.parser')
soup2 = soup1.findAll('table')[1]

def windspeed():
    windspeed = str(soup2.findAll('td')[1].get_text())
    windspeedonly = windspeed[0:8]
    WindSText = "Wind Speed: "
    ws1 = " "
    ws2 = "  "
    mphtext = "mph"
    windmph = str(float(windspeed[0:4]) * 1.15078)[0:5]

    print(WindSText + windspeedonly + ws2 + windmph + ws1 + mphtext)


def winddirection():
    winddirection = str(soup2.findAll('td')[5].get_text())
    WindDText = "Wind Direction: "

    print(WindDText + winddirection)

def airtemp():
    airtemp = str(soup2.findAll('td')[7].get_text())[0:8]
    airtemptext = "Air Temperature is: "

    print(airtemptext + airtemp)


windspeed()
winddirection()
airtemp()
