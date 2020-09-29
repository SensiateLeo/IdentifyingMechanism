#Código do mecanismo Reconhecedor integrado com o mecanismo Identificador (CIC)
#desenvolvido como parte da extenção do projeto
#"Uma ferramenta para identificação automática de componentes dinâmicos em Rich Internet Applications"
#FAPESP - Processo 2018/06322-3

###### BIBLIOTECAS ######
from selenium import webdriver
from time import sleep

###### CLASSES e FUNÇÕES ######
#Declaração da classe de mecanismo Identificador e suas funções
class Identificador:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def dispara_teclado(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            elemento.click()
            elemento.send_keys("01/01/2020")
            sleep(0.5)
            teclado = 1
        except:
            teclado = 0

        return teclado

    def dispara_clique(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            elemento.click()
            sleep(0.5)
            clique = 1
        except:
            clique = 0

        return clique

    def clique(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        try:
            elemento.click()
            sleep(0.5)
        except:
            return

        return

    def propriedades(self, caminho, arquivo):
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

    def propriedades_numericas(self, objeto, arquivo):

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

    def encontra_filhos(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filhos = elemento.find_elements_by_xpath('.//*')
        #for child in filhos:
            #print(child.get_attribute('outerHTML'))
        return len(filhos)

    def retorna_filho(self, caminho):
        driver = self.driver
        elemento = driver.find_element_by_xpath(caminho)
        filho = elemento.find_element_by_xpath('.//*')
        # for child in filhos:
        # print(child.get_attribute('outerHTML'))
        return filho

    def encontra_elementos(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")
        # print("Foram encontrados", len(elementos_pag), "elementos inicialmente na página")

        return len(elementos_pag)

    def retorna_elementos(self):
        driver = self.driver

        elementos_pag = driver.find_elements_by_css_selector("body > *")

        return elementos_pag

    def tira_foco(self):
        driver= self.driver
        stop = driver.find_element_by_tag_name("h1")
        stop.click()


###### INÍCIO DO CÓDIGO ######

#Abre o arquivo da base de dados
base_dados =  open('dados.txt', 'a+')
base_dados.write('\n')

#Inicia pegando as informações do usuário
#Processo é guiado!
PROMPT_1 = "Digite o site a ser analisado: "  # PROMPT_1 é o site
PROMPT_2 = "Digite o Xpath (caminho) do widget a ser reconhecido: "   # PROMPT_2 é o caminho do widget
PROMPT_3 = "Qual o tipo de widget será analisado? (Calendar, Menu, Dropdown, Time...): "

#Recebe as entradas do usuário
site = str(input(PROMPT_1))
xpath = str(input(PROMPT_2))
tipo = str(input(PROMPT_3))

#Guarda as informações recebidas na base
base_dados.write(site+',')
base_dados.write(xpath+',')
base_dados.write(tipo+',')

print("\nComponente Reconhecedor está executando...")
print("Extraindo características do elemento ", xpath)

#Instancia o Webdriver e acessa a URL informada
recon = webdriver.Firefox()
recon.implicitly_wait(30)
recon.get(site)

mecanismo = Identificador(recon)

#Extrai as propriedades iniciais do elemento indicado pelo usuário
mecanismo.propriedades(xpath,base_dados)

print("Extraiu propriedades!")

#Elemento pode receber cliques?
mouse = mecanismo.dispara_clique(xpath)
mecanismo.tira_foco()
base_dados.write(str(mouse)+",")

#Determina se o elemento possui nós filhos
filhos = mecanismo.encontra_filhos(xpath)
base_dados.write(str(filhos)+',')

#Caso existam nós filhos, armazena as propriedades numéricas desses filhos
#Tamanho e posição, e tags "netas"
if (filhos > 0):
    filho = mecanismo.retorna_filho(xpath)
    mecanismo.propriedades_numericas(filho, base_dados)
#Caso o elemento não tenha nós filhos, é marcado como não tendo e o número de tags netas é colocado como 0
else:
    for i in range(21):
        base_dados.write(str(0)+',')

#Analisa se o elemento é dinâmico através de uma interação com o mesmo
#Ou seja, verifica se a interação insere novos nós na DOM dinamicamente
dinamico = 0
elem = mecanismo.encontra_elementos()
mecanismo.clique(xpath)
num_elem = mecanismo.encontra_elementos()

#Se o elemento for dinâmico, são extraídas as propriedades desse novo elemento da DOM
#Pega- se a posição e tamanho e o número de tags dos nós netos, bisnetos, etc...
if (num_elem > elem):
    dinamico = 1
    base_dados.write(str(dinamico) + ',')
    elementos = mecanismo.retorna_elementos()
    mecanismo.propriedades_numericas(elementos[elem], base_dados)
    num_elem = elem
#Caso a interação não insira novos elementos na DOM, o elemento é marcado como não dinâmico
#e seu número de nós netos é marcado como 0
else:
    for i in range(22):
        base_dados.write(str(0)+',')
sleep(2)
#Realiza um clique em um ponto não interagível da página, para remover o foco do elemento.
mecanismo.tira_foco()
#Encerra o mecanismo
recon.quit()

#Fecha o arquivo da base
base_dados.close()

print("\n")
print("Extração de características finalizada.")
print("\nOs dados foram armazenado em dados.txt")

