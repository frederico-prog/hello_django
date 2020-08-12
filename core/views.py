from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} tem {idade} anos.<h1>')


def soma(request, v1, v2):
    soma = v1 + v2
    return HttpResponse(f'<h2>A soma entre {v1} e {v2} é igual a {soma}<h2>')


def multiplicacao(request, v1, v2):
    mult = v1 * v2
    return HttpResponse(f'<h2>O produto entre {v1} e {v2} é igual a {mult}<h2>')


def divisao(request, v1, v2):
    try:
        div = v1 / v2
        return HttpResponse(f'<h2>A divisão entre {v1} e {v2} é igual a {div}<h2>')
    except Exception as e:
        return HttpResponse(f'Por favor, procurar o administrado do sistema. ERRO: {e}')
    except ZeroDivisionError:
        return HttpResponse('<h1>Dvisão por ZERO não existe!<h1>')


def subtracao(request, v1, v2):
    sub = v1 - v2
    return HttpResponse(f'<h2>A subtração entre {v1} e {v2} é igual a {sub}<h2>')
