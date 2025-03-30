import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

caminho_base = "C:/Users/gabri/vaga_emprego/etapa_3/downloads"


# conf do seu banco
DB_HOST = 'localhost'  #  seu host
DB_USER = 'root'  #  seu usuário
DB_PASS = 'Gabriel.46139989809'  #  sua senha
DB_NAME = 'TesteTrabalho'  # seu banco de dados


#rpecisei criar uma função para formatar as datas, a maioria estava 
# vindo assim -> "2024-07-01", mas 1 arquivo veio assim -> 01/10/2023
def converter_data(data):
    try:
        if '-' in data:  # Formato YYYY-MM-DD
            return pd.to_datetime(data, format='%Y-%m-%d').date()
        elif '/' in data:  # Formato DD/MM/YYYY
            return pd.to_datetime(data, format='%d/%m/%Y').date()
    except Exception:
        return None  # Retorna None se não conseguir converter


def importar_csv(caminho_arquivo):
    try:
        print(f"Importando {caminho_arquivo}...")
        
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', dtype=str)
        
        df.columns = [col.strip() for col in df.columns]
        
        df['DATA'] = df['DATA'].apply(converter_data)
        
        # tirando a ',' para colocar '.' e convertendo para float
        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.', regex=False).astype(float)
        df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.', regex=False).astype(float)
        
        engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
        
        df.to_sql('extrato', con=engine, if_exists='append', index=False)
        
        print(f"Arquivo {caminho_arquivo} importado")
    except Exception as e:
        print(f"Erro ao importar {caminho_arquivo}: {e}")

def processar_pastas():
    for ano in os.listdir(caminho_base):
        caminho_ano = os.path.join(caminho_base, ano)
        if os.path.isdir(caminho_ano):  # Verifica se é uma pasta
            print(f"Processando pasta: {caminho_ano}")
            for trimestre in os.listdir(caminho_ano):
                caminho_trimestre = os.path.join(caminho_ano, trimestre)
                if os.path.isdir(caminho_trimestre):  # Verifica se é uma pasta
                    for arquivo in os.listdir(caminho_trimestre):
                        if arquivo.endswith(".csv"):
                            caminho_arquivo = os.path.join(caminho_trimestre, arquivo)
                            importar_csv(caminho_arquivo)


processar_pastas()

