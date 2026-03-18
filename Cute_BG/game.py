import pygame
import random
from settings import *
from board import Board
from player import Player
from cards import draw_card, apply_card_effect


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cute Board Game - Victory Points")
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("arial", 20)
        self.big_font = pygame.font.SysFont("arial", 40, bold=True)

        self.board = Board(BOARD_ROWS, BOARD_COLS, TILE_SIZE, BOARD_POS)

        # Create 4 players with different colors
        self.players = [
            Player(name="Player 1", color=(240, 128, 128), tile_index=0),
            Player(name="Player 2", color=(135, 206, 250), tile_index=0),
            Player(name="Player 3", color=(144, 238, 144), tile_index=0),
            Player(name="Player 4", color=(238, 130, 238), tile_index=0),
        ]

        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        self.die_value = None
        self.message = f"{self.current_player.name}: Press SPACE to roll the die."
        self.game_over = False

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]
        self.message = f"{self.current_player.name}: Press SPACE to roll the die."

    def roll_die_and_move(self):
        if self.game_over:
            return

        self.die_value = random.randint(1, 6)
        self.message = f"{self.current_player.name} rolled a {self.die_value}."

        # Move player
        self.current_player.move(self.die_value)

        # Keep player within board bounds
        if self.current_player.tile_index >= self.board.total_tiles - 1:
            self.current_player.tile_index = self.board.total_tiles - 1
            self.check_end_game()
            return

        # Check tile effect
        tile_type = self.board.tile_types[self.current_player.tile_index]

        if tile_type == "vp":
            self.current_player.victory_points += 1
            self.message += " Gained 1 victory point!"
        elif tile_type == "card":
            card = draw_card()
            self.message += f" Drew card: {card['text']}"
            apply_card_effect(card, self.current_player, self.players)

        # Update screen message
        self.message += f" Now has {self.current_player.victory_points} VP."

    def check_end_game(self):
        # Game ends when a player reaches the final tile
        self.game_over = True
        # Decide winner by victory points
        winner = max(self.players, key=lambda p: p.victory_points)
        self.message = f"Game Over! {winner.name} wins with {winner.victory_points} VP!"

    def draw_ui(self):
        # Draw board
        self.board.draw(self.screen)

        # Draw players
        for player in self.players:
            tile_pos = self.board.get_tile_rect(player.tile_index)
            # Draw a smaller circle inside the tile
            center_x = tile_pos.centerx
            center_y = tile_pos.centery
            pygame.draw.circle(self.screen, player.color, (center_x, center_y), TILE_SIZE // 4)

        # Draw info panel
        info_y = BOARD_POS[1] + BOARD_ROWS * TILE_SIZE + 10
        info_rect = pygame.Rect(BOARD_POS[0], info_y, BOARD_COLS * TILE_SIZE, 100)
        pygame.draw.rect(self.screen, (255, 255, 255), info_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), info_rect, 2)

        # Current message
        msg_surf = self.font.render(self.message, True, (0, 0, 0))
        self.screen.blit(msg_surf, (info_rect.x + 10, info_rect.y + 10))

        # Victory points list
        vp_text = " | ".join([f"{p.name}: {p.victory_points} VP" for p in self.players])
        vp_surf = self.font.render(vp_text, True, (0, 0, 0))
        self.screen.blit(vp_surf, (info_rect.x + 10, info_rect.y + 40))

        # Die value if rolled
        if self.die_value is not None and not self.game_over:
            die_surf = self.font.render(f"Last roll: {self.die_value}", True, (0, 0, 0))
            self.screen.blit(die_surf, (info_rect.x + 10, info_rect.y + 70))

        # Game over overlay
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))

            end_msg = self.big_font.render("Game Over!", True, (255, 255, 255))
            self.screen.blit(end_msg, (SCREEN_WIDTH // 2 - end_msg.get_width() // 2, SCREEN_HEIGHT // 2 - 60))

            detail_msg = self.font.render(self.message, True, (255, 255, 255))
            self.screen.blit(detail_msg, (SCREEN_WIDTH // 2 - detail_msg.get_width() // 2, SCREEN_HEIGHT // 2))

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if not self.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.roll_die_and_move()
                        # Only move to next player if game not ended
                        if not self.game_over:
                            self.next_player()

            self.screen.fill((245, 245, 245))
            self.draw_ui()
            pygame.display.flip()

        pygame.quit()
