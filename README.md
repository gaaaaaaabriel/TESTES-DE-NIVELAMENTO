# TESTES-DE-NIVELAMENTO
Teste Técnico – Extração de Dados de PDF

Criei três arquivos Python com as seguintes funções:

   1° Download do PDF – Obtém o arquivo diretamente da internet.

   2° Extração dos dados – Processa o PDF e salva os dados em um arquivo CSV.

   3° Compactação – Gera uma pasta ZIP contendo o arquivo .CSV final.


Busquei orientação de um professor da faculdade para aprofundar meu conhecimento sobre funções de download. Este projeto está diretamente relacionado ao conteúdo aprendido na disciplina Descoberta de Conhecimento em Banco de Dados, onde estamos estudando raspagem de dados neste semestre.

Execução do codigo: 

comando 1 -> python download_pdfs.py

comando 2 -> python extrair_dados_pdf.py

comando 3 -> python compacta_zip.py

porque utilizar um ambiente virtual?
pesquisei sobre como outra pessoa conseguirira rodar o meu codigo, sem precisar ficar baixando as dependencias (as vezes pode faltar algunmas rs)



PARA RODAR A INTERFACE, PASSO A PASSO:

1° verificar os caminhos dos arquivos na função -> server.py
   o meu esta assim: C:\Users\gabri\vaga_emprego\backend\etapa_3\downloads\Relatorio_cadop.csv

2° entrar na pasta correta, o fim dela sera -> cd backend/etapa_4

3° rodar o comando -> uvicorn server:app --reload

4° testar no postman, a url é essa (ja esta com o endpoint definido) -> http://localhost:8000/buscar_operadoras?query=unimed

5° caso o seu localhost esteja em uma porta diferente que a da minha, lembresse de mudar ela tambem no arquivo -> frontend/interface/src/api.js

6° apos verificar todos os arquivos acima, é só rodar o comando dentro do arquivo correto, que é -> cd frontend/interface

COMANDO PARA RODAR A INTERFACE -> npm run dev

