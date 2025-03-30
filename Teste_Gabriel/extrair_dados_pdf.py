import fitz 
import pandas as pd #mainipular os dados


#esse cara faz nada mais além de 
#extrair os dados de um pdf
def extrair_dados_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    dados = [] 

    #paginas por paginas do pdf
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  
        texto = page.get_text('text') 
        dados.append(texto)

    return dados

# salvar os dados em CSV
def salvar_dados_csv(dados, arquivo_csv):
    df = pd.DataFrame(dados)
    df.to_csv(arquivo_csv, index=False)
    print(f"Dados salvos com sucesso em {arquivo_csv}")


pdf_file = 'anexo_I.pdf'
dados = extrair_dados_pdf(pdf_file)
salvar_dados_csv(dados, 'dados_extraidos.csv')
