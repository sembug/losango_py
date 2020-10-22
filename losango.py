def monta_losango(tamanho):
    largura = tamanho * 2 + 1
    numeros = intervalo(tamanho)
    s = []
    for i in numeros:
        s.append(linha(i, largura))
    return "\n".join(s)


def linha(n, largura):
    return centralizar(text(intervalo(n)), largura)


def intervalo(n):
    return (*range(n), *range(n, -1, -1))


def text(numeros):
    return "".join((str(n) for n in numeros))


def centralizar(texto, largura, separador="."):
    margem = (largura - len(texto)) // 2
    return str(separador) * margem + texto + str(separador) * margem
