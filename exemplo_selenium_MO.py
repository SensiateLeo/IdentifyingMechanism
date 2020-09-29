from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Teste:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def dispara_eventos(self):
        driver = self.driver

        elementos_div = driver.find_elements_by_tag_name("div")  # Cria um vetor com todos os elementos com a tag "div"
        for webElement in elementos_div:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento div")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento div")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

        elementos_a = driver.find_elements_by_tag_name("a")  # Cria um vetor com todos os elementos com a tag "div"
        for webElement in elementos_a:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento a")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento a")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

        elementos_img = driver.find_elements_by_tag_name("img")  # Cria um vetor com todos os elementos com a tag "div"
        for webElement in elementos_img:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento img")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento img")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

        elementos_form = driver.find_elements_by_tag_name("form")  # Cria um vetor com todos os elementos com a tag "div"
        for webElement in elementos_form:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento form")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento form")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

        elementos_input = driver.find_elements_by_tag_name("input")  # Cria um vetor com todos os elementos com a tag "div"
        for webElement in elementos_input:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento input")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento input")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

        elementos_button = driver.find_elements_by_tag_name("button")  # Cria um vetor com todos os elementos com a tag "button"
        for webElement in elementos_button:  # Percorremos o vetor de elementos
            try:
                webElement.send_keys("teste")
            except:
                print("Não foi possível enviar letras ao elemento button")
            try:
                webElement.click()
                print("Clicou em: " + webElement.text)
            except:
                print("Não foi possível clicar no elemento button")

            if (driver.current_url != "http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html"):
                driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

            if (webElement.get_attribute("type") == "submit" and webElement.get_attribute("id") == "opener"):
                webElement.send_keys("teste")
                abrir = driver.find_element_by_id("opener")
                fechar = driver.find_element_by_css_selector(".ui-button-icon")
                ActionChains(driver).click(abrir).click(fechar).perform()

        # Clicar no calendario
        #calendario = driver.find_element_by_id("datepicker")  # Elemento que abre o calendário
        #calendario.send_keys("teste")
        #sleep(2)
        #calendario.click()
        #mes = driver.find_element_by_css_selector(".ui-icon-circle-triangle-e")  # Botão que troca o mês do calendário
        #mes.click()
        #data = driver.find_element_by_xpath("//a[contains(.,'4')]")  # Botão que seleciona a data (dia/mes/ano)
        #data.click()

#Instancia o browser
driver = webdriver.Firefox()
driver.implicitly_wait(30)

#Script que configura/ inicia o MutationObserver
#poe = open("mutation_observer.js", "r")
#set_mut = poe.read()

#Script que configura/ inicia o MutationObserver
poe = open("M_O2.js", "r")
set_mut = poe.read()

#Script que captura os elementos que sofreram mutações
#pega = open("get_mutation.js", "r")
#get_mut = pega.read()

#Script que captura o tipo das mutações identificadas
#tipo = open("get_tipos.js", "r")
#tipo_mut = tipo.read()

#Acessa a página criada para teste
driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

teste = Teste(driver)
driver.execute_script(set_mut) #Ativa o mutationObserver
teste.dispara_eventos() #Realiza o disparo dos eventos
sleep(3)
#tipos_capt = driver.execute_script(tipo_mut) #Recupera o tipo das mutações identificadas
#targets = driver.execute_script(get_mut)  #Recupera as mutações identificadas

#i = 0

#Realiza o print das mutações juntamente com o tipo de mutação detectada
#while( i < targets.__len__()):
#    print("Elemento: ", targets[i], "\n")
#    i = i + 1

#Para visualizar de uma maneira mais clara as mutações e os elementos responsáveis por elas,
#acessar o console do browser ao fim da execução do teste

driver.quit() #Encerra o browser - está comentado para que o console do browser fique acessível

