import re

def validar_cnpj(cnpj):
    # 1. Limpeza: remove pontos, barras e traços, mantém apenas letras e números
    cnpj = re.sub(r'[^A-Z0-9]', '', cnpj.upper())

    if len(cnpj) != 14:
        return False, "O CNPJ deve ter 14 caracteres."

    # 2. Conversão de Alfanumérico para Numérico (Regra da Receita Federal)
    # Valor = Código ASCII do caractere - 48
    def converter_caractere(c):
        if c.isdigit():
            return int(c)
        return ord(c) - 48

    try:
        valores = [converter_caractere(c) for c in cnpj]
    except Exception:
        return False, "Erro ao processar caracteres do CNPJ."

    # 3. Cálculo do Primeiro Dígito Verificador (DV1)
    def calcular_dv(lista_valores, pesos):
        soma = sum(v * p for v, p in zip(lista_valores, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    dv1 = calcular_dv(valores[:12], pesos1)

    if valores[12] != dv1:
        return False, f"Primeiro dígito verificador inválido (esperado {dv1})."

    # 4. Cálculo do Segundo Dígito Verificador (DV2)
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    dv2 = calcular_dv(valores[:13], pesos2)

    if valores[13] != dv2:
        return False, f"Segundo dígito verificador inválido (esperado {dv2})."

    return True, "CNPJ válido!"


# --- Interface de Usuário ---
print("=== Validador de CNPJ (Novo Padrão Alfanumérico) ===")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Digite o CNPJ para validar: ").strip()

    if entrada.lower() == 'sair':
        print("Encerrando...")
        break

    sucesso, mensagem = validar_cnpj(entrada)

    if sucesso:
        print(f"✅ {mensagem}")
    else:
        print(f"❌ Erro: {mensagem}")
    print("-" * 30)