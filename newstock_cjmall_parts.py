from selenium import webdriver

def cjmallCheck(res):    
    path = "C:\\Users\\JY\\JYC\\Projects\\restock\\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.get('https://display.cjonstyle.com/p/item/77766343?channelCode=30001003')
    driver.implicitly_wait(3)
    
    try:
        driver.find_element_by_class_name('_buy')
        driver.implicitly_wait(3)
        result = True
    except:
        result = False
    
    return True if result is True else False