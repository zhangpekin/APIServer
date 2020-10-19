from .base_model import BaseModel


class Test(BaseModel):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.data = []

    def render(self):
        self.data = [
            {
                "t1": {
                    "a": 1,
                    "b": 2
                },
                "t2": {
                    "A": "hello",
                    "B": "world"
                }
            },
            {
                "d1": {
                    "c": 3,
                    "d": 4
                },
                "d2": {
                    "C": "python",
                    "D": "flask"
                }
            }
        ]

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "data": self.data
        }
