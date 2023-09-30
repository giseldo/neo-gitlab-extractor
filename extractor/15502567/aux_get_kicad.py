# Autor: Giseldo Neo
# Nome do projeto: tezos/tezos/
# https://gitlab.com/kicad/code/kicad/-/issues/?sort=created_asc&state=closed&weight=Any&first_page_size=100

import os
import time

diretorio = os.getcwd() + "\extractor\src_kicad\json_export"
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

pagina = 1
nome_arquivo = "teste-saida-pag-{}.json".format(pagina) 
arquivo_saida_json= "{}\{}".format(diretorio, nome_arquivo)

nome_projeto = 'kicad%2Fcode%2Fkicad'
per_page = 100
url = 'https://gitlab.com/api/v4/projects/{}/issues?id={}&order_by=created_at&page={}&per_page={}&sort=desc&state=closed&weight=Any&with_labels_details=false'.format(nome_projeto, nome_projeto, pagina, per_page)

token = 'SUBSTITUA PELO SEU TOKEN'
pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)

os.system(pagina)

# for i in range(2, 34):
#     pagina = i
#     nome_arquivo = "teste-saida-pag-{}.json".format(pagina) 
#     arquivo_saida_json= "{}\{}".format(diretorio, nome_arquivo)

#     nome_projeto = 'kicad%2Fcode%2Fkicad'
#     per_page = 100
#     url = 'https://gitlab.com/api/v4/projects/{}/issues?id={}&order_by=created_at&page={}&per_page={}&sort=desc&state=closed&weight=Any&with_labels_details=false'.format(nome_projeto, nome_projeto, pagina, per_page)

#     token = 'SUBSTITUA PELO SEU TOKEN'
#     pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)
#     os.system(pagina)
#     time.sleep(5)