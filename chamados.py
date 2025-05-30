import json
import os

class GerenciadorChamados:
    """
    Gerencia a fila de chamados, com armazenamento em arquivo JSON.
    Permite adicionar, listar, atender com prioridade, deletar e salvar chamados.
    """

    def __init__(self, arquivo_dados="chamados.json"):
        self.fila = []
        self.arquivo = arquivo_dados
        self.carregar()

    def adicionar(self, chamado):
        """Adiciona um novo chamado à fila e salva no arquivo."""
        self.fila.append(chamado)
        self.salvar()

    def proximo(self):
        """
        Retorna o próximo chamado a ser atendido.
        Dá prioridade se houver diferença de gravidade maior ou igual a 2.
        """
        if not self.fila:
            return None
        fila_ordenada = sorted(self.fila, key=lambda x: x['gravidade'], reverse=True)
        if len(fila_ordenada) >= 2:
            primeiro = fila_ordenada[0]
            segundo = fila_ordenada[1]
            if primeiro['gravidade'] - segundo['gravidade'] >= 2:
                self.fila.remove(primeiro)
                self.salvar()
                return primeiro
        chamado = self.fila.pop(0)
        self.salvar()
        return chamado

    def listar(self):
        """Retorna a lista completa de chamados."""
        return list(self.fila)

    def deletar(self, id_chamado):
        """
        Remove um chamado da fila com base no ID.

        Args:
            id_chamado (int): Identificador do chamado a remover.

        Returns:
            bool: True se removido, False se não encontrado.
        """
        original_len = len(self.fila)
        self.fila = [item for item in self.fila if item['id'] != id_chamado]
        if len(self.fila) < original_len:
            self.salvar()
            return True
        else:
            return False

    def salvar(self):
        """Salva a fila atual no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.fila, f, ensure_ascii=False, indent=4)

    def carregar(self):
        """Carrega a fila de chamados do arquivo JSON se existir."""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    self.fila = json.load(f)
                except json.JSONDecodeError:
                    self.fila = []
        else:
            self.fila = []
