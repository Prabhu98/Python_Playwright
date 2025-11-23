*** Settings ***

Documentation    To validate the Login form
Library    SeleniumLibrary
Test Setup    open the browser with the Mortgage payment url
Test Teardown    Close Browser session
Resource    resource.robot

*** Variables ***
${Error_Message_Login}    css:.alert-danger
${Shop_page_load}    css:.nav-link


*** Test Cases ***
Validate UnSuccessful Login
    Maximize Browser Window
    Fill the login Form    ${user_name}    ${invalid_password}
    wait until Element is located in the page    ${Error_Message_Login}
    verify error message is correct

Validate Cards display in the shopping page
    Maximize Browser Window
    Fill The Login Form    ${user_name}    ${valid_password}
    wait until Element is located in the page    ${Shop_page_load}
    Set Selenium Implicit Wait    5

*** Keywords ***

Fill the login Form
    [Arguments]    ${username}    ${password}
    Input Text    id:username    ${username}
    Input Password    id:password    ${password}
    Click Button    id:signInBtn

wait until it checks and display error message
    Wait Until Element Is Visible    ${Error_Message_Login}

wait until Element is located in the page
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}  
    

# To store value in variable
verify error message is correct
     ${result}=     Get Text    ${Error_Message_Login}
     Should Be Equal As Strings    ${result}    Incorrect username/password.
     Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.

