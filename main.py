import random
import string

def gerar_cnpj_alfanumerico():
    # 1. Conjunto de caracteres permitidos para os 12 primeiros dígitos (Base + Filial)
    # Segundo a Receita, letras maiúsculas e números
    caracteres = string.ascii_uppercase + string.digits

    # Gera os 12 primeiros caracteres aleatoriamente
    base_cnpj = ''.join(random.choice(caracteres) for _ in range(12))

    # 2. Função de conversão (ASCII - 48) para cálculo do dígito
    def converter(c):
        if c.isdigit():
            return int(c)
        return ord(c) - 48

    # 3. Cálculo do Primeiro Dígito Verificador (DV1)
    valores = [converter(c) for c in base_cnpj]
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma1 = sum(v * p for v, p in zip(valores, pesos1))
    resto1 = soma1 % 11
    dv1 = 0 if resto1 < 2 else 11 - resto1

    # 4. Cálculo do Segundo Dígito Verificador (DV2)
    valores.append(dv1)
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma2 = sum(v * p for v, p in zip(valores, pesos2))
    resto2 = soma2 % 11
    dv2 = 0 if resto2 < 2 else 11 - resto2

    # Retorna o CNPJ completo (12 alfanuméricos + 2 numéricos)
    return f"{base_cnpj}{dv1}{dv2}"

def gerar_massa_testes(quantidade):
    cnpjs = []
    for _ in range(quantidade):
        cnpjs.append(gerar_cnpj_alfanumerico())
    return cnpjs


# --- Execução ---
try:
    qtd = int(input("Quantos CNPJs alfanuméricos você deseja gerar? "))
    if qtd <= 0:
        print("Por favor, insira um número maior que zero.")
    else:
        lista_cnpjs = gerar_massa_testes(qtd)

        print(f"\n--- Lista de {qtd} CNPJs Gerados ---")
        for i, cnpj in enumerate(lista_cnpjs, 1):
            # Formatação opcional para exibição (sem máscara, pois o novo padrão é variado)
            print(f"{i:02d}. {cnpj}")

except ValueError:
    print("Erro: Digite um número inteiro válido.")