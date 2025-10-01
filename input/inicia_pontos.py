from src.dominio import Ponto


def inicia_pontos(coordenadas_x: list[float], coordenadas_y: list[float]) -> list[Ponto]:
    pontos = [Ponto(x,y) for x, y in zip(coordenadas_x, coordenadas_y)]

    return pontos