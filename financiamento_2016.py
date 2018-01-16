estado = 'ac'
candidato = 'Antonio Barbosa de Sousa'
dindin = '10'

# Importação de todas as bibliotecas que vão ser utilizadas
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
    # Gambiarra para conseguir mostrar quando o nome não corresponde a um candidato.
    verificacao_candidato = ['candidato existe']
    # Lista com os doadores e total doado somente quando este for igual ou maior que o definido pelo usuário.
    if valor[registro["Nome do doador (Receita Federal)"]] >= float(dindin):
        doadores.append([registro["Nome do doador (Receita Federal)"].title(), valor[registro["Nome do doador (Receita Federal)"]]])

for linha in doadores:
    empresas = []
    pessoa = linha[0]
    pessoa = pessoa.lower().replace(' ', '-')
    url = f'https://www.empresascnpj.com/s/socio/{pessoa}'
    pagina = requests.get(url)
    
    
    from bs4 import BeautifulSoup
    sopa = BeautifulSoup(pagina.content, 'html.parser')

    teste_site = sopa.find('h1').text.strip()
    lista = sopa.find_all('li')
    
    if teste_site == 'Uso':
        empresas = ['fora do ar']
    else:
        for item in lista[:-3]:
            empresas.append({pessoa: item.get_text()})

# Mostra a resposta para o usuário
if verificacao_candidato == ['candidato existe']:
    if not doadores:
        print('O(A) candidato(a) não teve doações de pessoas físicas acima do valor indicado.')
    else: 
        if empresas == ['fora do ar']:
            print('Infelizmente o site de onde extraímos os dados não está permitindo mais consultas. Tente novemente dentro de alguns dias ou tente usar outro computador.')
        else:
            for linha in doadores:
                if empresas:
                    break
                else:
                    print(f'{linha[0]}, que doou R${linha[1]:.2f} para a campanha de {candidato.title()}, é sócio(a) das seguintes empresas:')
                    for empresa in empresas:
                        print(f'- {empresa} \n')
else:
    print('Este candidato não foi encontrado. Verifique se você digitou o nome COMPLETO e corretamente e se o estado escolhido corresponde ao estado da cidade onde ele se candidatou.')

arquivo.close()
