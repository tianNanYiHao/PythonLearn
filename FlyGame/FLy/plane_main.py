#! /usr/bin/python3

# @File:   plane_main.py
# @Author: tiannanyihao
# @DATE:   2019-01-14
# @TIME:   14:05
# @Software: PyCharm
# @Production: 飞机大战main文件


from pygame import *
from plane_sprites import *


class PlaneGame(object):
    """
    飞机大战小游戏
    """

    def __init__(self):
        # 1.初始化pygame
        pygame.init()
        # 2.设置屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 3.设置时钟
        self.clock = pygame.time.Clock()
        # 4.设置飞机精灵
        self.__create_sprites()
        # 5.设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 6.设置定时器事件 - 英雄飞机发射子弹 0.5s
        pygame.time.set_timer(CREATE_BULLET_EVENT, 500)
        pass

    def __create_sprites(self):
        """
        私有方法-创建精灵类
        :return:
        """
        # 1.1 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)
        # 1.2 创建背景精灵组
        self.bgGroup = pygame.sprite.Group(bg1, bg2)

        # 2.1 创建敌机精灵组
        self.enemyGroup = pygame.sprite.Group()

        # 3.1 创建英雄精灵
        self.hero = Hero()
        # 3.2 创建英雄精灵组
        self.heroGroup = pygame.sprite.Group(self.hero)

    def game_start(self):
        """
        开始游戏
        :return:
        """
        while True:
            # 1.设置刷新帧率 - 60fps
            self.clock.tick(60)
            # 2.事件监听
            self.__event_lis()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.update
            pygame.display.update()
            pass

    def __event_lis(self):
        """
        私有-事件监听
        :return:
        """
        for spriteEvent in pygame.event.get():
            # 退出游戏
            if spriteEvent.type == pygame.QUIT:
                self.__game_over()
                pass
            # 敌机出现
            elif spriteEvent.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemyGroup.add(enemy)
                pass
            # 英雄飞机发射子弹
            elif spriteEvent.type == CREATE_BULLET_EVENT:
                self.hero.fire(HERO_FIRE_NORMEL)
                self.hero
                pass

        # 获取键盘所有按键的元组
        self.keys_pressed = pygame.key.get_pressed()
        # 英雄精灵1(player1)的控制
        if self.keys_pressed[pygame.K_UP]:  # ↑
            self.hero.move(HERO_MOVE_UP)
            pass
        elif self.keys_pressed[pygame.K_DOWN]:  # ↓
            self.hero.move(HERO_MOVE_DOWN)
        elif self.keys_pressed[pygame.K_LEFT]:  # ←
            self.hero.move(HERO_MOVE_L)
            pass
        elif self.keys_pressed[pygame.K_RIGHT]:  # →
            self.hero.move(HERO_MOVE_R)
            pass

        # 英雄精灵2(player2)的控制
        elif self.keys_pressed[pygame.K_w]:  # ↑
            self.hero.move(HERO_MOVE_UP)
            pass
        elif self.keys_pressed[pygame.K_s]:  # ↓
            self.hero.move(HERO_MOVE_DOWN)
            pass
        elif self.keys_pressed[pygame.K_a]:  # ←
            self.hero.move(HERO_MOVE_L)
            pass
        elif self.keys_pressed[pygame.K_d]:  # →
            self.hero.move(HERO_MOVE_R)
            pass
        else:
            pass

    def __check_collide(self):
        """
        私有-碰撞检测
        :return:
        """
        # 1. 子弹精灵组与敌机精灵组碰撞检测并湮灭
        pygame.sprite.groupcollide(self.hero.bulletGroup, self.enemyGroup, True, True)

        # 2. 英雄飞机与敌机精灵组碰撞检测并湮灭
        enemys = pygame.sprite.spritecollide(self.hero, self.enemyGroup, True)
        if len(enemys) > 0:
            self.hero.kill()  # 英雄飞机牺牲
            PlaneGame.__game_over()  # 游戏结束
        pass

    def __update_sprites(self):
        """
        私有-更新/绘制精灵组
        :return:
        """
        # 1.1 背景精灵组更新
        self.bgGroup.update()
        # 1.2 背景精灵组绘制
        self.bgGroup.draw(self.screen)

        # 2.1 敌机精灵组更新
        self.enemyGroup.update()
        # 2.2 敌机精灵组绘制
        self.enemyGroup.draw(self.screen)

        # 3.1 英雄精灵组更新
        self.heroGroup.update()
        # 3.2 英雄精灵组绘制
        self.heroGroup.draw(self.screen)

        self.hero.bulletGroup.update()
        self.hero.bulletGroup.draw(self.screen)

    def __game_over(self):
        """
        私有-游戏结束
        :return:
        """
        # 退出pygame
        pygame.quit()
        # 退出程序
        exit()
        pass

    @staticmethod
    def description():
        """
        飞机大战类方法-描述自己
        这是我的第一个python小程序,
        要好好学习啊!
        :return:
        """
        print(PlaneGame)


if __name__ == '__main__':
    game = PlaneGame()
    game.game_start()
    pass
