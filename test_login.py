from selenium import webdriver

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    driver.find_element("id", "userName").send_keys("testuser")
    driver.find_element("id", "password").send_keys("Password123!")
    driver.find_element("id", "login").click()
    assert "Profile" in driver.page_source
    driver.quit()
