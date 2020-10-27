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
        try:
            elemento = driver.find_element_by_xpath(caminho)
            elemento.click()
            sleep(0.5)
        except:
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

    def obterPropriedadesAcessibilidade(self, caminho, scroll):
        driver = self.driver

        js = 'scrollBy(0,' + str(scroll) + ')'
        driver.execute_script(js)

        calendario = driver.find_element_by_xpath(caminho)

        print("\nPosição e tamanho:")
        loc = list(calendario.location.values())
        loc_x = loc[0]
        loc_y = loc[1]
        print("Posição - y: " + str(loc_y) + "; x: " + str(loc_x))

        tamanho = list(calendario.size.values())
        tam_x = tamanho[0]
        tam_y = tamanho[1]
        print("Tamanho - x: " + str(tam_x) + "; y: " + str(tam_y))

        # site com lista de atributos HTML: https://www.w3schools.com/tags/ref_attributes.asp
        #site com exemplo de como deve ser implementado um calendário acessível: https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/datepicker-dialog.html
        # if str(calendario.tag_name) != "":
        #     print("Tag do elemento: " + str(calendario.tag_name))

        print("\nAtributos de acessibilidade do elemento:")
        # if str(str(calendario.get_attribute('outerHTML'))):
        #     print("HTML: " + str(calendario.get_attribute('outerHTML')))

        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            calendario)

        attRole = 0
        attAcessibilidade = 0

        for x, y in attrs.items():

            #print(str(x) + ': ' + '"' + str(y) + '"')

            if (x == "role"):
                attRole = 1
                print('Atributo "role": ' + str(y))

            if("aria" in str(x)):
                print("Atributo '" + str(x) + "': " + str(y))
                attAcessibilidade += 1

        if(attRole == 0 and attAcessibilidade == 0):
            print("Não foram encontrados atributos de acessibilidade")

        resumo = [attRole, attAcessibilidade]
        return resumo

    def obterPropriedadesAcessibilidadeElementoFilho(self, calendario):
        driver = self.driver

        # site com lista de atributos HTML: https://www.w3schools.com/tags/ref_attributes.asp
        #site com exemplo de como deve ser implementado um calendário acessível: https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/datepicker-dialog.html
        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            calendario)

        roles = 0
        atts = 0
        for x, y in attrs.items():
            # print(str(x) + ': ' + '"' + str(y) + '"')
            if (x == "role"):
                roles += 1
                print('Atributo "role": ' + str(y))

            if ("aria" in str(x)):
                print("Atributo '" + str(x) + "': " + str(y))
                atts += 1

        resumoFilho = [roles, atts]
        return resumoFilho

    def encontrarElementosFilhos(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filhos = elemento.find_elements_by_xpath('.//*')
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

loop = 1

#Inicia pegando as informações do usuário
#Procedimento é guiado!
PROMPT_1 = "Digite a URL do site a ser analisado: "  # PROMPT_1 é o site
PROMPT_2 = "É necessário rolar a página para acessar o wigdet? (1 ou 0): "
PROMPT_3 = "Quantos pixels é necessário scrollar?: "
PROMPT_4 = "É necessário clicar em algum elemento para acessar o wigdet? (1 ou 0): "
PROMPT_5 = "Digite o Xpath (caminho) do elemento ativador: "
PROMPT_6 = "Digite o Xpath (caminho) do widget a ser avaliado: "
PROMPT_7 = "\nDeseja indicar um novo elemento para análise? (1 ou 0): "

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
    scrollValor = "0"

    scroll = input(PROMPT_2)

    if (scroll == "1"):
        scrollValor = input(PROMPT_3)

    elemAtivador = input(PROMPT_4)

    if (elemAtivador == "1"):
        caminhoAtivador = input(PROMPT_5)
        avaliador.disparaClique(caminhoAtivador)

    xpath = str(input(PROMPT_6))

    print("\nMecanismo Avaliador está executando...")
    print("Extraindo características do elemento ", xpath)

    #Obtém as propriedades iniciais do elemento indicado pelo usuário
    resumoElemPai = avaliador.obterPropriedadesAcessibilidade(xpath, scrollValor)

    #mouse = avaliador.disparaClique(xpath)

    #mecanismo.removerFoco()

    #Determina se o elemento possui nós filhos
    numFilhos = avaliador.encontrarElementosFilhos(xpath)

    rolesFilhos = 0
    attAcessibilidadeFilhos = 0
    #Caso existam nós filhos, armazena as propriedades numéricas desses filhos
    #Tamanho e posição, e tags "netas"
    if (numFilhos > 0):
        print("\nAtributos acessibilidade dos elementos filhos: ")
        filhos = avaliador.retornarElementosFilhos(xpath)
        for i in range(len(filhos)):
            resumoElemFilho = avaliador.obterPropriedadesAcessibilidadeElementoFilho(filhos[i])
            rolesFilhos += resumoElemFilho[0]
            attAcessibilidadeFilhos += resumoElemFilho[1]

    print("\nResumo de Acessibilidade:")
    print("Elemento pai: \nAtt role = " + str(resumoElemPai[0]) + "\nAtts Acessibilidade: " + str(resumoElemPai[1]))
    print("\nElementos filhos: \nAtt role = " + str(rolesFilhos) + "\nAtts Acessibilidade: " + str(attAcessibilidadeFilhos))

    loop = int(input(PROMPT_7))

#Encerra o mecanismo
driver.quit()
print("\nAvaliação de características finalizada.")


