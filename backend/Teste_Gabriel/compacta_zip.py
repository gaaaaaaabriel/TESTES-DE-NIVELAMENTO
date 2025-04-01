import zipfile


def compactar_csv(arquivo_csv, arquivo_zip):
    with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
        zipf.write(arquivo_csv, arcname='dados_extraidos.csv')
    print(f"Arquivo compactado: {arquivo_zip}")

#CSV
compactar_csv('dados_extraidos.csv', 'Teste_Gabriel.zip')
