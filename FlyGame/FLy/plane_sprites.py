#! /usr/bin/python3

# @File:   plane_sprites.py
# @Author: tiannanyihao
# @DATE:   2019-01-14
# @TIME:   14:05
# @Software: PyCharm
# @Production: 飞机大战_精力对象


import pygame
import random

# 配置屏幕rect
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹发射的定时器
CREATE_BULLET_EVENT = pygame.USEREVENT + 1

# 创建英雄飞机的移动方向
HERO_MOVE_UP = 'HERO_MOVE_UP'
HERO_MOVE_DOWN = 'HERO_MOVE_DOWN'
HERO_MOVE_R = 'HERO_MOVE_R'
HERO_MOVE_L = 'HERO_MOVE_L'

# 创建英雄飞机子弹模式
HERO_FIRE_NORMEL = 'HERO_FIRE_NORMEL'
HERO_FIRE_SUPER = 'HERO_FIRE_SUPER'


class GameSprites(pygame.sprite.Sprite):
    """
    基础精灵类
    """

    def __init__(self, image_name, speed=1):
        super().__init__()

        # 添加img属性
        self.image = pygame.image.load(image_name)
        # 添加rect属性
        self.rect = self.image.get_rect()
        # 添加速度属性
        self.speed = speed

    """
    提供动画更新的接口
    """

    def update(self):
        self.rect.y += self.speed * 3


class Background(GameSprites):
    """
    背景精灵子类
    重写GameSprites类的update方法
    扩充背景滚动的功能
    """

    def __init__(self, is_alt=False):
        super().__init__('../src/images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类实现
        super().update()
        # 2.判断是否移到底部,移到底部则重置y
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.y


class Enemy(GameSprites):
    """
    敌机精灵子类
    随机出现
    每个随机秒数出现
    """

    def __init__(self):
        super().__init__('../src/images/enemy1.png')
        # 1.随机速度
        self.speed = random.randint(2, 4)
        # 2.随机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        # 3.固定敌机的底部位置
        self.rect.bottom = 0

    def update(self):
        # 1. 调用父类方法
        super().update()
        # 2. 判断敌机飞出屏幕删除
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprites):
    """
    英雄精灵子类
    初始位置
    不能飞出屏幕
    发射子弹
    """

    def __init__(self):
        super().__init__('../src/images/me1.png')
        # 1.初始位置-中间
        self.rect.center = SCREEN_RECT.center
        self.rect.y = SCREEN_RECT.height * 4 / 5
        # 2.英雄精灵的移动速度
        self.speed = 1
        # 3.英雄精灵在垂直方向上的移动速度补偿值
        self.speed_Move_UPDOWN = 8
        # 4.英雄精灵在水平方向上的移动速度补偿值
        self.speed_Move_RL = 6
        # 5.为英雄精灵添加子弹精灵组
        self.bulletGroup = pygame.sprite.Group()

    def move(self, type):
        """
        英雄精灵移动,上下左右
        :param type:
        :return:
        """
        # 移动
        if type == HERO_MOVE_UP:
            self.rect.y -= self.speed + self.speed_Move_UPDOWN
            pass
        elif type == HERO_MOVE_DOWN:
            self.rect.y += self.speed + self.speed_Move_UPDOWN
            pass
        elif type == HERO_MOVE_L:
            self.rect.x -= self.speed + self.speed_Move_RL
            pass
        elif type == HERO_MOVE_R:
            self.rect.x += self.speed + self.speed_Move_RL
            pass
        else:
            pass

        # 移动边界检测
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.bottom >= SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self, type=HERO_FIRE_NORMEL):
        """
        开火
        :param type: 子弹模式
        :return:
        """
        if type == HERO_FIRE_NORMEL:
            # 创建子弹精灵1
            bullet1 = Bullet('../src/images/bullet1.png')
            bullet1.rect.center = self.rect.center
            bullet1.rect.y = self.rect.y - 20
            self.bulletGroup.add(bullet1)

        elif type == HERO_FIRE_SUPER:
            # 创建子弹精灵1
            bullet1 = Bullet('../src/images/bullet1.png')
            bullet1.rect.x = self.rect.x + self.rect.width / 4
            bullet1.rect.y = self.rect.y

            # 创建子弹精灵2
            bullet2 = Bullet('../src/images/bullet2.png')
            bullet2.rect.center = self.rect.center
            bullet2.rect.y = self.rect.y - 20

            # 创建子弹精灵3
            bullet3 = Bullet('../src/images/bullet1.png')
            bullet3.rect.x = self.rect.x + self.rect.width * 3 / 4
            bullet3.rect.y = self.rect.y

            self.bulletGroup.add(bullet1, bullet2, bullet3)

    def update(self):
        # super().update(
        pass


class Bullet(GameSprites):
    """
    子弹精灵子类
    """

    def __init__(self, imgName):
        # 设置子弹图片,速度
        super().__init__(imgName, -4)

    def update(self):
        super().update()
        # 子弹飞出后,删除子弹
        if self.rect.y <= 0:
            self.kill()

    def __del__(self):
        pass