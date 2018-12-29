#!/usr/bin/env python
#coding:utf-8


""""
Name: 10_Anaconda安装.py
Date: 2018/05/24
Connect: xc_guofan@163.com
Author: lvah
Desc:


Anaconda: conda 和 Python等180多个科学包及其依赖项；





conda: python开源包的安装与管理和虚拟环境的管理;



"""

import itchat



#


actions = ['Up', 'Down', 'Left', 'Right', 'Restart', 'Exit']
letters = 'WASDRQ'+ 'WASDRQ'.lower()
actions_dict = dict(zip(letters, actions*2))
print(actions_dict)




# 2. 游戏主逻辑:
# Init:  init()--- 随机生成游戏背景， 并且随机生成22/24；
#     Game




# Game:   game()
#       Game
#       Win
#       GameOver
#       Exit
#       Restart   ---- init()



# Win: not_game('Win')
#   Init
#   Exit

# GameOver:   not_game('')
#   Init
#   Exit



# Exit




def main():



    def init():
        #
        # pass
        return 'Game'



    def game():
        # 根据用户输入， 判断操作或者下一步状态
        #
        # action = input("选择:")
        # if action == 'Restart':
        #     return 'Init'
        # elif action == 'Exit':
        #     return 'Exit'
        # else:
        #
        #     if 游戏is_win():
        #         return 'Win'
        #     elif 游戏is_win():
        #         return 'GameOver'
        #     else:
        #         return 'Game'
        #


    state_actions = {
        'Init': init,
        'Game': game,




    }


    state = 'Init'
    while state != 'Exit':
        # 继续游戏
        pass




def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()




import curses


