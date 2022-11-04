import pygame.time
from pygame import *
from laser import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint,speed):
        super().__init__()
        self.image=pygame.image.load("clipart2630325.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=pos)
        self.max_x_constraint=constraint
        self.speed=5
        self.ready=False
        self.laser_time=0
        self.laser_cooldown=600
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif key[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time=pygame.time.get_ticks()
            if current_time-self.laser_time >= self.laser_cooldown:
                self.ready=True


    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,-8, self.rect.bottom))


    def constraint(self):
        if self.rect.left<=0:
            self.rect.left=0
        if self.rect.right>=self.max_x_constraint:
            self.rect.right=self.max_x_constraint

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
        self.constraint()