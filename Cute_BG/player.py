from pydantic import BaseModel  
class Player(BaseModel):
    name: str
    color: tuple
    tile_index: int = 0
    victory_points: int = 0

    def move(self, steps: int):          # move never returns a value, it just updates the player's position
        self.tile_index += steps
