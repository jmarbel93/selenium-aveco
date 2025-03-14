from selenium.webdriver.common.by import By

class MusicPage:
    def __init__(self,driver):
        self.driver=driver
        self.music_text = (By.XPATH, "//*[@id='nav-xshop']/ul/li[4]/a")
        
    def music_page(self):
        return "music" in self.driver.current_url