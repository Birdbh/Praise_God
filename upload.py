from instagrapi import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


USERNAME = "praisegodourlord"
PASSWORD = "NR^NR;qz+2m\\"

def post():
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    media = cl.video_upload(
        "__temp__.mp4",
        "Praise God Our Lord! -" + "\n" + "Find A Divine Artful Gift For Your Loved Ones In Our Bio" + "\n" "#god #love #jesus #faith #bible #christian #jesuschrist #church #life #peace #pray #godisgood #believe #christ #hope #prayer #blessed #holyspirit #christianity #gospel #truth #amen #motivation #bibleverse #spirituality #worship #inspiration #grace #instagram #instagood"
    )

def webpost():
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.get("https://business.facebook.com/creatorstudio/home")
    instagram_button = driver.find_element(By.ID,"media_manager_chrome_bar_instagram_icon")
    instagram_button.click()

    instagram_login = driver.find_element(By.XPATH,'//*[text()="Instagram login"]')
    instagram_login.click()

    wait = WebDriverWait(driver, 50)
    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != "https://business.facebook.com/creatorstudio/home":
            driver.switch_to.window(window_handle)

    wait.until(EC.visibility_of_element_located((By.NAME,"username")))

    username = driver.find_element(By.NAME, 'username')
    username.send_keys(USERNAME)
    password = driver.find_element(By.NAME,'password')
    password.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH,'//*[text()="Log in"]')
    login_button.click()

    wait.until(EC.visibility_of_element_located((By.NAME,"test")))

    
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[text()="Save Info"]')))
    
    driver.find_element(By.XPATH,'//*[text()="Save Info"]').click()

    
    wait.until(EC.visibility_of_element_located((By.NAME,"test")))



    create_post = driver.find_element(By.XPATH,'//*[text()="Create"]')
    create_post.click()
    reel_post = driver.find_element(By.XPATH, "Reel")
    reel_post.click()

def webpostv2():
    opt = Options()
    opt.add_experimental_option("debuggerAdress","localhost:9999")
    driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=opt)
    driver.get("http://facebook.com")

webpost()

#Praise God Our Lord! -
#Find A Divine Artful Gift For Your Loved Ones In Our Bio
##god #love #jesus #faith #bible #christian #jesuschrist #church #life #peace #pray #godisgood #believe #christ #hope #prayer #blessed #holyspirit #christianity #gospel #truth #amen #motivation #bibleverse #spirituality #worship #inspiration #grace #instagram #instagood