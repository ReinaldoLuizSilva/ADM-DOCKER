from backend.conexao import criar_cliente
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/conatiner")
def listar_container():
    cliente = criar_cliente()
    return [{
        "id": c.id[:12], "name:": c.name, "status": c.status }
        for c in cliente.containers.list()
    ]

def listar_images():
    cliente = criar_cliente()
    for images in cliente.images.list():
        print(images.id, images.labels)

if __name__ == "__main__":
    listar_container()
    listar_images()