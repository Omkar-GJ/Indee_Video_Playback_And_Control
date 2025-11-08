import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Method to switch to the 'Details' Tab:
    def open_video_details(self):
        target = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.remaining-views")))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target)
        time.sleep(4)
        target.click()
        time.sleep(2)
        details_link = self.wait.until(EC.element_to_be_clickable((By.ID, "detailsSection")))
        details_link.click()
        time.sleep(10)

    #Method to Return to the 'Videos' Tab:
    def switch_back_to_videos_tab(self):
        videos_link = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Videos')]")))
        videos_link.click()

    #Method to Locate the video on the page and play.
    def play_and_pause_video(self):
        print("PLAYY--")
        play_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play Video']"))
        )
        play_button.click()
        time.sleep(10)

        iframe = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "video_player"))
        )
        self.driver.switch_to.frame(iframe)

        """
        Video time to get start/play time is getting vary due to network speed/system issue,
        Hence video is kept to play till 30 second.
        """
        #Allow the video to play for 10 seconds, then pause it.
        time.sleep(30)
        self.driver.execute_script("if(window.jwplayer){jwplayer().pause();}")
        
        time.sleep(3)
        self.driver.execute_script("if(window.jwplayer){jwplayer().setVolume(50);}")

        WebDriverWait(self.driver, 10).until(
            lambda d: self.driver.execute_script(
                "return typeof jwplayer !== 'undefined' && jwplayer().getQualityLevels().length > 0")
        )
        quality_levels = self.driver.execute_script("return jwplayer().getQualityLevels();")
        print('Available qualities:', [q['label'] for q in quality_levels])


        # Change Video Resolution to 480p
        self.driver.execute_script("""
            var levels = jwplayer().getQualityLevels();
            for (var i = 0; i < levels.length; i++) {
                if (levels[i].label.includes('480')) {
                    jwplayer().setCurrentQuality(i);
                    break;
                }
            }
        """)

        #Change the resolution back to 720p
        WebDriverWait(self.driver, 5).until(
            lambda d: self.driver.execute_script("return jwplayer().getCurrentQuality()")
        )

        self.driver.execute_script("""
            var levels = jwplayer().getQualityLevels();
            for (var i = 0; i < levels.length; i++) {
                if (levels[i].label.includes('720')) {
                    jwplayer().setCurrentQuality(i);
                    break;
                }
            }
        """)
        

        #Pause the video after adjusting the resolution
        self.driver.execute_script("if(window.jwplayer){jwplayer().pause();}")

        self.driver.switch_to.default_content()

    def navigate_back_sequence(self):
        #time.sleep(10)
        #Press the Back button
        self.driver.back()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Test automation project')]"))
        )

        time.sleep(5)
        self.driver.back()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'All Titles')]"))
        )

    #Method to Locate and click the Logout button to sign out from the platform.
    def sign_out(self):
        sign_out_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signOutSideBar"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_out_btn).click().perform()
