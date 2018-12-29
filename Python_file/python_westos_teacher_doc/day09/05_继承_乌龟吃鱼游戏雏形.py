#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_乌龟吃鱼游戏雏形.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:

游戏规则:
    1. 游戏背景为10*10；
    2. 游戏会自动生成1个乌龟和10条鱼；
    3. 它们移动方向随机;
    4. 乌龟最大移动能力为2； [-2,-1,1,2]
    5. 鱼最大移动能力为1； [-1,1]
    6. 当移动到场景边界， 自动反方向移动;
    7. 乌龟初始化体能为100<200为上限>;每移动一次消耗体能1；
    8. 当乌龟和鱼的坐标重合， 代表乌龟吃掉鱼， 体能增加20；
    9. 乌龟无体力或者鱼吃光， 游戏结束;

"""
import random




class BaseAnimal(object):
    def __init__(self):
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)
        
        
    def is_vaild(self, value):
        """判断坐标是否越界"""
        if value < 0:   # -2  --> 2
            return 0-value
        elif value > 9:
            return 9 - (value - 9)
        return value

class Turtle(BaseAnimal):
    def __init__(self):
        super(Turtle, self).__init__()
        self.power = 100

    def move(self):
        move_skill = [-1, 1, 0, -2, 2]
        # 乌龟最大移动能力为2；  # (0,10)
        new_x = self.x + random.choice(move_skill) #1
        new_y = self.y + random.choice(move_skill)  #12

        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

        self.power -= 1

    def eat(self):
        self.power += 20
        # 乌龟初始化体能为100<200为上限>
        if self.power >= 200:
            self.power = 200


class Fish(BaseAnimal):
    def move(self):
        move_skill = [-1, 1, 0]
        # 乌龟最大移动能力为2；  # (0,10)
        new_x = self.x + random.choice(move_skill)  # 1
        new_y = self.y + random.choice(move_skill)  # 12

        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

def main():
    t1 = Turtle()

    # 10个鱼
    fishs = [Fish() for i in  range(10)]
    # fishs = []
    # for i in range(10):
    #     fishs.append(Fish())

    while True:
        # 判断游戏是否结束?
        if t1.power <= 0:
            print("乌龟over! Game Over......")
            break
        elif len(fishs) == 0:
            print("鱼被吃光！Game Over.......")
            break
        else:
            # 乌龟和鱼移动
            t1.move()
            for fish in fishs:
                fish.move()
                # 判断乌龟是否吃到鱼？
                if t1.x == fish.x and t1.y == fish.y:
                    t1.eat()
                    fishs.remove(fish)
                    print("鱼被吃掉......")
                    print("乌龟最新体能:%s" %(t1.power))
            else:
                print("乌龟没有吃到鱼，最新体能为%s" %(t1.power))

if __name__ == "__main__":
    main()







