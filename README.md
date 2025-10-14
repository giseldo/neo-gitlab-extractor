# NEO GITLAB EXTRACTOR

Resumo
-----
Projeto para extrair issues de projetos GitLab (fechados) que usam o atributo "weight". O repositório contém scripts para baixar páginas via API (curl) e para concatenar os JSONs gerados em um único arquivo para análise.

Estrutura principal
-------------------
- extractor/ — scripts por projeto que coletam páginas e unem JSONs (ex.: [extractor/6206924/get_.py](extractor/6206924/get_.py)).
- dataset/json/ — JSONs finais gerados para uso/backup (ex.: [dataset/json/10152778.json](dataset/json/10152778.json)).
- notebooks — notebooks para análise e concatenação (ex.: [extractor/278964/concat_json.ipynb](extractor/278964/concat_json.ipynb)).

Como funciona
-------------
1. Coleta de páginas
   - Cada pasta em `extractor/<id>/` tem um script com a função de coletar páginas por curl: por exemplo [`extractor.6206924.get_.colect_page`](extractor/6206924/get_.py).
   - Antes de executar, substitua a string do token por um token válido no arquivo (campo `token = 'SUBSTITUA PELO SEU TOKEN'`).
   - Exemplo de execução (linha de comando):
     - python extractor/6206924/get_.py
     - Os arquivos são gravados em `extractor/<id>/json_export/saida-pag-<n>.json`.

2. União / concatenação de JSONs
   - Os scripts possuem a função `juntar` que coleta todos os arquivos em `json_export`, faz concat com pandas e grava um JSON final. Ex.: [`extractor.734943/get_.py`](extractor/734943/get_.py) ou genericamente [`extractor.12584701/get_.py`](extractor/12584701/get_.py) — ver [`extractor.734943.get_.juntar`](extractor/734943/get_.py).
   - Executar o script do projeto grava `extractor/<id>/json_export/<id>.json`.

3. Notebooks de análise
   - Há notebooks que mostram concatenações e análises (ex.: [extractor/278964/concat_json.ipynb](extractor/278964/concat_json.ipynb), [extractor/15502567/concat_json_tezos.ipynb](extractor/15502567/concat_json_tezos.ipynb)).
   - Use Jupyter / VSCode para abrir e rodar as células.

Boas práticas e dicas
---------------------
- Sempre troque o placeholder do token por um token com permissões de leitura.
- Certifique-se que a pasta `extractor/<id>/json_export` exista (os scripts normalmente criam).
- Se houver problemas de encoding com pandas, abrir os arquivos com `encoding="utf8"` (implementado nos scripts).
- Logs simples são escritos com print() nos scripts para acompanhar progresso.

Arquivos e símbolos úteis
-------------------------
- Scripts de coleta (ex.: [extractor/6206924/get_.py](extractor/6206924/get_.py)) e função [`extractor.6206924.get_.colect_page`](extractor/6206924/get_.py).
- Funções de concat/merge em vários projetos: [`extractor.734943.get_.juntar`](extractor/734943/get_.py), [`extractor.12584701.get_.juntar`](extractor/12584701/get_.py), etc.
- Notebooks de concat/inspeção: [extractor/278964/concat_json.ipynb](extractor/278964/concat_json.ipynb).

Contribuição
-----------
Abrir issues ou PRs com melhorias: padronizar scripts, extrair funções comuns, parametrizar token via variável de ambiente ou arquivo .env.

Licença
-------
Arquivo original sem licença explícita — tratar conforme necessidade do projeto.

