from src.dominio import Ponto
from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_fecho_convexo
from src.varredura_graham import VarreduraGraham


if __name__ == '__main__':
    circulo = Circulo(
        centro=Ponto(x=-5.0, y=-5.0),
        raio=5
    )
    pontos = gera_nuvem_pontos(
        numero_pontos=66,
        circulo=circulo,
    )

    varredura_graham = VarreduraGraham()
    fecho_convexo = varredura_graham.gera_fecho_convexo(pontos)
    plota_fecho_convexo(fecho_convexo, pontos)

