from src.main import app, gerar_cnpj_alfanumerico
from fastapi.testclient import TestClient #precisa disso pra conseguir abrir o /run

client = TestClient(app)

def is_cnpj_valido(cnpj: str) -> bool:
    #apoio
    if len(cnpj) != 14:
        return False

def test_tamanho_do_cnpj_gerado():
    #14 caracteres sem mascara
    cnpj = gerar_cnpj_alfanumerico()
    assert len(cnpj) == 14


def test_formato_do_cnpj_gerado():
    #Verifica se os 12 primeiros caracteres são alfanuméricos e os 2 últimos são números.
    cnpj = gerar_cnpj_alfanumerico()

    base = cnpj[:12]
    dvs = cnpj[12:]

    assert base.isalnum() is True
    assert dvs.isdigit() is True


def test_retorno_e_uma_string():
    #retono é string
    cnpj = gerar_cnpj_alfanumerico()
    assert isinstance(cnpj, str)


def test_api_run_default():
    #retorno OK
    response = client.get("/run")
    assert response.status_code == 200

    dados = response.json()
    assert isinstance(dados, list)
    assert len(dados) == 100

    # Valida pelo menos um dos itens gerados pela API
    assert is_cnpj_valido(dados[0]) is True


def test_api_run_quantidade_personalizada():
    #quantidade diferente
    response = client.get("/run?quantidade=5")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_api_run_quantidade_invalida_abaixo_minimo():
    #quantidade invalida
    response = client.get("/run?quantidade=0")
    assert response.status_code == 422  #deve retornar 422


def test_api_run_quantidade_invalida_acima_maximo():
    #quantidade invalida
    response = client.get("/run?quantidade=1001")
    assert response.status_code == 422