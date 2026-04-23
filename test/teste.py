from src.main import gerar_cnpj_alfanumerico

def test_tamanho_do_cnpj_gerado():
    """Garante que o CNPJ gerado tem exatamente 14 caracteres."""
    cnpj = gerar_cnpj_alfanumerico()
    assert len(cnpj) == 14


def test_formato_do_cnpj_gerado():
    """Verifica se os 12 primeiros caracteres são alfanuméricos e os 2 últimos são números."""
    cnpj = gerar_cnpj_alfanumerico()

    base = cnpj[:12]
    dvs = cnpj[12:]

    assert base.isalnum() is True
    assert dvs.isdigit() is True


def test_retorno_e_uma_string():
    """Verifica se o retorno da função é do tipo texto (str)."""
    cnpj = gerar_cnpj_alfanumerico()
    assert isinstance(cnpj, str)