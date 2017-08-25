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

    def fill(self, name, value, position="first"):
        if position == "last":
            self.browser.find_by_name(name).last.fill(value)
        else:
            self.browser.find_by_name(name).first.fill(value)

    def fillByXpath(self, xpath, value, position="first"):
        if position == "last":
            self.browser.find_by_xpath(xpath).last.fill(value)
        else:
            self.browser.find_by_xpath(xpath).first.fill(value)

    def clickByXPath(self, xpath):
        self.browser.find_by_xpath(xpath).first.click()

    def waitAndClickById(self, id, waitTime=300):
        if (self.browser.is_element_present_by_id(id, waitTime)):
            self.findByIdAndClick(id)