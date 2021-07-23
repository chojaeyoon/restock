import configparser
from bs4 import BeautifulSoup
from restock import StockCheck
from telegram_bot import TelegramBot
from datetime import datetime
import time

# Loading config
config = configparser.ConfigParser()
config.read('config.ini')

# Initialize scraping classes
# TODO Consider function to lambda

def coupangCheck(res):    
    soup = BeautifulSoup(res.text, 'html.parser')
    stock_div = soup.find('div', class_='prod-not-find-known__buy__button')

    if stock_div == None:
        return True

    stock_result = stock_div.text

    import re # 정규표현식 내장함수

    p = re.compile('품절')
    m = p.search(stock_result)

    return True if m == None else False


# main script
if __name__ == "__main__":
    bot = TelegramBot(config['TELEGRAM']['TOKEN'])
    bot.sendMessage(config['TELEGRAM']['RECEIVER_ID'], "Monitoring started.")

    coupang = StockCheck("Q92"
        , "https://www.coupang.com/vp/products/4656360190?itemId=3421774698&vendorItemId=71408330401&q=q92+%EC%9E%90%EA%B8%89%EC%A0%9C&itemsCount=10&searchId=8fd9019b12b94853bf757113463d4119&rank=7"
        , coupangCheck, "utf-8")

    sleep_mins = config['DEFAULT']['INTERVAL_MINS']


    def check(checkTargetArray):
        return list(map(lambda item: item.statusChanged(), checkTargetArray))


    while True:
        returns = check([coupang])

        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), returns)
        
        alerts = list(filter(lambda item: item[0] , returns))

        for item in alerts:
            bot.sendMessage(config['TELEGRAM']['RECEIVER_ID'], "{} status has changed to {}".format(item[3].name, item[0]))
        
        time.sleep(int(sleep_mins) * 60)