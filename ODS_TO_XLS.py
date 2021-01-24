from pandas_ods_reader import read_ods
import pandas as pd
# NÚMERO DE ARQUIVOS:
Arq = 9

# NOME DA PLANILHA FINAL:
Planilha = "Homicídio Simples"



# INÍCIO DO CÓDIGO, NÃO ALTERE AS LINHAS ABAIXO
N1 = "Procedimentos("
N2 = ").ods"

Planilha_Final = read_ods("Procedimentos.ods", 1, headers=False)

i = 1
while i<=Arq-1:
    Planilha_1 = read_ods(N1+str(i)+N2, 1, headers=False)
    frame = [Planilha_Final,Planilha_1]
    Planilha_Final = pd.concat(frame)
    i = i+1

Planilha_Final.reset_index();
Planilha_Final.columns = ['Número MP', 'Procedimento','Unidade','Assunto']
Planilha_Final.to_excel(Planilha + ".xlsx");

print("Planilha criada com sucesso!")
