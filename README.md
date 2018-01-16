# Quem financiou esse candidato?
Programa em Python que cruza nomes de pessoas físicas que financiaram um candidato com as empresas das quais ela é sócia.

Este programa foi desenvolvido como trabalho final para o MOOC "Introdução à Programação: Python para Jornalistas", ofericido pelo Knight Center for Journalism in the Americas.

Antes de usar o programa, é importante ter em mente as seguintes informações:
- O programa foi escrito por uma pessoa iniciante na linguagem Python e, portanto, ainda não possui um código tão limpo, além de depender de certas restrições de outros sites que ainda não tenho conhecimento sufuciente para resolver.
- O programa foi criado em Python3 e usa as bibliotecas csv, collections, requests e BeautifulSoup.
- O objetivo do programa é identificar quem financiou as campanhas eleitorais de cada candidato, com doações de pessoa física, e mostrar de quais empresas estas pessoas são sócias.
- O programa foi desenvolvido para funcionar somente com as eleições municipais de 2016.
- O programa funciona para candidados de qualquer cargo e de qualquer cidade do Brasil, mas por questões de rapidez, é necessário indicar o estado onde o candidato concorreu.
- O programa só funciona se o nome completo do candidato for indicado. Muitos candidados se idendificam com apelidos os nomes abreviados, mas o programa só aceitará o nome completo (com todos os sobrenomes).
- IMPORTANTE!! O programa solicita as informações sobre as empresas para o site "Empresas CNPJ". Como este site limita a quantidade de consultas por IP, o programa pode parar de funcionar por alguns dias.
