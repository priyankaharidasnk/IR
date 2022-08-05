import schedule
import time
import datetime
from Crawling import crawling
def run_crawler():
    date = datetime.datetime.now()
    crawling()
schedule.every().saturday.at("03:00").do(run_crawler)

while True:
    schedule.run_pending()
    time.sleep(1)
