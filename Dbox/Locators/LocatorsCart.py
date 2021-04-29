class LocatorsCart():
    # cart option
    cart_script = "var s=document.getElementsByClassName('nav-link');s[3].click();"

    # place order
    po_xpath = "//button[@class = 'btn btn-success']"

    # names
    name_xpath = "//input[@id = 'name']"

    # country
    country_xpath = "//input[@id = 'country']"

    # city
    city_xpath = "//input[@id = 'city']"

    # credit card
    credit_xpath = "//input[@id = 'card']"

    # month
    month_xpath = "//input[@id = 'month']"

    # year
    year_xpath = "//input[@id = 'year']"

    # purchase
    purchase_xpath = "//button[@onclick = 'purchaseOrder()']"

    # OK button
    ok_script = "var s3=document.getElementsByClassName('confirm btn btn-lg btn-primary');s3[0].click();"

    # close button
    clssbtn_script = "var n=document.getElementsByClassName('btn btn-secondary');n[2].click();"