from src.constants import Orientacao
from src.dominio import Ponto, Segmento, Poligono, Vetor


class VarreduraGraham:

    def gera_fecho_convexo(self, pontos: list[Ponto]) -> Poligono:
        ponto_inicial = self._encontra_ponto_incial(pontos)
        segmentos = self._cria_segmentos(ponto_inicial, pontos)
        pontos_ordenados = self._ordena_pontos(ponto_inicial, segmentos)
        segmentos_fecho_convexo = self._obtem_segmentos_fecho_convexo(pontos_ordenados)

        vertices = [segmento.vertice_inicial for segmento in segmentos_fecho_convexo]
        poligono = Poligono(vertices)

        return poligono

    @staticmethod
    def _encontra_ponto_incial(pontos: list[Ponto]) -> Ponto:
        min_coord_y = min(ponto.coord_y for ponto in pontos)
        pontos_min_coord_y = list(
            filter(
                lambda ponto: ponto.coord_y == min_coord_y, pontos
            )
        )

        if len(pontos_min_coord_y) == 1:
            ponto_inicial = pontos_min_coord_y[0]
        else:
            ponto_inicial = max(pontos_min_coord_y, key=lambda ponto: ponto.coord_x)

        return ponto_inicial

    @staticmethod
    def _cria_segmentos(ponto_inicial: Ponto, pontos: list[Ponto]) -> list[Segmento]:
        segmentos = []
        for ponto in pontos:
            if ponto == ponto_inicial:
                continue

            segmento = Segmento(ponto_inicial, ponto)
            segmentos.append(segmento)

        return segmentos

    @staticmethod
    def _ordena_pontos(ponto_inicial: Ponto, segmentos: list[Segmento]) -> list[Ponto]:
        vetor_canonico_horizontal = Vetor(x=1, y=0)
        pontos_ordenados = [ponto_inicial]

        prioridades = []
        for segmento in segmentos:
            vetor_unitario = segmento.ordenamento.normaliza()
            pseudo_angulo = 1 - vetor_unitario.calcula_produto_interno(vetor_canonico_horizontal)
            prioridades.append(pseudo_angulo)

        ordenamento = sorted(zip(prioridades, segmentos))
        pontos_ordenados.extend([segmento.vertice_final for _, segmento in ordenamento])

        return pontos_ordenados

    @staticmethod
    def _obtem_segmentos_fecho_convexo(pontos_ordenados: list[Ponto]) -> list[Segmento]:
        segmento = Segmento(pontos_ordenados[0], pontos_ordenados[1])
        segmentos = [segmento]

        for ponto in pontos_ordenados[2:]:
            orientacao = segmento.localiza_ponto(ponto)

            while orientacao == Orientacao.DIREITA:
                segmentos.pop()
                orientacao = segmentos[-1].localiza_ponto(ponto)

            segmento = Segmento(segmentos[-1].vertice_final, ponto)
            segmentos.append(segmento)

        segmento = Segmento(segmento.vertice_final, pontos_ordenados[0])
        segmentos.append(segmento)

        return segmentos
