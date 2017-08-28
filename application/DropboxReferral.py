"""
Author: Alexis Cheung Ho
Date: 8/27/17
Summary:    This program automates the process of increasing a user's dropbox space
            using the referral system - Project to test automation development
Note: Automation might not work in the future as it involves html scraping and UI automation
"""
from interface.DropboxInstaller import DropboxInstaller
from wrapper.Browser import Browser
from interface.TaskKill import TaskKill
from pywinauto.application import Application
import time

def main():
    mainAccountEmail = "l834542@mvrht.net"
    mainAccountPassword = "123password"
    tempAccountPassword = "123password"
    tempAccountFName = "Marcos"
    tempAccountLName = "Rodriguez"

    # -- Open browser and go to Dropbox.com/login
    dropboxBrowser = Browser()
    dropboxBrowser.goTo("https://www.dropbox.com/login")
    # Sign in to main account
    dropboxBrowser.fillByName("login_email", mainAccountEmail, "last")
    dropboxBrowser.fillByName("login_password", mainAccountPassword, "last")
    dropboxBrowser.clickByXPath('//*[@id="regular-login-forms"]/form[1]/div[1]/div[5]/button')

    # -- Refer an account
    print("Creating referral email")
    # Get temporary email
    tempEmailBrowser = Browser()
    tempEmailBrowser.goTo("https://10minutemail.com/")
    # Retrieve temp email
    tempAccountEmail = tempEmailBrowser.getValueById("mailAddress")

    # Refer from main account
    dropboxBrowser.goTo("https://www.dropbox.com/referrals")
    # Fill form with referral email
    dropboxBrowser.fillByXpath('//*[@id="r_tokenizer"]/div/div/div/div[1]/div/textarea', tempAccountEmail)
    # Click refer button
    dropboxBrowser.clickByXPath('//*[@id="r_tokenizer"]/div/button')

    # Wait to receive email
    tempEmailBrowser.waitAndClickByXPath('//*[@id="ui-id-1"]')
    referralLink = tempEmailBrowser.waitAndGetHrefByXPath('//*[@id="ui-id-2"]/div/div[4]/table/tbody/tr/td/table[2]/tbody/tr[1]/td/a')
    tempEmailBrowser.goTo(referralLink)
    # Sign up new account
    tempEmailBrowser.waitAndFillByName("fname", tempAccountFName)
    tempEmailBrowser.fillByName("lname", tempAccountLName, "last")
    tempEmailBrowser.fillByName("password", tempAccountPassword, "last")
    tempEmailBrowser.fillByName("email", tempAccountEmail, "last")
    tempEmailBrowser.checkByName("tos_agree", "last")
    signUpValidation = tempEmailBrowser.clickByXPath('//*[@id="invite-register-container"]/div/form/button', "last")

    assert(signUpValidation == True), "Temporary Email failed to sign up"

    # -- Install Dropbox
    print("Installing Dropbox")
    dropboxInstaller = DropboxInstaller()
    dropboxInstaller.run()
    time.sleep(30)

    # -- Terminate Dropbox
    print("Closing Dropbox for automation")
    # TODO: move this inside taskkill and make a function to modify args (only in constructor right now)
    taskKill = TaskKill(["/IM", "Dropbox*", "/F"])
    taskKill.run()

    # -- Open Dropbox with automation and sign in
    print("Enabling Dropbox UI automation")
    dropboxApp = Application().start(r"C:\Program Files (x86)\Dropbox\Client\Dropbox.exe")
    time.sleep(30)
    dropboxApp["Set Up Dropbox"].SetFocus()
    dropboxApp["Set Up Dropbox"].TypeKeys("{TAB 2}")
    dropboxApp["Set Up Dropbox"].TypeKeys(tempAccountEmail)
    dropboxApp["Set Up Dropbox"].TypeKeys("{TAB}")
    dropboxApp["Set Up Dropbox"].TypeKeys(tempAccountPassword)
    dropboxApp["Set Up Dropbox"].TypeKeys("{TAB}")
    dropboxApp["Set Up Dropbox"].TypeKeys("{ENTER}")
    time.sleep(30)
    taskKill.run()

    # -- Uninstalling Dropbox


    # referral link - https://db.tt/qtp4RnDIht

    debug = input("DEBUG: Press anything to exit:")
    # dropboxBrowser.close()
    tempEmailBrowser.close()
    return 0

    # app["Set Up Dropbox"].SetFocus()
    # app["Set Up Dropbox"].TypeKeys("{TAB 2}")
    # app["Set Up Dropbox"].TypeKeys(account)
    # app["Set Up Dropbox"].TypeKeys("{TAB}")
    # app["Set Up Dropbox"].TypeKeys(password)
    # app["Set Up Dropbox"].TypeKeys("{TAB}")
    # app["Set Up Dropbox"].TypeKeys("{ENTER}")




if __name__ == "__main__":
    main()