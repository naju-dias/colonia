def media(lista):
    return sum(lista) / len(lista)


def ajustar_reta(x, y):
    # mínimos quadrados: y = a*x + b
    mx = media(x)
    my = media(y)
    soma_xy = 0
    soma_xx = 0
    for i in range(len(x)):
        soma_xy += (x[i] - mx) * (y[i] - my)
        soma_xx += (x[i] - mx) ** 2
    a = soma_xy / soma_xx
    b = my - a * mx
    return a, b


def prever(a, b, x):
    return a * x + b