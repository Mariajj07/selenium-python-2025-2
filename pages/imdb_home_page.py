from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbHomePage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#suggestion-search")  # Campo de búsqueda
    SEARCH_BUTTON = (By.ID, "suggestion-search-button")           # Botón de lupa

    def search_movie(self, movie_name):
        self.enter_text(self.SEARCH_INPUT, movie_name)
        self.click(self.SEARCH_BUTTON)
