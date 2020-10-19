from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="c:/users/simon/downloads/chromedriver.exe")

my_driver.get("http://127.0.0.1:5001/scores")

def test_scroe_service():
    score = my_driver.find_element_by_id("score").text

    if int(score) in range (1,1001):
        return True
    else:
        return False

def main_fuction():
   if test_scroe_service():
        return 0
   else:
        return -1


main_fuction()

