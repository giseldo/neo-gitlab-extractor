import requests
import os
import time

url_original = "https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/issues?state=closed&weight=Any&per_page=100" # 19.764 / 100 = 197,64
project_name = "gitlab"

if not os.path.exists(project_name):
    os.makedirs(project_name)

def get_page(projeto, url, id):
    nome = str(projeto) + "_saida_" + str(id) + ".json"
    saida= "{}/{}".format(project_name, nome)
    pagina = """curl -X 'GET' '{}' -H 'accept: application/json' -H 'Private-Token: glpat-dXUy6-AP5pmMfj857Jor' >> {}""".format(url, saida)
    print("---- "+ pagina)
    os.system(pagina)

def get_max_pages(url):
    response = requests.head(url)
    total = response.headers['x-total']
    xtotalpages =  response.headers['x-total-pages']
    return total, xtotalpages

def get_next_url(url): 
    response = requests.head(url)
    links = response.headers['link']
    links_ant_prox_ult = links.split(",")
    df_dict = dict()

    for l in links_ant_prox_ult:
        ls = l.split(";")
        url_ = ls[0].replace("<", "").replace(">", "").replace(" ", "")
        typ = ls[1].replace("rel=", "").replace("\"","").replace(" ", "")
        df_dict[typ] = url_

    return df_dict["next"]


def main():
    print("Iniciou")
    #total, xtotalpages = get_max_pages(url)
    #print("total de itens: {}".format(total))
    #print("total de páginas: {}".format(xtotalpages))
    
    get_page(project_name, url_original, 0)

    next_url = url_original
    
    for x in range(1, int(198)):
        next_url = get_next_url(next_url)
        print(next_url)
        time.sleep(5)
        get_page("gitlab", next_url, x)

if __name__ == "__main__":
    main()



