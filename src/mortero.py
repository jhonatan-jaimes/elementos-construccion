class Mortero:
    def __init__(self, cemento: float = 0.0, arena: float = 0.0, agua: float = 0.0):
        super().__init__()
        self.cemento = cemento
        self.arena = arena
        self.agua = agua

    def json(self):

        return {
                "cemento": self.cemento,
                "arena": self.arena,
                "agua": self.agua
        }


mortero = Mortero()
