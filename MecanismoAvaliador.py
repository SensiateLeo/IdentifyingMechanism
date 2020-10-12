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

###### CLASSES e FUNÇÕES ######
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

    def obterPropriedadesGerais(self, caminho, arquivo):
        driver = self.driver
        calendario = driver.find_element_by_xpath(caminho)

        # site com lista de atributos HTML: https://www.w3schools.com/tags/ref_attributes.asp
        if str(calendario.tag_name) != "":
            arquivo.write(str(calendario.tag_name)+'|')
        else:
            arquivo.write('None|')

        if str(str(calendario.get_attribute('outerHTML'))) != "":
            arquivo.write(str(calendario.get_attribute('outerHTML'))+'|')
        else:
            arquivo.write('None|')

        if (str(calendario.get_attribute('class')) == ""):
            arquivo.write('None|')
        else:
            arquivo.write(str(calendario.get_attribute('class')) + '|')

        if str(calendario.get_attribute('id')) != "":
            arquivo.write(str(calendario.get_attribute('id'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('name')) != "":
            arquivo.write(str(calendario.get_attribute('name'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('type')) != "":
            arquivo.write(str(calendario.get_attribute('type'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('href')) != "":
            arquivo.write(str(calendario.get_attribute('href'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('role')) != "":
            arquivo.write(str(calendario.get_attribute('role'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('form')) != "":
            arquivo.write(str(calendario.get_attribute('form'))+',')
        else:
            arquivo.write('None,')

        #NO CASO DE INPUTS
        if str(calendario.get_attribute('checked')) != "":
            arquivo.write(str(calendario.get_attribute('checked'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('style')) != "":
            arquivo.write(str(calendario.get_attribute('style'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('tabindex')) != "":
            arquivo.write(str(calendario.get_attribute('tabindex'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('text')) != "":
            arquivo.write(str(calendario.get_attribute('text'))+',')
        else:
            arquivo.write('None,')

        if str(calendario.get_attribute('color')) == "":
            arquivo.write('None,')
        else:
            arquivo.write(str(calendario.get_attribute('color')) + ',')

        tamanho = list(calendario.size.values())
        tam_x = tamanho[0]
        tam_y = tamanho[1]
        arquivo.write(str(tam_x)+',')
        arquivo.write(str(tam_y) + ',')

        loc = list(calendario.location.values())
        loc_x = loc[0]
        loc_y = loc[1]
        arquivo.write(str(loc_y) + ',')
        arquivo.write(str(loc_x) + ',')

    def obterPropriedadesNumericas(self, objeto, arquivo):

        tamanho = list(objeto.size.values())
        tam_x = tamanho[0]
        tam_y = tamanho[1]
        arquivo.write(str(tam_x)+',')
        arquivo.write(str(tam_y) + ',')

        loc = list(objeto.location.values())
        loc_x = loc[0]
        loc_y = loc[1]
        arquivo.write(str(loc_y) + ',')
        arquivo.write(str(loc_x) + ',')

        #lista de tags HTML: https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element
        divs = 0
        li = 0
        p = 0
        col = 0
        table = 0
        tbody = 0
        td = 0
        th = 0
        thead = 0
        tfoot = 0
        tr = 0
        button = 0
        form = 0
        input = 0
        textarea = 0
        menu = 0
        menuitem = 0
        filhos = objeto.find_elements_by_xpath('.//*')
        for i in filhos:
            if(str(i.tag_name) == "div"):
                divs = divs + 1
            if (str(i.tag_name) == "p"):
                p = p + 1
            if (str(i.tag_name) == "li"):
                li = li + 1
            if (str(i.tag_name) == "menu"):
                menu = menu + 1
            if (str(i.tag_name) == "menuitem"):
                menuitem = menuitem + 1
            if (str(i.tag_name) == "input"):
                input = input + 1
            if (str(i.tag_name) == "button"):
                button = button + 1
            if (str(i.tag_name) == "form"):
                form = form + 1
            if (str(i.tag_name) == "textarea"):
                textarea = textarea + 1
            if (str(i.tag_name) == "col"):
                col = col + 1
            if (str(i.tag_name) == "table"):
                table = table + 1
            if (str(i.tag_name) == "thead"):
                thead = thead + 1
            if (str(i.tag_name) == "tbody"):
                tbody = tbody + 1
            if (str(i.tag_name) == "tfoot"):
                tfoot = tfoot + 1
            if (str(i.tag_name) == "th"):
                th = th + 1
            if (str(i.tag_name) == "tr"):
                tr = tr + 1
            if (str(i.tag_name) == "td"):
                td = td + 1

        arquivo.write(str(divs) + ',')
        arquivo.write(str(li) + ',')
        arquivo.write(str(p) + ',')
        arquivo.write(str(col) + ',')
        arquivo.write(str(table) + ',')
        arquivo.write(str(tbody) + ',')
        arquivo.write(str(td) + ',')
        arquivo.write(str(th) + ',')
        arquivo.write(str(thead) + ',')
        arquivo.write(str(tfoot) + ',')
        arquivo.write(str(tr) + ',')
        arquivo.write(str(button) + ',')
        arquivo.write(str(form) + ',')
        arquivo.write(str(input) + ',')
        arquivo.write(str(textarea) + ',')
        arquivo.write(str(menu) + ',')
        arquivo.write(str(menuitem) + ',')

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

        if str(calendario.get_attribute('class')):
            print("Classe: " + str(calendario.get_attribute('class')))

        if str(calendario.get_attribute('id')):
            print("ID: " + str(calendario.get_attribute('id')))

        if str(calendario.get_attribute('name')):
            print("Nome: " + str(calendario.get_attribute('name')))

        if str(calendario.get_attribute('type')):
            print("Tipo: " + str(calendario.get_attribute('type')))

        if str(calendario.get_attribute('href')):
            print("HREF: " + str(calendario.get_attribute('href')))

        if str(calendario.get_attribute('text')):
            print("Texto/Placeholder: " + str(calendario.get_attribute('text')) + "/" + str(calendario.get_attribute('placeholder')))

        print("\nPadrões WAI-ARIA propostos pela W3C:")

        print("Padrões WAI-ARIA estabelecidos para calendários:")
        #Choose Date Button || Date Picker Dialog: Calendar Navigation Buttons || Date Picker Dialog: Date Grid
        if str(calendario.tag_name) == "button":
            if str(calendario.get_attribute('aria-label')):
                print("Aria-label: " + str(calendario.get_attribute('aria-label')))
            if str(calendario.get_attribute('tabindex')):
                print("Tab index: " + str(calendario.get_attribute('tabindex')))
            if str(calendario.get_attribute('aria-selected')):
                print("Aria-selected: " + str(calendario.get_attribute('aria-selected')))

        #Date Picker Dialog
        if str(calendario.tag_name) == "div":
            if str(calendario.get_attribute('role')):
                print("Role: " + str(calendario.get_attribute('role')))
            if str(calendario.get_attribute('aria-modal')):
                print("Aria-modal: " + str(calendario.get_attribute('aria-modal')))
            if str(calendario.get_attribute('aria-labelledby')):
                print("Aria-labelledby: " + str(calendario.get_attribute('aria-labelledby')))
            if str(calendario.get_attribute('aria-live')):
                print("Aria-live: " + str(calendario.get_attribute('aria-live')))

        #Date Picker Dialog: Calendar Navigation Buttons
        if str(calendario.tag_name) == "h2":
            if str(calendario.get_attribute('aria-live')):
                print("Aria-live: " + str(calendario.get_attribute('aria-live')))

        #Date Picker Dialog: Date Grid
        if str(calendario.tag_name) == "table":
            if str(calendario.get_attribute('role')):
                print("Role: " + str(calendario.get_attribute('role')))
            if str(calendario.get_attribute('aria-labelledby')):
                print("Aria-labelledby: " + str(calendario.get_attribute('aria-labelledby')))

        # if str(calendario.get_attribute('role')) != "":
        #     arquivo.write(str(calendario.get_attribute('role')) + ',')
        # else:
        #     arquivo.write('None,')
        #
        #
        # # NO CASO DE INPUTS
        # if str(calendario.get_attribute('checked')) != "":
        #     arquivo.write(str(calendario.get_attribute('checked')) + ',')
        # else:
        #     arquivo.write('None,')

        # lista de tags HTML: https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element
        # divs = 0
        # li = 0
        # p = 0
        # col = 0
        # table = 0
        # tbody = 0
        # td = 0
        # th = 0
        # thead = 0
        # tfoot = 0
        # tr = 0
        # button = 0
        # form = 0
        # input = 0
        # textarea = 0
        # menu = 0
        # menuitem = 0
        # filhos = calendario.find_elements_by_xpath('.//*')
        # for i in filhos:
        #     if (str(i.tag_name) == "div"):
        #         divs = divs + 1
        #     if (str(i.tag_name) == "p"):
        #         p = p + 1
        #     if (str(i.tag_name) == "li"):
        #         li = li + 1
        #     if (str(i.tag_name) == "menu"):
        #         menu = menu + 1
        #     if (str(i.tag_name) == "menuitem"):
        #         menuitem = menuitem + 1
        #     if (str(i.tag_name) == "input"):
        #         input = input + 1
        #     if (str(i.tag_name) == "button"):
        #         button = button + 1
        #     if (str(i.tag_name) == "form"):
        #         form = form + 1
        #     if (str(i.tag_name) == "textarea"):
        #         textarea = textarea + 1
        #     if (str(i.tag_name) == "col"):
        #         col = col + 1
        #     if (str(i.tag_name) == "table"):
        #         table = table + 1
        #     if (str(i.tag_name) == "thead"):
        #         thead = thead + 1
        #     if (str(i.tag_name) == "tbody"):
        #         tbody = tbody + 1
        #     if (str(i.tag_name) == "tfoot"):
        #         tfoot = tfoot + 1
        #     if (str(i.tag_name) == "th"):
        #         th = th + 1
        #     if (str(i.tag_name) == "tr"):
        #         tr = tr + 1
        #     if (str(i.tag_name) == "td"):
        #         td = td + 1

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

#Inicia pegando as informações do usuário
#Procedimento é guiado!
PROMPT_1 = "Digite a URL do site a ser analisado: "  # PROMPT_1 é o site
PROMPT_2 = "Digite o Xpath (caminho) do widget a ser avaliado: "   # PROMPT_2 é o caminho do widget
PROMPT_3 = "Qual o tipo de widget será avaliado? (Calendar, Menu, Dropdown, Time...): "
PROMPT_4 = "É necessário rolar a página para acessar o wigdet? (1 ou 0): "

#Recebe as entradas do usuário
site = str(input(PROMPT_1))
xpath = str(input(PROMPT_2))
tipo = str(input(PROMPT_3))
scroll = input(PROMPT_4)
scrollValor = 0

if(scroll == "1"):
    PROMPT_5 = "Quantos pixels é necessário scrollar?: "
    scrollValor = input(PROMPT_5)

#Guarda as informações recebidas na base
# base_dados.write(site+',')
# base_dados.write(xpath+',')
# base_dados.write(tipo+',')

print("\nMecanismo Avaliador está executando...")
print("Extraindo características do elemento ", xpath)

#Instancia o Webdriver e acessa a URL informada
avaliador = webdriver.Firefox()
avaliador.implicitly_wait(30)
avaliador.get(site)

mecanismo = Avaliador(avaliador)

#Obtém as propriedades iniciais do elemento indicado pelo usuário
mecanismo.obterPropriedadesAcessibilidade(xpath)

print("Extraiu propriedades!")

#Elemento pode receber cliques?
if(scroll == "1"):
    mouse = mecanismo.disparaCliqueComScroll(xpath, scrollValor)
else:
    mouse = mecanismo.disparaClique(xpath)

#mecanismo.removerFoco()
#base_dados.write(str(mouse)+",")

#Determina se o elemento possui nós filhos
# filhos = mecanismo.encontrarElementosFilhos(xpath)
# base_dados.write(str(filhos)+',')

#Caso existam nós filhos, armazena as propriedades numéricas desses filhos
#Tamanho e posição, e tags "netas"
# if (filhos > 0):
#     filho = mecanismo.retornarElementoFilho(xpath)
#     mecanismo.obterPropriedadesNumericas(filho, base_dados)
# #Caso o elemento não tenha nós filhos, é marcado como não tendo e o número de tags netas é colocado como 0
# else:
#     for i in range(21):
#         base_dados.write(str(0)+',')

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
#Realiza um clique em um ponto não interagível da página, para remover o foco do elemento.
# mecanismo.removerFoco()
#Encerra o mecanismo
avaliador.quit()

#Fecha o arquivo da base
# base_dados.close()

print("\n")
print("Extração de características finalizada.")
#print("\nOs dados foram armazenado em dados.txt")

