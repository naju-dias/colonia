import dados
import decisoes
import previsao

print("=== Estrutura da colônia ===")
dados.mostrar_hierarquia()

geracao = dados.total_geracao()
consumo = dados.total_consumo()
reserva = dados.colonia["energia"]["reserva"]

print("\n=== Análise de energia ===")
print("Geração:", geracao, "| Consumo:", consumo)
print(decisoes.analisar_energia(geracao, consumo))

print("\n=== Decisão ===")
print("Entrada: energia =", reserva, ", consumo =", consumo)
print("Saída:", decisoes.decidir(reserva, consumo))
print("Desligar:", decisoes.sistemas_para_desligar(dados.colonia["consumo"]))

print("\n=== Previsão ===")
a, b = previsao.ajustar_reta(dados.vento, dados.energia_eolica)
v = dados.colonia["clima"]["vento"]
print("Entrada: vento =", v)
print("Saída: previsão de energia ≈", round(previsao.prever(a, b, v), 1))