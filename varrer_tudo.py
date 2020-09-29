from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Teste:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def dispara_eventos(self):
        driver = self.driver

        #elem_div = driver.find_elements_by_tag_name("div")
        stop = driver.find_element_by_tag_name("h1")
        #elem_div = driver.find_elements_by_css_selector("body > *")
        #print(len(elem_div))
        elementos = driver.find_elements_by_css_selector("body > *")
        print(len(elementos))
        for i in elementos:
            print("------------------------------------Elemento -------------------------------------")
            #if (i.is_displayed() == True):
            print('Elemento: ', i.get_attribute('outerHTML'))
            filhos = i.find_elements_by_xpath('.//*')
            for j in filhos:
                print('Elemento filho: ', j.get_attribute('outerHTML'))
                try:
                    j.click()
            #        netos = j.find_elements_by_xpath('.//*')
            #        if(len(netos) > 1):
            #            for k in netos:
            #                if(k.is_displayed() == True):
            #                    print('Elemento neto', k.get_attribute('outerHTML'))
            #                    print(" ")
                    stop.click()
                except:
                    print("Não foi possível clicar em: ", j.get_attribute('innerHTML'), j.get_attribute('outerHTML'))
           #     netos = j.find_elements_by_xpath('.//*')
           #     for k in netos:
           #         if(k.is_displayed() == True):
           #             print('Propriedade', k.get_attribute('outerHTML'))
           #             print(" ")
           #     stop.click()
#
        #elems_div = driver.find_elements_by_tag_name("div")
        #for i in elems_div:
        #    print (i.get_attribute('outerHTML'))
        #    if (i.is_displayed() == True):
        #        filhos = i.find_elements_by_xpath('.//*')
        #        for j in filhos:
        #            print(j.get_attribute('outerHTML'))
        #            print(" ")
        #            try:
        #                j.click()
        #                sleep(1)
        #                if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
        #                    driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")
        #            except:
        #                print("Não foi possível clicar em: ", j.get_attribute('innerHTML'), j.get_attribute('outerHTML'))

        #print(len(elem_div))
        #for webElement in elem_div:
        #    try:
        #        webElement.click()
        #    except:
        #        print("Não foi possível clicar em: ", webElement.get_attribute('innerHTML'), webElement.get_attribute('outerHTML'), webElement.is_displayed())

        #elementos = driver.find_elements_by_css_selector("body *")
        #print(len(elementos))

        #for webElement in elementos:  # Percorremos o vetor de elementos
        #    childs = webElement.find_elements_by_css_selector(" *")
        #    for i in range(len(childs)):
        #        try:
        #            childs[i].send_keys("teste")
        #        except:
        #            print("Não foi possível enviar letras ao elemento div")
        #        try:
        #            childs[i].click()
        #            print("Clicou em: " + childs[i].text)
        #        except:
        #            print("Não foi possível clicar no elemento div")
        #
        #        if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
        #            driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/calendarios.html")

teste = Teste(driver)
teste.dispara_eventos() #Realiza o disparo dos eventos
sleep(3)
driver.quit()