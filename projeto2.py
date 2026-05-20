import sys

def CadastroPedidos(pedidos):
    id = GerarID(pedidos)

    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")

    prioridade = ""
    while prioridade not in ["alto", "normal"]:
        prioridade = input("Qual a prioridade (Alto, Normal): ").strip().lower()

    descricao = input("Descrição do pedido: ")

    status = "Pendente"

    entregador = EntregadorPedido()

    dadosPedido = {
        'id': id,
        'nome': nome,
        'endereco': endereco,
        'prioridade': prioridade,
        'descricao': descricao,
        'status': status,
        'entregador': entregador
    }

    pedidos.append(dadosPedido)

    print("Pedido cadastrado com sucesso!")
    print(pedidos)


def CadastroEntregadores():
    print("2")


def AtualizacaoPedidos():
    print("3")


def ConsultaInformacoes():
    print("4")


def RelatoriosOperacionais():
    print("5")


def EntregadorPedido():


def GerarID(pedidos):


def menu_principal(pedidos):
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
                CadastroPedidos(pedidos)
            case 2:
                CadastroEntregadores()
            case 3:
                AtualizacaoPedidos()
            case 4:
                ConsultaInformacoes()
            case 5:
                RelatoriosOperacionais()
            case _:
                sys.exit("Encerrando")


pedidos = []

menu_principal(pedidos)