import re


def validar_cnpj(cnpj):
    # Remover caracteres não numéricos
    cnpj = re.sub(r'\D', '', cnpj)

    # Verificar se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Lista dos pesos para o cálculo dos dígitos verificadores
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def calcular_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Calcular os dois dígitos verificadores
    digito1 = calcular_digito(cnpj, pesos1)
    digito2 = calcular_digito(cnpj + digito1, pesos2)

    # Verificar se os dígitos calculados coincidem com os dígitos verificadores do CNPJ
    return cnpj[-2:] == digito1 + digito2

