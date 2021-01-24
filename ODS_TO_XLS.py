from pandas_ods_reader import read_ods
import pandas as pd
import os

# NOME DA PLANILHA FINAL:
Planilha = "Homicídio Simples"



# INÍCIO DO CÓDIGO, NÃO ALTERE AS LINHAS ABAIXO
N1 = "Procedimentos("
N2 = ").ods"

arquivosOds = []
dirname = '.'

def print_nomes(Lista):
    print("Arquivos unificados:")
    for item in Lista:
        print(">",item)

for name in os.listdir(dirname):
    path = os.path.join(dirname, name)
    if os.path.isfile(path):
        if name.endswith('.ods'):
            arquivosOds.append(name)
    else:
        walk(path)

print_nomes(arquivosOds)

Planilha_Final = read_ods(arquivosOds[0], 1, headers=False)
arquivosOds.remove(arquivosOds[0])

for arq in arquivosOds:
    Planilha_1 = read_ods(arq, 1, headers=False)
    frame = [Planilha_Final,Planilha_1]
    Planilha_Final = pd.concat(frame)


Planilha_Final.reset_index();
Planilha_Final.columns = ['Número MP', 'Procedimento','Unidade','Assunto']
Planilha_Final.to_excel(Planilha + ".xlsx")

print("\nPlanilha criada com sucesso!")

