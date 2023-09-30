# Autor: Giseldo Neo
# Nome do projeto: freepascal.org/lazarus/lazarus
# url do projeto: https://gitlab.com/freepascal.org/lazarus/lazarus/-/issues/?sort=updated_desc&state=closed&weight=Any&first_page_size=100
# Mudar  

import os
from datetime import date
import os
import json
import pandas as pd

def colect_page(dir_projeto, nome_projeto, pagina):
    
    diretorio = os.getcwd() + "/extractor/{}/json_export".format(dir_projeto)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    nome_arquivo = "saida-pag-{}.json".format(pagina) 
    arquivo_saida_json= "{}/{}".format(diretorio, nome_arquivo)

    per_page = 100
    state='closed'
    url = 'https://gitlab.com/api/v4/projects/{}/issues?id={}&order_by=created_at&page={}&per_page={}&sort=desc&state={}&weight=Any&with_labels_details=false'.format(nome_projeto, nome_projeto, pagina, per_page, state)

    token = 'SUBSTITUA PELO SEU TOKEN'
    pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)
    #print(pagina)
    os.system(pagina)

def juntar():
    diretorio = os.getcwd() + "/extractor/{}/json_export".format(dir_projeto)
    filenames_ = []
    for diretorio, subpastas, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            filenames_.append(str(os.path.join(diretorio, arquivo)))

    df_total = pd.DataFrame()
    for s in filenames_:
        print(s)
        f = open(s, encoding="utf8") 
        df = pd.read_json(f)
        df_total = pd.concat([df_total, df])
    
    df_total.to_json(diretorio + "\\final.json", orient = 'records')

if __name__ == "__main__":
    nome_projeto = 'freepascal.org%2Flazarus%2Flazarus'
    dir_projeto = 'src_lazarus'
    pagina = 3
    #colect_page(dir_projeto, nome_projeto, pagina)
    #juntar()