import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import time

print("Time is in the format Minutes : Seconds")

def get_void_time():
    url = "https://pxgame.xyz/void"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    target_line = None
    for line in soup.prettify().split('\n'):
        if "Next void at" in line:
            target_line = line.strip()
            break

    if target_line:
        void_time_str = target_line[30:]
        current_time_utc = datetime.now(pytz.utc)
        gmt_timezone = pytz.timezone('GMT')
        current_time_gmt_str = current_time_utc.astimezone(gmt_timezone).strftime('%H:%M:%S %Z')
        
        void_time = datetime.strptime(void_time_str, '%H:%M:%S %Z')
        current_time_gmt = datetime.strptime(current_time_gmt_str, '%H:%M:%S %Z')
        
        time_difference = void_time - current_time_gmt
        
        if time_difference.total_seconds() < 0:
            time_difference = abs(time_difference)
            time_difference_str = "{}:{} ago".format(int(time_difference.total_seconds() // 60), int(time_difference.total_seconds() % 60))
        else:
            time_difference_str = "{}:{} ahead".format(int(time_difference.total_seconds() // 60), int(time_difference.total_seconds() % 60))
        
        print("Void:", time_difference_str)
    else:
        print("Error")

get_void_time()

while True:
    time.sleep(1)
    get_void_time()
