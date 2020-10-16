from selenium.webdriver.support.events import AbstractEventListener

class MyListener(AbstractEventListener):

    def after_click(self, element, driver):
        print ("Depois de clicar no elemento")