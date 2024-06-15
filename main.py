import pygame
import sys

from sprites import *
from config import *


class Game:

    #Constructor
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font("Arial")
        self.font = pygame.font.Font("src/fonts/Pokemon Solid.ttf", 32)
        self.running = True

        # Cargando las hojas de sprites
        self.character_spritesheet = Spritesheet("src/img/character.png")
        self.terrain_spritesheet = Spritesheet("src/img/terrain.png")
        self.enemy_spritesheet = Spritesheet("src/img/enemy.png")
        self.attack_spritesheet = Spritesheet("src/img/attack.png")
        self.intro_background = pygame.image.load("src/img/introbackground.png")
        self.go_background = pygame.image.load("src/img/gameover.png")
        
        

    def createTileMap(self):
        for i , row in enumerate(tile_map):
            for j , column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i) # si en esa posición hay una "B" significa que es un bloque u obstáculo entonces lo instancia
                if column == "E":
                    Enemy(self, j, i) # si en esa posición hay una "E" significa que es un enemigo entonces lo instancia
                if column == "P":
                    self.player = Player(self, j, i) # si en esa posición hay una "P" significa que el jugador entonces lo instancia
    
    def new(self):
        # a new game starts
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTileMap()

    
    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == "up":
                        Attack(self, self.player.rect.x, self.player.rect.y - TILE_SIZE)
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x, self.player.rect.y + TILE_SIZE)
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x - TILE_SIZE, self.player.rect.y )
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x + TILE_SIZE, self.player.rect.y )


            


    
    def update(self):
        #game loop updates
        self.all_sprites.update()


    
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    
    def main(self):
        #game loop

        while self.playing:
            self.events()
            self.update()
            self.draw()

        #self.running = False


    
    def game_over(self):
        text = self.font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, "Restart", 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()



    

    def intro_screen(self):
        intro = True

        title = self.font.render(TITULO, True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    


g = Game()

g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.QUIT()
sys.exit()