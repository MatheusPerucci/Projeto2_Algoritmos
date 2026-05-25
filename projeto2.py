import sys
import random
import string

def CadastroPedidos(pedidos, entregadores):
    id = GerarIDPedidos(pedidos)

    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")

    prioridade = ""
    while prioridade not in ["alto", "normal"]:
        prioridade = input("Qual a prioridade (Alto, Normal): ").strip().lower()

    tamanho = ""
    while tamanho not in ["pequeno", "medio", "grande"]:
        tamanho = input("Qual o tamanho (Pequeno, Medio, Grande): ").strip().lower()

    descricao = input("Descrição do pedido: ")

    status = "Pendente"

    entregador = EntregadorPedido(entregadores, tamanho)
    if entregador == "":
        print("Não temos entregadores no momento")
    
    dadosPedido = {
        'id': id,
        'nome': nome,
        'tamanho': tamanho,
        'endereco': endereco,
        'prioridade': prioridade,
        'descricao': descricao,
        'status': status,
        'entregador': entregador
    }

    pedidos.append(dadosPedido)

    print("Pedido cadastrado com sucesso!")
    print(pedidos)


def CadastroEntregadores(entregadores):
    id = GerarIDEntregador(entregadores)

    nome = input("Digite seu nome: ")
    veiculo = input("Digite seu veiculo: ").strip().lower()

    while veiculo not in ["moto", "carro", "van"]:
        veiculo = input("Digite seu veiculo (Moto, Carro, Van): ").strip().lower()
    
    if veiculo == "moto":
        disponibilidade = 3
    elif veiculo == "carro":
        disponibilidade = 6
    else:
        disponibilidade = 12

    idPedidos = []

    dadosEntregador = {
        'id': id,
        'nome': nome,
        'veiculo': veiculo,
        'idPedidos': idPedidos,
        'disponibilidade': disponibilidade
    }
    entregadores.append(dadosEntregador)


def AtualizacaoPedidos():
    print("3")


def ConsultaInformacoes():
    print("4")


def RelatoriosOperacionais():
    print("5")


def EntregadorPedido(entregadores, tamanho):
    if tamanho == "pequeno":
        espaco = 1
    elif tamanho == "medio":
        espaco = 2
    else: 
        espaco = 4

    for entregador in entregadores:
        if entregador['disponibilidade'] >= espaco:
            entregador['disponibilidade'] -= espaco
            return entregador['id']
    return ""

def GerarIDPedidos(pedidos):
    existe = True
    while existe:
        numero = random.randint(1, 999)
        letra = random.choice(string.ascii_uppercase)

        id = f'{letra}{numero:03d}'

        if len(pedidos) > 0:
            for pedido in pedidos:
                if pedido['id'] != id:
                    existe = False
                else: 
                    break
        else:
            existe = False
    return id

def GerarIDEntregador(entregadores):
    existe = True
    while existe:
        numero = random.randint(1, 9999)
        id = f'{numero:04d}'

        if len(entregadores) > 0:
            for entregador in entregadores:
                if entregador['id'] != id:
                    existe = False
                else:
                    break
        else:
            existe = False
    return id

def menu_principal(pedidos, entregadores):
    while True:
        num = int(input(
            "\n1 - Cadastro de Pedidos"
            "\n2 - Cadastro de Entregadores"
            "\n3 - Atualização de Pedidos"
            "\n4 - Consulta de Informações"
            "\n5 - Relatórios Operacionais"
            "\nOutro - Exit"
            "\nEscolha sua opção: "
        ))

        match num:
            case 1:
                CadastroPedidos(pedidos, entregadores)
            case 2:
                CadastroEntregadores(entregadores)
            case 3:
                AtualizacaoPedidos()
            case 4:
                ConsultaInformacoes()
            case 5:
                RelatoriosOperacionais()
            case _:
                sys.exit("Encerrando")


pedidos = []
entregadores = []
menu_principal(pedidos, entregadores)
