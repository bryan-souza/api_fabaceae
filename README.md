# Fabaceae API

API criada para realizar o upload de imagens e a identificação de plantas da família das fabaceas. Feito com [FastAPI](https://fastapi.tiangolo.com).

Link original do projeto: https://gitlab.com/BDAg/aipim

## O que há de novo?

* Módulo `cerebrum`
    * Re-implementação do código original de identificação da imagem
    * Agora pode ser consumido tanto pela API como por outra aplicação python

* Dockerfile
    * Criação de um Dockerfile para deploy local usando gerenciadores de containeres como [Docker](https://docker.com) e [Podman](https://podman.io)

## Instalação

Você pode escolher realizar o deploy localmente (diretamente na sua máquina) ou utilizando um contâiner.

### Instalação Local

Para realizar o deploy localmente, você deverá ter instalado em sua máquina as seguintes dependências:

* Python 3.8+
* PIP

1. Baixe/clone esse repositório em sua máquina

```
git clone https://github.com/bryan-souza/api_fabaceae.git
```

2. Instale as bibliotecas python necessárias usando PIP

```
pip install -r requirements.txt
```

3. Inicialize o servidor

```
uvicorn server:app
```

> NOTA: Utilizamos o servidor web [uvicorn](https://uvicorn.org). Todas as customizações e flags encontradas na documentação do uvicorn podem ser aplicadas ao inicializar o servidor.

### Usando um contâiner

### Docker

Será inserido aqui quando forem realizados os devidos testes :p

### Buildah + Podman

> NOTA: Por padrão, a porta 80 (HTTP) será exposta (vide Dockerfile), porém é sabido que a mesma não pode ser utilizada em modo rootless. Então fica a seu critério alterar o Dockerfile e mudar a porta padrão, ou usar o Podman em modo root (como descrito abaixo)

1. Construa a imagem

```
sudo buildah build --format=docker -f Dockerfile -t api_fabaceae
```

2. Execute o contâiner

```
sudo podman run -dt --name api_fabaceae -p 80:80 localhost/api_fabaceae
```

