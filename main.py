import random
import string
import uvicorn
from typing import List
from fastapi import FastAPI, Query

app = FastAPI(
    title="Gerador de CNPJ Alfanumérico",
    description="API para geração de massa de dados seguindo o novo padrão da Receita Federal."
)


def gerar_cnpj_alfanumerico() -> str:
    """Gera um único CNPJ alfanumérico válido matematicamente. """
    caracteres = string.ascii_uppercase + string.digits
    base_cnpj = ''.join(random.choice(caracteres) for _ in range(12))

    def converter(c):
        return int(c) if c.isdigit() else ord(c) - 48

    # Cálculo do DV1
    valores = [converter(c) for c in base_cnpj]
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(v * p for v, p in zip(valores, pesos1))
    dv1 = 0 if (soma1 % 11) < 2 else 11 - (soma1 % 11)

    # Cálculo do DV2
    valores.append(dv1)
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(v * p for v, p in zip(valores, pesos2))
    dv2 = 0 if (soma2 % 11) < 2 else 11 - (soma2 % 11)

    return f"{base_cnpj}{dv1}{dv2}"


@app.get("/run", response_model=List[str])
async def get_cnpjs(quantidade: int = Query(default=10, ge=1, le=1000)):
    """
    Retorna uma lista de CNPJs alfanuméricos válidos.
    - **quantidade**: Número de itens desejados (padrão 10, máximo 1000).
    """
    return [gerar_cnpj_alfanumerico() for _ in range(quantidade)]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

