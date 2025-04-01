import os # manipula caminhos de arquivos CRIAÇÃO DAS PASTAS
import requests # http
from bs4 import BeautifulSoup  # type: ignore
import sys

def baixar_arquivo(url, destino):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, 'wb') as f: # abre a pasta
            f.write(response.content) 
        print(f"Arquivo {destino} baixado")
    else:
        print(f"Falha ao baixar: {url}. Código de status: {response.status_code}")

# ESSE CARA ELE FAZ UMA BUSCA MAIS DETALHADA, BUSCANDO POR ARQUIVOS .ZIP
def obter_links_download(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)  # esse cara vai atras dos links que em html é <a>
        return [link['href'] for link in links if link['href'].endswith('.zip')] #filtra os links pegando somente os que tem .zip
    else:
        print(f"Falha ao acessar a página: {url}")
        return []


def baixar_arquivos_do_ano(ano):
    url_base = f"https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/{ano}/"
    print(f"Acessando: {url_base}")
    
    pasta_ano = os.path.join("downloads", str(ano)) 
    os.makedirs(pasta_ano, exist_ok=True)  # acaso a pasta com o ano não existe ele cria uam 
    
    links = obter_links_download(url_base)

    #extraindo o nome dos arquivos que no caso é com .zip
    if links:
        for link in links:
            if not link.startswith('http'):
                arquivo_url = f"{url_base}{link}" 
            else:
                arquivo_url = link  

            nome_arquivo = link.split('/')[-1]  
            caminho_destino = os.path.join(pasta_ano, nome_arquivo)  # caminho onde sera salvo 
            baixar_arquivo(arquivo_url, caminho_destino) # dowload
    else:
        print(f"Não foram encontrados arquivos para o ano {ano}.")

if len(sys.argv) > 1:
    ano = sys.argv[1]  
    baixar_arquivos_do_ano(ano)
else:
    print("forneça o ano como argumento. Exemplo: python script.py 2023")


