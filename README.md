# Fecho convexo 2D pelo algoritmo por varredura de Graham 

Este projeto, intitulado fecho convexo, implementa o algoritmo por varredura de Graham. A versão utilizada para desenvolvimento é Python 3.12.3.


---
## Ambientes virtuais

É fortemente recomendado a utilização de ambientes virtuais. Para tal, execute no terminal a partir de um path desejado o seguinte comando de acordo com o sistema operacional:

**WINDOWS**:
```
python -m venv env
```

**OS/LINUX**:
```
python3 -m venv env
```

Para ativação do ambiente virutal, execute o seguinte comando de acordo com a platafoma:

**WINDOWS**:
```
<path>\env\Scripts\Activate.ps1
```

**POSIX**:
```
source <path>/env/bin/activate
```

O ambiente virtual será criado.

## Instalando dependências

Todas as dependências do projeto se encontram no arquivo `requirements.txt`. A obtenção é feita a partir da execução do seguinte comando na raiz do projeto:

```
pip install -r requirements.txt
```

As dependências são instaladas.

## Recomendações de uso

Para acionar o código basta rodar da raiz do projeto

```
python main.py
```

O código realizará o plot do fecho convexo 2D para uma nuvem de pontos contendo `numero_pontos` elementos que é
gerada aleatoriamente a partir de uma distribuição uniforme em área de um quardado centrado na origem e com lados iguais
a `base` e `altura`:

```python
if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=100,
        base=10,
        altura=10,
    )

    varredura_graham = VarreduraGraham()
    fecho_convexo = varredura_graham.gera_fecho_convexo(pontos)
    plota_fecho_convexo(fecho_convexo, pontos)
```
