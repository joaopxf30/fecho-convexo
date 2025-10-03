import random
from src.dominio import Ponto


def gera_nuvem_pontos(numero_pontos: int, base: float, altura: float) -> list[Ponto]:
    nuvem_pontos = []

    for i in range(numero_pontos):
        coord_x = random.uniform(-base/2, base/2)
        coord_y = random.uniform(-altura/2, altura/2)
        ponto = Ponto(x=coord_x, y=coord_y)
        nuvem_pontos.append(ponto)

    return nuvem_pontos