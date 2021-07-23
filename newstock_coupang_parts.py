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