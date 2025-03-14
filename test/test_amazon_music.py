from selenium import webdriver
from pages.verify_music_page import MusicPage
from pages.amazon_music_page import FindMusicPage


def test_navigate_to_music_page():
    
    driver = webdriver.Edge()  
    driver.get("https://www.amazon.es")

    amazon_page = FindMusicPage(driver)
    amazon_music_page = MusicPage(driver)


    amazon_page.go_to_music_page()

    assert amazon_music_page.music_page(), "No estamos en la página de música"

    driver.quit()
