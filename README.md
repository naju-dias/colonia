# Sistema Inteligente da Colônia

Sistema em Python que organiza os dados de uma colônia, toma decisões automáticas, prevê a energia eólica e analisa o uso de energia.

## Como funciona
- `dados.py`: guarda os dados em dicionários (sistema -> subsistema) e listas, e calcula geração e consumo totais.
- `decisoes.py`: regras de decisão (ex.: energia < 50 e consumo alto -> modo economia) e análise de geração x consumo. Suporte à vida nunca é desligado.
- `previsao.py`: regressão linear simples (reta y = a*x + b) feita à mão, sem bibliotecas.
- `main.py`: junta tudo e mostra o resultado.

## Como rodar
```
python main.py
```

## Exemplo de entrada e saída
```
=== Análise de energia ===
Geração: 45 | Consumo: 70
ALERTA: consumo maior que geração

=== Decisão ===
Entrada: energia = 40 , consumo = 70
Saída: ALERTA: reduzir consumo
Desligar: ['laboratorio', 'logistica']

=== Previsão ===
Entrada: vento = 11
Saída: previsão de energia ≈ 27.5
```
