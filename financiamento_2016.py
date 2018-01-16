# Inputs do usuário
estado = input('Digite a sigla do estado desejado: ') # O estado é necessário para definir qual arquivo .csv deverá ser consultado. Existe um grande arquivo com os dados de todo o Brasil, mas sua consulta era bem mais demorada.
candidato = input('Digite o nome completo do candidato desejado: ')
dindin = input('Digite o valor mínimo de doação que a pessoa deve ter feito para entrar na verificação: ')

# Importação das bibliotecas que vão ser utilizadas
import csv
import collections
import requests

# Definição de variáveis e listas que serão usadas
valor = collections.Counter()
verificacao_candidato = []
doadores = []
estado = estado.upper()
arquivo_csv = f'receitas_candidatos_2016_{estado}.csv' # Define qual arquivo será aberto, de acordo com o estado escolhido pelo usuário.

# Abre o arquivo desejado e cria um leitor baseado na linha de cabeçalho do arquivo
arquivo = open(arquivo_csv, encoding='iso-8859-15')
leitor = csv.DictReader(arquivo, delimiter=';', lineterminator='\n') # O arquivo usa ';' para separar os valores, por isso precisamos definir o 'delimiter'

# Soma as doações de todos os doadores
for registro in leitor:
    dinheiro = registro["Valor receita"].replace(',', '.')
    if registro["Nome candidato"].upper() == candidato.upper():
        if len(registro["CPF/CNPJ do doador"]) == 11:
            valor[registro["Nome do doador (Receita Federal)"]] += float(dinheiro)

# Cria uma lista com os valores doador e total doado            
for registro["Nome do doador (Receita Federal)"] in valor:
    # Verifica se o nome dgitado corresponde a algum candidato do estado escolhido
    verificacao_candidato = ['candidato existe']
    # Cria lista com os doadores e total doado somente quando este for igual ou maior que o definido pelo usuário
    if valor[registro["Nome do doador (Receita Federal)"]] >= float(dindin):
        doadores.append([registro["Nome do doador (Receita Federal)"].title(), valor[registro["Nome do doador (Receita Federal)"]]])

# Mostra as respostas para o usuário

# Mostra se os valores colocados não tiveram resultados positivos
if verificacao_candidato == ['candidato existe']:
    if not doadores:
        print('O(A) candidato(a) não teve doações de pessoas físicas acima do valor indicado.')
    # Verifica se o limite de acessos ao site foi atingido
    else:
        for linha in doadores:
            empresas = []
            pessoa = linha[0]
            pessoa = pessoa.lower().replace(' ', '-')
            url = f'https://www.empresascnpj.com/s/socio/{pessoa}'
            pagina = requests.get(url)
    
            from bs4 import BeautifulSoup
            sopa = BeautifulSoup(pagina.content, 'html.parser')

            teste_site = sopa.find('h1').text.strip()
    
            if teste_site == 'Uso':
                empresas = ['fora do ar']
        if empresas == ['fora do ar']:
            print('Infelizmente o site de onde extraímos os dados não está permitindo mais consultas. Tente novemente dentro de alguns dias ou tente usar outro computador.')
        # Procura cada doador no site de sócios
        else:
            for linha in doadores:
                empresas = []
                pessoa = linha[0]
                pessoa = pessoa.lower().replace(' ', '-')
                url = f'https://www.empresascnpj.com/s/socio/{pessoa}'
                pagina = requests.get(url)
    
                from bs4 import BeautifulSoup
                sopa = BeautifulSoup(pagina.content, 'html.parser')
                
                lista = sopa.find_all('li')
                socio = sopa.find('p').text.strip()
                # Avisa quando o doador não é sócio de nenhuma empresa
                if socio != 'Mostrando 0 (zero) empresas.':
                    for item in lista[:-3]:
                        empresas.append(item.get_text())
                if not empresas:
                    print(f'{linha[0]}, que doou R${linha[1]:.2f} para a campanha de {candidato.title()}, não é sócio(a) de nenhuma empresa.')       
                # Mostra o nome de cada doador e as empresas que ele é sócio
                else:
                    print(f'{linha[0]}, que doou R${linha[1]:.2f} para a campanha de {candidato.title()}, é sócio(a) das seguintes empresas:')
                    for empresa in empresas:
                        print(f'- {empresa} \n')
# Mostra o resultado quando o nome digitado não corresponde a nenhum candidato do estado                 
else:
    print('Este candidato não foi encontrado. Verifique se você digitou o nome COMPLETO e corretamente e se o estado escolhido corresponde ao estado da cidade onde ele se candidatou.')

arquivo.close()

