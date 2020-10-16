#Projeto baseado na implementação dos mecanismos Reconhecedor/ Avaliador (CIC)
#desenvolvidos como parte da extenção do projeto
#"Uma ferramenta para identificação automática de componentes dinâmicos em Rich Internet Applications"
#FAPESP - Processo 2018/06322-3

#O objetivo deste projeto é analisar quali/quantitativamente a acessibilidade de widgets calendários
#Os resultados obtidos através detes mecanismos serão comparados aos resultados de ferramentas
#utilizadas para a avaliação de acessibilidade, a fim de comprovar a viabilidade do mesmo

###### BIBLIOTECAS ######
from selenium import webdriver
from time import sleep

#Declaração da classe de mecanismo Avaliador e suas funções
class Avaliador:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def disparaEventoTeclado(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            elemento.click()
            elemento.send_keys("10/12/2020")
            sleep(0.5)
            teclado = 1
        except:
            teclado = 0

        return teclado

    def disparaClique(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            elemento.click()
            sleep(0.5)
        except:
            print("O elemento não recebe eventos de clique")
            return

        print("O elemento recebe eventos de clique")
        return

    def disparaCliqueComScroll(self, caminho, valor):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            js = 'scrollBy(0,' + str(valor) + ')'
            driver.execute_script(js)
            elemento.click()
            sleep(0.5)
        except:
            print("O elemento não recebe eventos de clique")
            return

        print("O elemento recebe eventos de clique")
        return

    def obterPropriedadesAcessibilidade(self, caminho):
        driver = self.driver
        calendario = driver.find_element_by_xpath(caminho)

        print("\nLocalização do elemento na página:")
        loc = list(calendario.location.values())
        loc_x = loc[0]
        loc_y = loc[1]
        print("Posição y: " + str(loc_y))
        print("Posição x: " + str(loc_x) + "\n")

        print("Tamanho do elemento na página:")
        tamanho = list(calendario.size.values())
        tam_x = tamanho[0]
        tam_y = tamanho[1]
        print("Tamanho x: " + str(tam_x))
        print("Tamanho y: " + str(tam_y) + "\n")
        #arquivo.write(str(tam_x) + ',')
        #arquivo.write(str(tam_y) + ',')

        # site com lista de atributos HTML: https://www.w3schools.com/tags/ref_attributes.asp
        #site com exemplo de como deve ser implementado um calendário acessível: https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/datepicker-dialog.html
        if str(calendario.tag_name) != "":
            print("Tag do elemento: " + str(calendario.tag_name))

        print("Atributos do elemento:")
        if str(str(calendario.get_attribute('outerHTML'))):
            print("HTML: " + str(calendario.get_attribute('outerHTML')))

        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            calendario)

        temRole = 0

        for x, y in attrs.items():
            print(str(x) + ': ' + '"' + str(y) + '"')
            if (x == "role"):
                temRole = 1
                valorRole = str(y)

        if(temRole == 1):
            print('Elemento possui atributo "Role": ' + valorRole)
        else:
            print('Elemento não possui atributo "Role"')

    def obterPropriedadesAcessibilidadeElementoFilho(self, calendario):
        driver = self.driver

        print("\nLocalização do elemento na página:")
        loc = list(calendario.location.values())
        loc_x = loc[0]
        loc_y = loc[1]
        print("Posição y: " + str(loc_y))
        print("Posição x: " + str(loc_x) + "\n")

        print("Tamanho do elemento na página:")
        tamanho = list(calendario.size.values())
        tam_x = tamanho[0]
        tam_y = tamanho[1]
        print("Tamanho x: " + str(tam_x))
        print("Tamanho y: " + str(tam_y) + "\n")
        #arquivo.write(str(tam_x) + ',')
        #arquivo.write(str(tam_y) + ',')

        # site com lista de atributos HTML: https://www.w3schools.com/tags/ref_attributes.asp
        #site com exemplo de como deve ser implementado um calendário acessível: https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/datepicker-dialog.html

        if str(calendario.tag_name) != "":
            print("Tag do elemento: " + str(calendario.tag_name))

        print("Atributos do elemento:")
        if str(str(calendario.get_attribute('outerHTML'))):
            print("HTML: " + str(calendario.get_attribute('outerHTML')))

        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            calendario)

        temRole = 0

        for x, y in attrs.items():
            print(str(x) + ': ' + '"' + str(y) + '"')
            if (x == "role"):
                temRole = 1
                valorRole = str(y)

        if(temRole == 1):
            print('Elemento possui atributo "Role": ' + valorRole)
        else:
            print('Elemento não possui atributo "Role"')


    def encontrarElementosFilhos(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filhos = elemento.find_elements_by_xpath('.//*')
        #for child in filhos:
            #print(child.get_attribute('outerHTML'))
        return len(filhos)

    def retornarElementoFilho(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filho = elemento.find_element_by_xpath('.//*')
        # for child in filhos:
        # print(child.get_attribute('outerHTML'))
        return filho

    def retornarElementosFilhos(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filhos = elemento.find_elements_by_xpath('.//*')
        # for child in filhos:
        # print(child.get_attribute('outerHTML'))
        return filhos

    def encontrarElementosPagina(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")
        # print("Foram encontrados", len(elementos_pag), "elementos inicialmente na página")

        return len(elementos_pag)

    def retornarElementosPagina(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")

        return elementos_pag

    def removerFoco(self):
        driver= self.driver
        stop = driver.find_element_by_tag_name("h1")
        stop.click()


###### INÍCIO DO CÓDIGO ######

#Abre o arquivo onde serão guardados os dados
# base_dados =  open('dados.txt', 'a+')
# base_dados.write('\n')

scrollValor = 0
loop = 1

#Inicia pegando as informações do usuário
#Procedimento é guiado!
PROMPT_1 = "Digite a URL do site a ser analisado: "  # PROMPT_1 é o site
PROMPT_2 = "Digite o Xpath (caminho) do widget a ser avaliado: "  # PROMPT_2 é o caminho do widget
PROMPT_3 = "É necessário rolar a página para acessar o wigdet? (1 ou 0): "
PROMPT_4 = "Quantos pixels é necessário scrollar?: "
PROMPT_5 = "\nDeseja indicar um novo elemento para análise? (1 ou 0): "


site = str(input(PROMPT_1))

#Guarda as informações recebidas na base
# base_dados.write(site+',')
# base_dados.write(xpath+',')
# base_dados.write(tipo+',')

#Instancia o Webdriver e acessa a URL informada
driver = webdriver.Firefox()
driver.get(site)

avaliador = Avaliador(driver)

while loop:

    xpath = str(input(PROMPT_2))
    scroll = input(PROMPT_3)

    if (scroll == "1"):
        scrollValor = input(PROMPT_4)

    print("\nMecanismo Avaliador está executando...")
    print("Extraindo características do elemento ", xpath)

    #Obtém as propriedades iniciais do elemento indicado pelo usuário
    avaliador.obterPropriedadesAcessibilidade(xpath)

    print("Extraiu propriedades!")

    #Elemento pode receber cliques?
    if(scroll == "1"):
        mouse = avaliador.disparaCliqueComScroll(xpath, scrollValor)
    else:
        mouse = avaliador.disparaClique(xpath)

    #mecanismo.removerFoco()

    #Determina se o elemento possui nós filhos
    numFilhos = avaliador.encontrarElementosFilhos(xpath)

    #Caso existam nós filhos, armazena as propriedades numéricas desses filhos
    #Tamanho e posição, e tags "netas"
    if (numFilhos > 0):
        filhos = avaliador.retornarElementosFilhos(xpath)
        for i in range(len(filhos)):
            avaliador.obterPropriedadesAcessibilidadeElementoFilho(filhos[i])

    loop = int(input(PROMPT_5))

    #Analisa se o elemento é dinâmico através de uma interação com o mesmo
    #Ou seja, verifica se a interação insere novos nós na DOM dinamicamente
    # dinamico = 0
    # elem = mecanismo.encontrarElementosPagina()
    # mecanismo.disparaClique(xpath)
    # num_elem = mecanismo.encontrarElementosPagina()

    #Se o elemento for dinâmico, são extraídas as propriedades desse novo elemento da DOM
    #Pega- se a posição e tamanho e o número de tags dos nós netos, bisnetos, etc...
    # if (num_elem > elem):
    #     dinamico = 1
    #     base_dados.write(str(dinamico) + ',')
    #     elementos = mecanismo.retornarElementosPagina()
    #     mecanismo.obterPropriedadesNumericas(elementos[elem], base_dados)
    #     num_elem = elem
    #Caso a interação não insira novos elementos na DOM, o elemento é marcado como não dinâmico
    #e seu número de nós netos é marcado como 0
    # else:
    #     for i in range(22):
    #         base_dados.write(str(0)+',')
    # sleep(2)

#Encerra o mecanismo
driver.quit()

#Fecha o arquivo da base
# base_dados.close()

print("\n")
print("Extração de características finalizada.")
#print("\nOs dados foram armazenado em dados.txt")

