<<<<<<< Updated upstream
Hello there !

Below are the Key features of the framework :

1- Compatability with different browsers:
    Conftest.py file has addoption hook that provides you the advantage to execute the test cases based on the browser of your choice
         (Firefox & Chrome), As chrome is set as default, Hence if you don't provide any browser it will by default use firefox
    Synatx to run : python -m pytest --browser firefox 
    
2- Fixture used for BrowserSetUp and BrowserTearDown Method :
    conftest.py file has the fixture test_set Up, Hence all you need is to include this fixture in your test , as this fixture is under
          conftest.py hence there is no need to import this file.
 
3- Screenshot attachment in reports :
   when you execute below allure commands to generate report, you will have the screenshot attached to your allure report    
   commands :python -m pytest --browser firefox --alluredir Reports
             Allure serve Reports

4- Test wise screenshots saving functionality:
    In case you need to validate snapshots manually, Here you will get them in dedicated screenshot folder mapped to your testcase in
            sequential order
    
5- Parallel testing supported :
   This framework supports parallerl testing as well, So in case you want to execute test in less time use below command   
   command : pytest -n 3 --dist=loadscope

###########################################################################################################################

6- This Framework has two conftest files for below reason :

        A -Conftest.py (Present Under Root folder) - To facilitate testing on normal Host system

        B- Conf_Zalenium.py (Present under GRID folder) - To enable testing on GRID using Zalenium and facilitate cross browser tesing on Chrome & Firefox browser only

        C -Conftest_Sequential.py (Present under GRID folder) - To enable testing on GRID using Zalenium and its integration with sauce labs to perform cross browser testing on - Chrome, Firefox & Safari browser


 ###########################################################################################################################

In case you want to execute this framework on your local machine - I have listed the requirements with version under Requirements.txt file,
Please execute command from your command line to install the libraries.
command : pip install -r Requirements, Additionally you can execute tox.ini file - it will create the virtual environment with all the required dependencies

###########################################################################################################
Implemented markers for grouping of test @pytest.mark.smoke and same has been registered under ini file
Below is the command to execute test via markers :
pytest -m smoke : To execute smoke test case only
pytest -m "not smoke" : To execute testcase that are not smoke

#############################################################################################################

Incase of any query/concerns/ suggestions - Please contact me on - email.aloksrivastav@gmail.com
=======
Inorder to install requirements - pip install -r Requirements

>>>>>>> Stashed changes
