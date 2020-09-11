**#1. Settings**

For running tests using for instance Chrome browser v85, so in case of some changing chrome browser
also needs to be updated drivers/chromedriver (Ubuntu driver for Chrome v85), for iOS (drivers/chromedriver) etc.
Other versions can be found by http://chromedriver.chromium.org/downloads
Tests running using strict screen resolution for headless mode
 

**#2. Installing required packages**

a) Command line: run following command 

    pip3 install -r requirements.txt

b) PyCharm: Go to _File_ -> _Settings_ -> _Project: name_of_project_ -> _Project Interpreter_ ->
click on + button -> install all package from requirements.txt

**#3. Installing Allure Reporting**

Linux: for debian-based repositories a PPA is provided:

    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update
    sudo apt-get install allure

Mac OS X, automated installation is available via Homebrew

    brew install allure

Windows, Allure is available from the Scoop commandline-installer.

To install Allure, download and install Scoop and then execute in the Powershell:

    scoop install allure

Also Scoop is capable of updating Allure distribution installations. 
To do so navigate to the Scoop installation directory and execute

    \bin\checkver.ps1 allure -u

This will check for newer versions of Allure, and update the manifest file. Then execute

    scoop update allure


For detailed information follow:

https://docs.qameta.io/allure/#_installing_a_commandline

    
**#4. Running the tests and generating report**

To enable Allure listener to collect results during the test execution simply add 
_--alluredir_ option and provide path to the folder where results should be stored. 
Write in the _Terminal_ from the root directory the following command:

     pytest --alluredir allure-results/

If you want to clean allure-results directory before running tests just write _--clean-alluredir_
command in the end of the previous command. So it should look like this:

    pytest --alluredir allure-results/ --clean-alluredir

Where _allure-results_ is a directory where *.json results will be generated.

To see the actual report after your tests have finished, you need to use Allure 
commandline utility to generate report from the results. Write in the _Terminal_ from the 
root directory the following command:

    allure generate -c --report-dir allure-report/
    
This command will generate report and now you can open index.html file to see the report.

**Notes:** some browsers like Chrome can block access for json files so use another browser (Firefox etc.)
to see the execution results.

This is already enough to see the Allure report in one command:

    allure serve allure-results
    
Which generates a report in temporary folder from the data found in the provided path and then creates
a local Jetty server instance, serves generated report and opens it in the default browser.

**Examples:**
a)

    pytest --alluredir allure-results/ --clean-alluredir
    allure serve allure-results
 
 Wait for the report is running in the default browser

b)

    pytest --alluredir allure-results/ --clean-alluredir
    allure generate -c --report-dir allure-report/
 
 Open file ./allure-report/index.html

**#5. Running the tests without Allure**
For running test without Allure reporting use following command:

a) Run all existed tests:

    pytest
    
b) Run tests using marks("vacancy" is a name of mark, others can be found in file ./pytest.ini):

    pytest -m "vacancy"
    
c) Run tests using headless mode (by default tests running with option headless mode is False):

    pytest --headless "YES"
    