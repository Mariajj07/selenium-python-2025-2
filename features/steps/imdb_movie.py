from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import IMDbHomePage
from pages.imdb_results_page import IMDbResultsPage
from pages.imdb_movie_page import IMDbMoviePage

@given('el usuario esta en el home page de IMDb')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = IMDbHomePage(context.driver)

@when('busca la pelicula "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = IMDbResultsPage(context.driver)

@when('selecciona el primer resultado de IMDb')
def step_select_result(context):
    context.imdb_results.click_movie_link()
    context.imdb_movie = IMDbMoviePage(context.driver)

@then('el titulo debe ser "{expected_title}"')
def step_validate_title(context, expected_title):
    obtained_title = context.imdb_movie.get_movie_title()
    assert obtained_title == expected_title, f"Los titulos no coinciden: se esperaba '{expected_title}', pero se obtuvo '{obtained_title}'"

@then('el rating debe ser {expected_rating}')
def step_validate_rating(context, expected_rating):
    obtained_rating = context.imdb_movie.get_movie_rating()
    assert str(obtained_rating) == expected_rating, f"Los ratings no coinciden: se esperaba '{expected_rating}', pero se obtuvo '{obtained_rating}'"

