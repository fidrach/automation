from splinter import Browser as SplinterBrowser
import os


class Browser(object):

    def __init__(self, browserName="chrome"):
        self.url = None
        self.driverPath = None
        self.browserName = browserName

        basePath = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "dependency"

        if self.browserName == "chrome":
            self.driverPath = basePath + os.sep + "chromedriver.exe"

        driverJson = {"executable_path": self.driverPath}
        self.browser = SplinterBrowser(self.browserName, **driverJson)

    def goTo(self, url):
        self.browser.visit(url)

    def getValueById(self, id):
        return self.browser.find_by_id(id).first.value

    def findByIdAndClick(self, id):
        self.browser.find_by_id(id).first.click()

    def fillByName(self, name, value, position="first"):
        if position == "last":
            self.browser.find_by_name(name).last.fillByName(value)
        else:
            self.browser.find_by_name(name).first.fillByName(value)

    def fillByXpath(self, xpath, value, position="first"):
        if position == "last":
            self.browser.find_by_xpath(xpath).last.fillByName(value)
        else:
            self.browser.find_by_xpath(xpath).first.fillByName(value)

    def clickByXPath(self, xpath,  position="first"):
        if position == "last":
            self.browser.find_by_xpath(xpath).last.click()
        else:
            self.browser.find_by_xpath(xpath).first.click()

    def waitAndClickByXPath(self, xpath, waitTime=300):
        """ Polls every 10 secs until wait time """
        timerIncrease = 30
        timer = 0
        while(timer < waitTime):
            print("DEBUG: Looping...")
            if (self.browser.is_element_present_by_xpath(xpath, timerIncrease)):
                self.clickByXPath(xpath, position="last")
                print("DEBUG: Found Path!")
                break
            else:
                timer += timerIncrease

    def checkByName(self, name, position="first"):
        if position == "last":
            self.browser.find_by_name(name).last.check()
        else:
            self.browser.find_by_name(name).first.check()