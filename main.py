import requests

class StockCheck: # StockCheck 클래스가 스크래핑 부분을 담당

    def __init__(self, name, url, checkMethod, encoding):
        self.name = name
        self.url = url
        self.checkMethod = checkMethod # 품절 여부를 체크하는 함수
        self.encoding = encoding
        self.last_status = False # 최종 상태를 저장하기 위한 변수


    def getResponse(self): # HTTP 요청을 담당하는 함수
        # TODO Pass parameters def getResponse(self, params):
        # TODO Add some error handling
        URL = self.url
        
        return requests.get(URL)


    def check(self): # 가장 중요한 부분으로 getResponse 실행을 통해 응답을 가져오고 결과를 리턴
        res = self.getResponse()

        if res.encoding != self.encoding: # 인코딩 관련 문제 방지를 위해 인코딩을 강제로 설정
            res.encoding = self.encoding

        return self.checkMethod(res) 

    def statusChanged(self): # check 함수를 실행하여 상태가 바뀌었는지 체크하는 함수
        status = self.check()

        if (self.last_status != status):
            self.last_status = status
            return (True, not(self.last_status), self.last_status, self)
        
        return (False, self.last_status, status, self)


    def __str__(self): # 클래스의 기본 함수를 오버라이딩 한 부분, 로그 등을 출력할 때 보기 쉽게 만들기 위함.
        return "{} is {}".format(self.name, self.last_status)


if __name__ == "__main__": # 테스트 코드
    def cjCheck(res):
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(res.text, 'html.parser')
        stock_div = soup.find("a", class_= "_buy")

        if stock_div == None:
            return True

        stock_result = stock_div.text

        import re # 정규표현식 내장함수

        p = re.compile('매진')
        m = p.search(stock_result)

        return True if m == None else False


    lego_friends_perk = StockCheck("Friends Central Perk"
        , "https://www.lego.com/ko-kr/product/central-perk-21319"
        , cjCheck, "utf-8")
    stock = lego_friends_perk.check()
    print(lego_friends_perk.name, "Available? ", stock)
    (status_changed, last_status, current_status) = lego_friends_perk.statusChanged()
    print(lego_friends_perk.name, "Status Changed? ", status_changed, ", Last Status? ", last_status, ", Current Status? ", current_status)
