*** Settings ***

Documentation    A resource file with reusable keyword and variable

...     The system specific keywords created here form our own domain specific language. They
...     utilize keywords provided by the imported SeleniumLibrary

...     by the imported SeleniumLibrary

Library    SeleniumLibrary


*** Variables ***
${url}    https://rahulshettyacademy.com/loginpagePractise/
${user_name}    rahulshettyacademy
${invalid_password}    123456
${valid_password}    learning


*** Keywords ***

open the browser with the Mortgage payment url
    Create Webdriver    Chrome
    Go To    ${url}

Close Browser session
    Close Browser