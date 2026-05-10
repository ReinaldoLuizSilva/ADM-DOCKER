from conexao import criar_cliente

def listar_container():
    cliente = criar_cliente()
    for container in cliente.containers.list():
        print(container.id, container.status, container.name, container.ports, container.health)

def listar_images():
    cliente = criar_cliente()
    for images in cliente.images.list():
        print(images.id, images.labels)

if __name__ == "__main__":
    listar_container()
    listar_images()