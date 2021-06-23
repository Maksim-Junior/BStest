from .baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    TASKS_TABLE = (By.XPATH, "/html/body/section/div/div")
    CHROME_CPU = (By.CLASS_NAME, 'bg-warning')


class SearchDynamicTable(Base):
    def tasks(self):
        return self.find_element(Locators.TASKS_TABLE, time=2)

    def chrome_cpu(self):
        return self.find_element(Locators.CHROME_CPU, time=2).text
