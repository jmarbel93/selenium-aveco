from selenium.webdriver.common.by import By

class FindMusicPage:
    def __init__(self,driver):
        self.driver=driver
        self.music_text = (By.LINK_TEXT, "Música")
        
    def go_to_music_page(self):
        accept_cookies = self.driver.find_element(By.ID, "sp-cc-accept")
        accept_cookies.click()
        print("Cookies aceptadas")
        self.driver.find_element(*self.music_text).click()