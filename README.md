# Python_Chrome_Print_SaveAs_PDF
* ver1.0 : 2021.06.23

# 시작하기 
첫 번째 파이썬 프로젝트 중 구현하게 된 소스입니다.
구동은 엄~청 느리지만, 안정성에 대한 부분과 Class 공부를 위해 나름 보완 해보았습니다.

* Chrome://Print 화면의 컨트롤에 대한 소스입니다. 
* Python의 Selenium를 사용한 웹 크롤링 방식입니다.  
* ChromeDriver를 다운로드 받아 주세요. 
  * https://chromedriver.chromium.org/downloads   

# 설치 패키지 
* Selenium.webdriver : 웹 크롤링을 위한 패키지 
* pywinauto.application : 다른 이름으로 저장 창을 잡기 위한 패키지
  * 파이썬 버전에 대한 이슈가 있습니다. 
  * https://github.com/pywinauto/pywinauto/issues/868
* pyautogui : 프린트 화면을 띄우기 위한, Ctrl + p 를 누르는 패키지 
* time : 타임 딜레이를 위한 패키지  

# 변수 
* PTHchrome : 크롬 드라이브 풀 경로 
* PTHsave : 다운로드 파일명 풀 경로 
* URL : 사이트 링크
