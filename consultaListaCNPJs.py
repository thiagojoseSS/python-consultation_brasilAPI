import json
import re
from time import sleep

import consulta_brasilAPI_cnpj
import AVL_Tree
import read_csvs
import carregarLista
import validarCNPJ


def novo_arq():
    new_arq = read_csvs.ReadCSV()
    new_arq.localizar_csv()
    return new_arq.get_caminho()


def ler_linhas(caminho):
    new_array = carregarLista.LoadList(caminho)
    return new_array.loadCaminho()


def clean_cnpj(cnpj_in):
    result = re.sub(r'\D', '', cnpj_in)
    return int(result)


avl = AVL_Tree.AVLTree()
root = None

lista_cnpjs = ler_linhas(novo_arq())

with open('json_resultados.json', 'r') as arq_json_resultados:
    json_resultados = json.load(arq_json_resultados)

for item in json_resultados:
    if str(item) != '404':
        chave = int(item['cnpj'])
        valor = item
        root = avl.insert(root, chave, valor)

x = 1
for idx, cnpj in enumerate(lista_cnpjs):
    if validarCNPJ.validar_cnpj(cnpj):
        temp_cnpj_avl = avl.search(root, clean_cnpj(cnpj))
        if temp_cnpj_avl is None:
            api_cnpj = consulta_brasilAPI_cnpj.ConsultarCNPJ()
            result = api_cnpj.get_url_with_cnpj(cnpj)
            root = avl.insert(root, result[0], result[1])
            json_resultados.append(result[1])
            print(f"Consultado: {idx}")
            if str(result[1]) == '404':
                print(f"CNPJ: {cnpj} ---- Não foi encontrado na API!")
            else:
                print(f"CNPJ: {cnpj} ---- Consultado com Sucesso!")
            if (x % 10) == 0:
                print("Pausa de 1 segundo")
                sleep(1)
            if x == 100:
                print("Pausa de 100 segundo")
                sleep(100)
                x = 1
            x += 1
            with open('json_resultados.json', 'w') as arq_json_resultados:
                json.dump(json_resultados, arq_json_resultados, indent=4)

            with open('json_resultados.json', 'r') as arq_json_resultados:
                json_resultados = json.load(arq_json_resultados)

