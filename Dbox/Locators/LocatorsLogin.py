class LocatorsLogin():
    # sign up option
    signupopt_ID = "signin2"

    # sign up username
    signupusrn_ID = "sign-username"

    # sign up password
    signuppssd_ID = "sign-password"

    # sign up button
    signupbtn_xpath = "//button[@onclick='register()']"

    # close button
    closebtn_script = "var x =document.getElementsByClassName('btn btn-secondary');x[1].click();"

    # login option
    loginopt_ID = "login2"

    # login username
    loginusrn_ID = "loginusername"

    # login password
    loginpssd_ID = "loginpassword"

    # login button
    loginbtn_xpath = "//button[@onclick='logIn()']"

    # close button
    clsbtn_script = "var x =document.getElementsByClassName('btn btn-secondary');x[2].click();"

    # welcome option
    welcomeopt_script = "var d=document.getElementsByClassName('nav-link');d[6].click();"