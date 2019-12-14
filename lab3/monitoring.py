import requests
import json
import logging
import time
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)
def run():
    main("http://localhost:8000/health")
def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = json.loads(r.content)
        logging.info("Server available, server date: %s", data['date'])
        logging.info("Monitoring page: : %s", data['current_page'])
        logging.info("Server info: %s", data['server_info'])
        logging.info("Client info: %s", data['client_info'])
    except Exception as e:
        logging.error("Exception: %s", e)
'''
    while 1 == 1:
        time.sleep(60)
        run()
'''

if __name__ == '__main__':
    run()
