import requests
import logging
from datetime import date
from ingestion.janelas import gerar_janelas


logger = logging.getLogger(__name__)

URL_BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"


def buscar_janela(codigo: int, data_inicial: date, data_final: date) -> list[dict]:
    url = URL_BASE.format(codigo=codigo)
    params = {
        "formato": "json",
        "dataInicial": data_inicial.strftime("%d/%m/%Y"),
        "dataFinal": data_final.strftime("%d/%m/%Y"),
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
    except requests.HTTPError as e:
        logger.error("SGS %s falhou: %s | resposta: %s", codigo, e, e.response.text)
        raise
    return r.json()

def buscar_serie(
    codigo: int, inicio: date, fim: date, anos_por_janela: int = 5
) -> list[dict]:
    resultado: list[dict] = []
    for data_ini, data_fim in gerar_janelas(inicio, fim, anos_por_janela):
        logger.info("SGS %s: buscando %s a %s", codigo, data_ini, data_fim)
        dados = buscar_janela(codigo, data_ini, data_fim)
        resultado.extend(dados)
    return resultado