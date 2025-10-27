from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbResultsPage(BasePage):
    MOVIE_NAME = (By.CLASS_NAME, "ipc-image")

    def click_movie_link(self):
        self.click(self.MOVIE_NAME)
