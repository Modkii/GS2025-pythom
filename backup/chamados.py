import json
import os


class GerenciadorChamados:
    """
    Gerencia chamados com regra de prioridade:
    - Chamados com diferença de gravidade >= 2 são prioritários.
    - Caso contrário, seguem ordem de chegada (FIFO).
    """

    def __init__(self, arquivo_dados="chamados.json"):
        self.fila = []  # Fila simples (não usa heap)
        self.arquivo = arquivo_dados
        self.carregar()

    def adicionar(self, chamado):
        self.fila.append(chamado)
        self.salvar()

    def proximo(self):
        if not self.fila:
            return None

        # Ordenar por gravidade decrescente (temporário)
        fila_ordenada = sorted(self.fila, key=lambda x: x['gravidade'], reverse=True)

        # Verificar se o primeiro tem diferença de 2 ou mais do segundo
        if len(fila_ordenada) >= 2:
            primeiro = fila_ordenada[0]
            segundo = fila_ordenada[1]

            if primeiro['gravidade'] - segundo['gravidade'] >= 2:
                self.fila.remove(primeiro)
                self.salvar()
                return primeiro

        # Caso não haja diferença >= 2, atender pelo primeiro da fila (FIFO)
        chamado = self.fila.pop(0)
        self.salvar()
        return chamado

    def listar(self):
        return list(self.fila)

    def deletar(self, id_chamado):
        original_len = len(self.fila)

        self.fila = [
            item for item in self.fila if item['id'] != id_chamado
        ]

        if len(self.fila) < original_len:
            self.salvar()
            return True
        else:
            return False

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.fila, f, ensure_ascii=False, indent=4)

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    self.fila = json.load(f)
                except json.JSONDecodeError:
                    self.fila = []
        else:
            self.fila = []
