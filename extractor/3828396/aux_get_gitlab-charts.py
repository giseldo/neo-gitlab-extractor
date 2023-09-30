# Autor: Giseldo Neo
# Nome do projeto: gitlab-org/charts/gitlab

import os
from datetime import date

cwd = os.getcwd()
diretorio = cwd + "/extractor/gitlab-charts"
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# str(date.today())

nome_arquivo = "saida.json" 
arquivo_saida_json= "{}/{}".format(diretorio, nome_arquivo)

url_pagina = 'https://gitlab.com/gitlab-org/charts/gitlab/-/issues/?sort=created_asc&state=closed&weight=Any&with_labels_details=false'
url = 'https://gitlab.com/api/v4/projects/gitlab-org%2Fcharts%2Fgitlab/issues?id=gitlab-org%2Fcharts%2Fgitlab&order_by=created_at&&per_page=100&sort=desc&state=closed&weight=Any&with_labels_details=false'

token = 'SUBSTITUA PELO SEU TOKEN'
pagina = """ curl -X 'GET' '{}' -H 'accept: application/json' -H 'Private-Token: {}' >> {} """.format(url, token, arquivo_saida_json)

os.system(pagina)