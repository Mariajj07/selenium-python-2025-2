from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbMoviePage(BasePage):
    MOVIE_TITLE = (By.CLASS_NAME, "hero__primary-text")
    MOVIE_RATING = (By.CSS_SELECTOR, ".sc-4dc495c1-1.lbQcRY")

    def get_movie_title(self):
        return self.find_element(self.MOVIE_TITLE).text

    def get_movie_rating(self):
        return self.find_element(self.MOVIE_RATING).text