cd /d %~dp0

rmdir /s /q allure-results
rmdir /s /q allure-report

pytest tests\ --alluredir=allure-results & allure generate allure-results -o allure-report --clean & allure open allure-report