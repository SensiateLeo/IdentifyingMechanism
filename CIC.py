from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Identificador:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def encontra_elementos(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")
       # print("Foram encontrados", len(elementos_pag), "elementos inicialmente na página")

        return len(elementos_pag)

    def retorna_elementos(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")

        return elementos_pag

    def dispara_eventos(self, elemento):
        driver = self.driver
        try:
            elemento.click()
            sleep(0.5)
        except:
            print("Elemento não clicavel!")

    def encontra_filhos(self, elemento):
        filhos = elemento.find_elements_by_xpath('.//*')
        for child in filhos:
           # print("Filho: ")
            print(child.get_attribute('outerHTML'))

    def tira_foco(self):
        driver=self.driver
        stop = driver.find_element_by_tag_name("h1")
        stop.click()

cic = webdriver.Firefox()
cic.implicitly_wait(30)
cic.get("https://jqueryui.com/datepicker/")
mecanismo = Identificador(cic)
elem = mecanismo.encontra_elementos()
elementos = mecanismo.retorna_elementos()

#Script que configura/ inicia o MutationObserver
poe = open("scripts/mutation_observer.js", "r")
set_mut = poe.read()

#Script que encerra o Mutation Observer
fecha = open("scripts/fecha_mo.js", "r")
fecha_mo = fecha.read()
saida = open('arquivo.txt','w')
dinamicos = 0
for i in range(elem):
    print("--------------------- Elemento", i, " -----------------------")
    print(elementos[i].get_attribute('outerHTML'))
    cic.execute_script(set_mut)  # Ativa o mutationObserver
    mecanismo.dispara_eventos(elementos[i])
    num_elem = mecanismo.encontra_elementos()
    if(num_elem>elem):
        dinamicos = dinamicos + 1
        elementos = mecanismo.retorna_elementos()
        mecanismo.dispara_eventos(elementos[elem])
        mecanismo.encontra_filhos(elementos[elem])
        num_elem = elem
    mecanismo.tira_foco()
    elementos = mecanismo.retorna_elementos()
    cic.execute_script(fecha_mo) # Encerra o mutationObserver
    print(' ')

#Script que captura os elementos que sofreram mutações
pega = open("scripts/get_mutation.js", "r")
get_mut = pega.read()
#Script que captura o tipo das mutações identificadas
tipo = open("scripts/get_tipos.js", "r")
tipo_mut = tipo.read()
tipos_capt = cic.execute_script(tipo_mut) #Recupera o tipo das mutações identificadas
targets = cic.execute_script(get_mut)  #Recupera as mutações identificadas
saida.close()
sleep(3)
cic.quit()
print("O número de elementos dinâmicos na página é: ", dinamicos)