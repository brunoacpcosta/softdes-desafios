from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")


def login_test(user, password):
    # http://username:password@pentesteracademylab.appspot.com/

    driver.get(f"http://{user}:{password}@localhost:8080/")
    login = driver.find_element_by_xpath('//*[@id="navbarsExampleDefault"]/ul/li/a')
    driver.close()

    if user in login.text:
        print("Login feito com sucesso!")
    else:
        print("Usuário ou senha incorreta!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Faltam argumentos, favor consultar o guia de test")
        driver.close()
        exit()

    arg = sys.argv[1]

    if "login" in arg:
        user = sys.argv[2]
        password = sys.argv[3]
        login_test(user, password)
