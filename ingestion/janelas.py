from datetime import date, timedelta

from dateutil.relativedelta import relativedelta


def gerar_janelas(
    inicio: date, fim: date, anos_por_janela: int = 5
) -> list[tuple[date, date]]:
    """Divide [inicio, fim] em janelas consecutivas, sem sobreposição e sem buracos."""
    if inicio > fim:
        raise ValueError(f"inicio ({inicio}) é posterior a fim ({fim})")
    if anos_por_janela < 1:
        raise ValueError("anos_por_janela deve ser >= 1")

    janelas: list[tuple[date, date]] = []
    cursor = inicio
    while cursor <= fim:
        fim_janela = min(
            cursor + relativedelta(years=anos_por_janela) - timedelta(days=1),
            fim,
        )
        janelas.append((cursor, fim_janela))
        cursor = fim_janela + timedelta(days=1)
    return janelas