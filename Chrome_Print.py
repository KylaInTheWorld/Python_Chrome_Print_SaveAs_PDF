import time
import pyautogui
from pywinauto.application import Application
from pywinauto.backend import element_class
from selenium import webdriver

#쉐도우 돔을 위한 Class
class shadowDOM :
    def __init__(self, driver) :
        driver.implicitly_wait(90)
        self.driver = driver
        self.root = driver

    def CSS(self, element):
        driver.implicitly_wait(90)
        self.root = self.driver.execute_script('return arguments[0].shadowRoot',self.root.find_element_by_css_selector(element))

    def Tag(self, element):
        driver.implicitly_wait(90)
        self.root = self.driver.execute_script('return arguments[0].shadowRoot',self.root.find_element_by_tag_name(element))

    #해당 Element 클릭
    def CSSck (self, element):
        driver.implicitly_wait(90)
        self.root.find_element_by_css_selector(element).click()
        text = self.root.find_element_by_css_selector(element).text
        print(text+" 클릭 완료")

#다른 이름으로 저장창 저장버튼 클릭 함수
def click_SaveAs(blYN):
    try:
        #중복된 이름일 경우 저장 버튼과 그냥 저장 버튼이 동일하게 인지
        app.다른이름으로저장확인.Button1.click()
        time.sleep(3)
    except:
        return False
    return True

#크롬드라이브 경로
PTHchrome = r"C:\test\chromedriver.exe"
#PDF 저장 경로
PTHsave = r"C:\test\test.pdf"
#URL 링크
URL = "https://www.google.com/search?q=%ED%85%8C%EC%8A%A4%ED%8A%B8&oq=%ED%85%8C%EC%8A%A4%ED%8A%B8&aqs=chrome..69i57j0i433j0l8.1283j0j15&sourceid=chrome&ie=UTF-8"

#크롬 크롤링 시작
driver = webdriver.Chrome(PTHchrome)
driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(90)
driver.maximize_window()
time.sleep(3)

#프린트 창으로
pyautogui.hotkey('ctrl', 'p')
time.sleep(3)

#Chrome://Print 페이지 인지 : 마지막에 열린 Driver
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)

#PDF로 저장 찾기
PDFCK = shadowDOM(driver)
PDFCK.Tag('print-preview-app')
PDFCK.CSS('#sidebar')
PDFCK.CSS('#destinationSettings')
PDFCK.CSS('#destinationSelect')
PDFCK.CSSck('print-preview-settings-section:nth-child(9) > div > select > option:nth-child(3)')
time.sleep(3)

#가로방향 레이아웃
RayOutCK = shadowDOM(driver)
RayOutCK.Tag('print-preview-app')
RayOutCK.CSS('#sidebar')
RayOutCK.CSS('#container > print-preview-layout-settings')
RayOutCK.CSSck('print-preview-settings-section > div > select > option:nth-child(2)')
time.sleep(3)

#저장 버튼
SaveCK = shadowDOM(driver)
SaveCK.Tag('print-preview-app')
SaveCK.Tag('print-preview-sidebar')
SaveCK.CSS('print-preview-button-strip')
driver.implicitly_wait(90)
SaveCK.CSSck('div > cr-button.action-button')
time.sleep(3)

#다른 이름으로 저장 창
app = Application().connect(class_name="#32770", title='다른 이름으로 저장')
SaveAsWin = app.window()

# 파일 full 경로 입력
SaveAsWin.Edit.type_keys(PTHsave)

# i = 리트라이 숫자
i = 0
# blYN = 존재여부
blYN = True

#저장버튼 클릭 실패할 경우 대비 Loop
while(blYN and i<5):   
    blYN = click_SaveAs(blYN)
    print("저장 클릭 결과 : "+str(blYN)+" / 재시도 횟수 : "+str(i))
    i+=1

if(blYN):
    print("저장 실패")
else :
    print("저장 성공")
