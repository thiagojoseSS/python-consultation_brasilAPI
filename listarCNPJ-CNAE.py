import csv
import json

with open('json_resultados.json', 'r') as arq_json_resultados:
    json_resultados = json.load(arq_json_resultados)

array = []
for item in json_resultados:
    if str(item) != '404':
        # print(item['cnpj'], item['cnae_fiscal_descricao'])
        array.append([item['cnpj'], item['cnae_fiscal_descricao']])


with open('csv_resultados-CNPJ-CNAE.csv', 'w', newline='') as arq_csv_resultados:
    csv_resultados = csv.writer(arq_csv_resultados, delimiter=';')
    csv_resultados.writerows(array)
