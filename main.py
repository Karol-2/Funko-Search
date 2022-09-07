from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def Find_Pop(site, type, search_bar, pop):
    driver.get(site)

    if type == "id":
        search_box = driver.find_element(By.ID, search_bar)
    elif type == "name":
        search_box = driver.find_element(By.NAME, search_bar)
    elif type == "class":
        search_box = driver.find_element(By.CLASS_NAME, search_bar)
    elif type == "xpath":
        search_box = driver.find_element(By.XPATH, search_bar)
    else:
        print("MISSING DATA")

    search_box.send_keys(pop)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.switch_to.new_window()


database = [{"site": "https://gamegoods.pl/funko", "find_type": "id", "string": "search-engine-string"},
            {"site": "https://popando.pl/", "find_type": "name", "string": "search"},
            {"site": "https://www.amazon.pl/", "find_type": "id", "string": "twotabsearchtextbox"},
            {"site": "https://mediamarkt.pl/", "find_type": "xpath",
             "string": "//*[@id='spark']/div[3]/div[1]/div[2]/div[1]/div/div[2]/form/div/input"},
            {"site": "https://popvinyl.pl/", "find_type": "xpath",
             "string": "//*[@id='__layout']/div/header/div[1]/div/div[3]/div[1]/div/form/input"},
            {"site": "https://pixel-shop.pl/", "find_type": "name", "string": "search"},
            {"site": "https://www.stworkipotworki.pl/funko", "find_type": "name", "string": "search"},
            {"site": "https://www.dystryktzero.pl/", "find_type": "id", "string": "search_input"},
            {"site": "https://www.emp-shop.pl/", "find_type": "id", "string": "q"}]

looking_for = input("What are you looking for?: ")
driver = webdriver.Chrome()

for i in range(len(database)):
    Find_Pop(database[i]["site"], database[i]["find_type"], database[i]["string"], looking_for)

# {"site": "https://lamaco.pl/?v=9b7d173b068d", "find_type": "name", "string": "s"} # ERROR
# {"site": "https://www.empik.com/", "find_type": "class", "string": "css-1rwl265-input-1"} # ERROR
# {"site": "https://popownia.pl/", "find_type": "xpath", "string": "//*[@id='header-search']/div/form/input[1]"}  # ERROR
