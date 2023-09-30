# Autor: Giseldo Neo
# nome do projeto: gitlab-org/gitlab

import os

diretorio = os.getcwd() + "/extractor/gitlab-2"
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

nome = "saida.json"

saida= "{}/{}".format(diretorio, nome)

url = 'https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/issues?id=gitlab-org%2Fgitlab&order_by=created_at&page=3&per_page=100&sort=desc&state=closed&weight=Any&with_labels_details=false'

token_antigo = 'glpat-dXUy6-AP5pmMfj857Jor'
token = 'SUBSTITUA PELO SEU TOKEN'

pagina = """ curl -X 'GET' '{}' -H 'accept: application/json' -H 'Private-Token: {}' >> {} """.format(url, token, saida)

os.system(pagina)