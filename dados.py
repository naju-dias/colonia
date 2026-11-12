# Dados da colônia organizados de forma hierárquica
colonia = {
    "energia": {
        "solar": {"geracao": 25},
        "eolica": {"geracao": 20},
        "reserva": 40,
    },
    "consumo": {
        "suporte_vida": {"valor": 30, "essencial": True},
        "laboratorio": {"valor": 25, "essencial": False},
        "logistica": {"valor": 15, "essencial": False},
    },
    "clima": {"vento": 11},
}

# Histórico para a previsão
vento = [8, 10, 12]
energia_eolica = [20, 25, 30]


def total_geracao():
    return colonia["energia"]["solar"]["geracao"] + colonia["energia"]["eolica"]["geracao"]


def total_consumo():
    total = 0
    for nome in colonia["consumo"]:
        total += colonia["consumo"][nome]["valor"]
    return total


def mostrar_hierarquia():
    for sistema in colonia:
        print(sistema)
        for sub in colonia[sistema]:
            print("  -", sub)