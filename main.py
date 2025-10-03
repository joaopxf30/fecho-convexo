from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_fecho_convexo
from src.varredura_graham import VarreduraGraham


if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=100,
        base=10,
        altura=10,
    )

    varredura_graham = VarreduraGraham()
    fecho_convexo = varredura_graham.gera_fecho_convexo(pontos)
    plota_fecho_convexo(fecho_convexo, pontos)

