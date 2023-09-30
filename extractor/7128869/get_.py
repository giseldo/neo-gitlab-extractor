import os
from datetime import date
import time
import os
import pandas as pd

def colect_page(id_projeto, pagina):
    
    diretorio = os.getcwd() + "/extractor/{}/json_export".format(id_projeto)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    nome_arquivo = "saida-pag-{}.json".format(pagina) 
    arquivo_saida_json= "{}/{}".format(diretorio, nome_arquivo)

    per_page = 100
    state='closed'
    url = 'https://gitlab.com/api/v4/projects/{}/issues?&order_by=created_at&page={}&per_page={}&sort=desc&state={}&weight=Any&with_labels_details=false'.format(id_projeto, pagina, per_page, state)

    token = 'SUBSTITUA PELO SEU TOKEN'
    pagina = """ curl -X "GET" "{}" -H "accept: application/json" -H "Private-Token: {}" >> {} """.format(url, token, arquivo_saida_json)
    #print(pagina)
    os.system(pagina)

def juntar(id_projeto):
    diretorio_ = os.getcwd() + "/extractor/{}/json_export".format(id_projeto)
    filenames_ = []
    for diretorio, subpastas, arquivos in os.walk(diretorio_):
        for arquivo in arquivos:
            filenames_.append(str(os.path.join(diretorio, arquivo)))

    df_total = pd.DataFrame()
    for s in filenames_:
        print(s)
        f = open(s, encoding="utf8") 
        df = pd.read_json(f)
        df_total = pd.concat([df_total, df])
    
    df_total.to_json(diretorio_ + "/{}.json".format(id_projeto), orient = 'records')
    print(diretorio_ + "/final.json")

if __name__ == "__main__":
    
    id_projeto = 7128869
    
    # for i in range(1, 6):
    #     pagina = i
    #     colect_page(id_projeto, pagina)
    #     time.sleep(3)
    
    juntar(id_projeto)