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
        self.running = True

        self.character_spritesheet = Spritesheet("src/img/character.png")
        self.terrain_spritesheet = Spritesheet("src/img/terrain.png")
        self.enemy_spritesheet = Spritesheet("src/img/enemy.png")

    def createTileMap(self):
        for i , row in enumerate(tile_map):
            for j , column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i) # si en esa posición hay una "B" significa que es un bloque u obstáculo entonces lo instancia
                if column == "E":
                    Enemy(self, j, i) # si en esa posición hay una "E" significa que es un enemigo entonces lo instancia
                if column == "P":
                    Player(self, j, i) # si en esa posición hay una "P" significa que el jugador entonces lo instancia
    
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

        self.running = False


    
    def game_over(self):
        pass
    

    def intro_screen(self):
        pass
    


g = Game()

g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.QUIT()
sys.exit()