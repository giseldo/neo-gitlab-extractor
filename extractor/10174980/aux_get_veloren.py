# Autor: Giseldo Neo
# Nome do projeto: veloren/veloren
# url do projeto: https://gitlab.com/veloren/veloren/-/issues/?sort=updated_desc&state=closed&weight=Any&first_page_size=100

import os
from datetime import date

dir_projeto = 'src_veloren'
diretorio = os.getcwd() + "/extractor/{}/json_export".format(dir_projeto)
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

pagina = 3
nome_arquivo = "saida-pag-{}.json".format(pagina) 
arquivo_saida_json= "{}/{}".format(diretorio, nome_arquivo)

nome_projeto = 'veloren%2Fveloren'
per_page = 100
state='closed'
url = 'https://gitlab.com/api/v4/projects/{}/issues?id={}&order_by=created_at&page={}&per_page={}&sort=desc&state={}&weight=Any&with_labels_details=false'.format(nome_projeto, nome_projeto, pagina, per_page, state)

token = 'SUBSTITUA PELO SEU TOKEN'
pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)

os.system(pagina)