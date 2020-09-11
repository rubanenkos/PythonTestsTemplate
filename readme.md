#1. Setting

For running tests using for instance Chrome browser v85, so in case of some changing chromebrowser also needs to be updated
Driver/chromedriver_linux (Ubuntu driver for Chrome v85), for iOS (Driver/chromedriver_ios) etc.
Other versions can be found by http://chromedriver.chromium.org/downloads
Tests running using strict screen resolution 
 

#2. Installing of important packages

The best way to install all required libs is just execute next command:
 >> pip3 install -r requirements.txt

To install all required libraries manually
For PyCharm: Go to _File_ -> _Settings_ -> _Project: name_of_project_ -> _Project Interpreter_ ->
click on + button -> install _allure-pytest_, _selenium_

#3. Installing of Allure

The package can to be manually installed too
Download the .deb package from here:

https://launchpad.net/~qameta/+archive/ubuntu/allure/+files/allure_2.4.1~xenial_all.deb
    
You can use Gdebi to install it by double clicking it, or using dpkg as follows

    sudo dpkg -i allure_2.4.1~xenial_all.deb
    
Once you are done with dpkg, you should execute
    
    sudo apt-get install -f
    
#4. Running the tests and generating report

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

    allure generate -c --report-dir AllureReport/
    
This command will generate report and now you can open index.html file to see the report.

**Notes:** some browsers like Chrome can block access for json files so use other browser like Firefox
to see the execution results.

This is already enough to see the Allure report in one command:

    allure serve allure-results
    
Which generates a report in temporary folder from the data found in the provided path and then creates
a local Jetty server instance, serves generated report and opens it in the default browser.
