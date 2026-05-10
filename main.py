from conexao import criar_cliente

def listar_container():
    cliente = criar_cliente()
    for conatiner in cliente.containers.list():
        print(conatiner.id)


if __name__ == "__main__":
    listar_container()