Pytest+Selenoid+Docker+Allure
==

***Steps for performing tests using selenoid, pytest, docker, allure.***    
For pre-initialization browser  in 
fixtures used factory pattern.(**conftest.py**).
Used **selenium.webdriver.chrome / selenium.webdriver.firefox** and
added an option to use selenoid(
Look **chrome_browser_selenoid** and **firefox_browser_selenoid** methods).

## For Windows 7 and above.

Create the virtual environment:
- `py -m venv venv`

Run the virtual environment:
- `.\venv\Scripts\activate`

Download selenoid with the command:
- `(New-Object Net.WebClient).DownloadFile('https://github.com/aerokube/cm/releases/download/1.8.1/cm_windows_amd64.exe', 'cm.exe')`

After that how docker images are downloaded, run selenoid with the command:
- `./cm selenoid start --vnc`

Selenoid will be use port 4444:
- `docker ps`

Сan check the running browsers:
- `curl http://localhost:4444/status`

Run the tests and creating alluredir:
- `pytest -s -v .\tests\ --alluredir=allureress`

### Add-on for using the UI.

Selenoid have UI, this can be run:
- `./cm selenoid-ui start`

Run the tests and creating alluredir:
- `pytest -s -v .\tests\ --alluredir=allureress`

Open in browser link:
- `http://localhost:8080/`

## For Linux and above.

Create the virtual environment:
- `python3 -m venv venv`

Run the virtual environment:
- `. .\venv\bin\activate`

Download selenoid with the command:
- `curl -s https://aerokube.com/cm/bash | bash`

After that how docker images are downloaded, run selenoid with the command:
- `. ./cm selenoid start --vnc`

Selenoid will be use port 4444:
- `docker ps`

Сan check the running browsers:
- `curl http://localhost:4444/status`

Run the tests and creating alluredir:
- `pytest -s -v .\tests\ --alluredir=allureress`

### Add-on for using the UI.

Selenoid have UI, this can be run:
- `. ./cm selenoid-ui start`

Run the tests and creating alluredir:
- `pytest -s -v .\tests\ --alluredir=allureress`

Open in browser link:
- `http://localhost:8080/`

>Run the allure:
>- allure serve allureress


### Example of test cases on the website: _https://www.saucedemo.com_

**test_standard.py:**   
_Log in to the site. Chose two things to buy.
Checking the number of items in the trading card icon.
Checking the things we have chosen. Entered first name,
last name, zip/postal code.
Expect that the purchase was completed correctly._

**test_headers.py:**    
_Checking status code, url, cookies, on the page.
Compare values in the headers._


**_Sources I used:_**     
https://intexsoft.com/blog/selenide-test-automation-using-selenoid-in-the-docker-container/     
https://gainanov.pro/eng-blog/devops/selenium-in-docker-with-selenoid/  
https://4te.me/post/selenium-docker/    
https://stackoverflow.com/a/20476904    
