from selenium import webdriver

def cjmallCheck(url):    
    path = "C:\\Users\\JY\\JYC\\Projects\\restock\\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(path, options=options)
    driver.get(url)
    driver.implicitly_wait(3)
    
    try:
        driver.find_element_by_class_name('_buy')
        driver.implicitly_wait(3)
        result = True
    except:
        result = False
    
    driver.quit()
    
    return True if result is True else False