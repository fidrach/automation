"""
This program automates the process of increasing a user's dropbox space using the referal system
"""

from wrapper.Browser import Browser
import time

def main():
    mainAccountEmail = "alexischeungho2@gmail.com"
    mainAccountPassword = "lazy94"
    tempAccountPassword = "123password"

    # -- Open browser and go to Dropbox.com/login
    dropboxBrowser = Browser()
    dropboxBrowser.goTo("https://www.dropbox.com/login")
    # Sign in to main account
    dropboxBrowser.fill("login_email", mainAccountEmail, "last")
    dropboxBrowser.fill("login_password", mainAccountPassword, "last")
    dropboxBrowser.clickByXPath('//*[@id="regular-login-forms"]/form[1]/div[1]/div[5]/button')

    # -- Refer an account
    # Get temporary email
    tempEmailBrowser = Browser()
    tempEmailBrowser.goTo("https://10minutemail.com/")
    # Retrieve temp email
    tempEmail = tempEmailBrowser.getValueById("mailAddress")

    # Refer from main account
    dropboxBrowser.goTo("https://www.dropbox.com/referrals")
    # Fill form with referral email
    dropboxBrowser.fillByXpath('//*[@id="r_tokenizer"]/div/div/div/div[1]/div/textarea', tempEmail)
    # Click refer button
    dropboxBrowser.clickByXPath('//*[@id="r_tokenizer"]/div/button')

    # Wait to receive email
    tempEmailBrowser.waitAndClickById("messagesList")

    print("Waiting 30 mins... for debugging")
    time.sleep(1800)

    # b.browser.find_by_xpath('//*[@id="ui-id-1"]').last.click()
    #
    # b.browser.find_by_xpath('//*[@id="ui-id-2"]/div/div[4]/table/tbody/tr/td/table[2]/tbody/tr[1]/td/a').last.click()
    #
    # b.fill("fname", "Thomas", "last")
    # b.fill("lname", "Hernando", "last")
    # b.fill("password", "123password", "last")
    # b.browser.find_by_name("tos_agree").last.check()




if __name__ == "__main__":
    main()