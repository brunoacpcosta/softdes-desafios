from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\gustavogb\Documents\chromedriver_win\chromedriver.exe")


def login_test(user, password):
    # http://username:password@pentesteracademylab.appspot.com/

    driver.get(f"http://{user}:{password}@localhost:8080/")
    login = driver.find_element_by_xpath('//*[@id="navbarsExampleDefault"]/ul/li/a')

    if user in login.text:
        print("Login feito com sucesso!")
        return 1
    else:
        print("Usuário ou senha incorreta!")
        return 0

def challenge_test(user,password):
    if login_test(user, password):
        wrong_upload = "C:\\Users\\gustavogb\\Documents\\Insper\\DEV_ABERTO\\softdes-desafios\\test\\desafio3.py"
        right_upload = "C:\\Users\\gustavogb\\Documents\\Insper\\DEV_ABERTO\\softdes-desafios\\test\\desafio.py"
        time.sleep(0.4)
        
        s = driver.find_element_by_xpath("//input[@type='file']")
        time.sleep(0.2)
        s.send_keys(wrong_upload)
        time.sleep(0.2)
        button = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        time.sleep(0.2)
        button.click()
        time.sleep(0.2)

        row = driver.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/table/tbody/tr[1]/td[2]")
        
        if row.text == "Sem erros.":
            print("Seu arquivo foi corretamente enviado")
        else:
            print("Houve um erro, por favor enviar o arquivo novamente")
        driver.close()
        

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
        driver.close()

    if "upload" in arg:
        challenge_test("Gob","Gob")

