# Cute Board Game

A simple 4-player turn-based board game built with pygame.

## How to Play

1. Up to 4 players take turns rolling a die (press **Space**).
2. Move along a 5x5 grid of tiles, collecting victory points along the way.
3. The first player to reach the final tile ends the game. The player with the most **victory points wins**.

## Tile Types

| Tile | Effect |
|------|--------|
| Normal | Nothing happens |
| VP (yellow) | Gain 1 victory point |
| Card (blue) | Draw a random event card |
| End (gold) | Triggers game over |

## Cards

- **Lucky Day** — Gain 2 VP
- **Oops!** — Lose 1 VP
- **Steal** — Take 1 VP from the next player
- **Speed Boost** — Move forward 2 tiles
- **Trip** — Move backward 2 tiles

## Requirements

```
pip install pygame pydantic
```

## Run

```
python main.py
```
