from .mortero import Mortero


class Concreto(Mortero):
    def __init__(self, cemento: float = 0.0, arena: float = 0.0, grava: float = 0.0,
                 agua: float = 0.0):
        super().__init__(cemento, arena, agua)
        self.grava = grava

    def json(self):
        return {
            "cemento": self.cemento,
            "arena": self.arena,
            "grava": self.grava,
            "agua": self.agua
        }

