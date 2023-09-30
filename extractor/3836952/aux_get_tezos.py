# Autor: Giseldo Neo
# Nome do projeto: tezos/tezos/
# url do projeto: https://gitlab.com/tezos/tezos/-/issues/?sort=created_asc&state=closed&weight=Any&first_page_size=20

import os
from datetime import date

diretorio = "/extractor/src_tezos/json_export"
if not os.path.exists(diretorio):
     os.makedirs(diretorio)

pagina = 2
nome_arquivo = "saida-pag-{}.json".format(pagina) 
arquivo_saida_json= "{}/{}".format(diretorio, nome_arquivo)

nome_projeto = 'tezos%2Ftezos'
per_page = 100
url = 'https://gitlab.com/api/v4/projects/{}/issues?id={}&order_by=created_at&page={}&per_page={}&sort=desc&state=closed&weight=Any&with_labels_details=false'.format(nome_projeto, nome_projeto, pagina, per_page)

token = 'SUBSTITUA PELO SEU TOKEN'
pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)

#os.system(pagina)