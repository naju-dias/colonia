def decidir(energia, consumo):
    # regra combinada vem primeiro (é a mais grave)
    if energia < 50 and consumo > 80:
        return "ALERTA CRÍTICO: ativar modo economia"
    elif energia < 50:
        return "ALERTA: reduzir consumo"
    else:
        return "OK: energia em nível normal"


def analisar_energia(geracao, consumo):
    if consumo > geracao:
        return "ALERTA: consumo maior que geração"
    elif geracao > consumo:
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "OK: geração e consumo equilibrados"


def sistemas_para_desligar(consumos):
    # prioridade: suporte à vida nunca desliga, não essenciais sim
    desligar = []
    for nome in consumos:
        if not consumos[nome]["essencial"]:
            desligar.append(nome)
    return desligar