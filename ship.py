import pygame
from pygame.sprite import Sprite

from path import resource_path


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        asset_url = resource_path("images/ship.bmp")
        self.image = pygame.image.load(asset_url)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放置在屏幕底端的中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center 中储存小数值
        self.center = float(self.rect.centerx)

        # 设置飞船的移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center的值更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置画飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船放置到屏幕底部的中央位置"""
        self.center = self.screen_rect.centerx