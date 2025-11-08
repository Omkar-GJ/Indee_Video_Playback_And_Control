import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.login_page import LoginPage
from Pages.title_page import TitlePage
from Pages.video_page import VideoPage

@pytest.mark.selenium
def test_selenium():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://indeedemo-fyc.watch.indee.tv/")

    # POM Implementation
    login = LoginPage(driver)
    title = TitlePage(driver)
    video = VideoPage(driver)

    #Step-1 : Sign in to the Platform.
    login.accept_cookies()
    login.login_with_pin("WVMVHWBS")
    login.click_brand_button()
    time.sleep(10)

    #Step-2 : Navigate to the 'Test Automation Project':
    title.scroll_to_test_project()
    title.open_test_project()

    #Step-3 : Switch to the 'Details' Tab:
    video.open_video_details()

    #Step-4 : Return to the 'Videos' Tab
    video.switch_back_to_videos_tab()

    #Step-5 : Play the Video
    #Step-7 : Adjust Volume:
    #Srep-8 : Change Video Resolution:
    
    video.play_and_pause_video()

    #Step-9 : Pause and Exit:
    video.navigate_back_sequence()

    #Step-10 : Logout:
    video.sign_out()

    
    time.sleep(5)
    driver.quit()
