import requests

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
# url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

arquivo_pdf = 'anexo_I.pdf' #nome do arquivo que tra no enunciado


response = requests.get(url)
with open(arquivo_pdf, 'wb') as file:
    file.write(response.content)

print(f"PDF baixado: {arquivo_pdf}")



