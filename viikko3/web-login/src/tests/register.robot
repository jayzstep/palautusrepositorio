*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle234
    Set Password Confirmation  kalle234
    Submit New User
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle234
    Set Password Confirmation    kalle234
    Submit New User
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  123
    Set Password Confirmation  123
    Submit New User
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle
    Set Password  vainkirjaimia
    Set Password Confirmation  vainkirjaimia
    Submit New User
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle234
    Set Password Confirmation  kalle235
    Submit New User
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Set Username  kalle
    Set Password  kalle234
    Set Password Confirmation  kalle234
    Submit New User
    Register Should Fail With Message  User with username kalle already exists
    
Login After Successful Registration
    Set Username  kalle
    Set Password  kalle234
    Set Password Confirmation  kalle234
    Submit New User
    Click Link  ohtu
    Click Button  logout-button
    Set Username  kalle
    Set Password  kalle234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle234
    Set Password Confirmation  kalle235
    Submit New User
    Click Link  Login
    Set Username  kalle
    Set Password  kalle234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit New User
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
