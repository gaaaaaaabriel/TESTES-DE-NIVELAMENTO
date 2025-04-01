from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import unicodedata

# Cria a instância do FastAPI
app = FastAPI()

# ja utilizei essse cara em outro projeto web para consegui acessar imagens que ficava dentro de um servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  # permite todos os tipos de requisições 
    allow_headers=["*"],
)

caminho_csv = r"C:\Users\gabri\vaga_emprego\backend\etapa_3\downloads\Relatorio_cadop.csv" # caminho do meu pc, precisa mudar 


df_operadoras = pd.read_csv(caminho_csv, sep=";", encoding="latin1", dtype=str).fillna("")

# Criei essa função para descodificar alguns caracterespeciais
def corrigir_codificacao(texto):
    if isinstance(texto, str):
        texto = texto.encode('latin1').decode('utf-8', 'ignore')
        return unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    return texto


@app.get("/buscar_operadoras")
def buscar_operadoras(query: str = Query(..., description="Nome ou parte do nome da operadora")):

    resultado = df_operadoras[df_operadoras['Nome_Fantasia'].str.contains(query, case=False, na=False)]

    #aqui eu corrijo antes de exibir, utilizando a função que criei    
    resultado_corrigido = resultado.applymap(corrigir_codificacao)
    
    
    return resultado_corrigido.to_dict(orient="records") # retorna no formato json

