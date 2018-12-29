#!/usr/bin/env python
# coding:utf-8


""""
Name: 2048.py
Date: 2018/05/26
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
import curses
from itertools import chain
from random import choice, randint


class GameField(object):
    def __init__(self, width=4, height=4, win_value=2048):
        self.width = width
        self.height = height
        self.win_value = win_value
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        """重置棋盘"""
        if self.score > self.height:
            self.highscore = self.score
        self.score = 0

        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]

        self.random_create()
        self.random_create()

    def random_create(self):
        """初始化棋盘时， 在随机位置生成2或者4， 2的可能性大， 4的可能性少"""
        # 可能出现的问题: 随机生成的i,j位置原本已经有值。 解决方法：
        while True:
            i, j = choice(range(self.width)), choice(range(self.height))
            if self.field[i][j] == 0:
                self.field[i][j] = 4 if randint(1, 100) > 80 else 2
                break

    def draw(self, stdscr):
        def draw_sep():
            line = '+' + '----+' * self.width
            stdscr.addstr(line + '\n')

        def draw_row(row):  # [2,0,2,0]
            draw_one_row = "".join(['|{:^4}'.format(num)
                                    if num != 0  else '|    ' for num in row]) + '|'

            stdscr.addstr(draw_one_row + '\n')

        # 清屏
        stdscr.clear()
        stdscr.addstr('SCORE:' + str(self.score) + '\n')
        if self.highscore != 0:
            stdscr.addstr("HIGHSCORE:" + str(self.highscore) + '\n\n')

        for row in self.field:
            draw_sep()
            draw_row(row)
        draw_sep()

        if self.is_win():
            stdscr.addstr('You win!' + '\n')
        if self.is_gameover():
            stdscr.addstr('Game Over!' + '\n')
        stdscr.addstr("                上下左右键" + '\n')
        stdscr.addstr("       (R)Restart (Q)Exit" + '\n')

    def is_win(self):
        return max(chain(*self.field)) >= self.win_value

    def is_gameover(self):
        """任何方向都不能移动时"""
        return not any([self.move_is_possible(direction)
                        for direction in ['Up', 'Down', 'Right', 'Left']])

    @staticmethod
    def invert(field):
        # 对于列表每一行进行反转
        return [row[::-1] for row in field]

    @staticmethod
    def tranpose(field):
        """对于列表转置， 可以间接求向上移动的可能性"""
        return [list(row) for row in zip(*field)]

    def move_is_possible(self, direction):
        def move_left_possible(row):
            """判断列表中的一行是否可以移动"""

            # 0 2, 0 4, 2 2, 4 2
            # 0 0
            # # 1. 判断两个元素是否可以移动?
            # 4,2,2,2
            def is_change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False

            # len(row)-1 =4-1 = 3
            # i= 0,1,2
            # 依次遍历每一行的每一个元素， 判断是否可以移动， 只要有一个时可以移动的， 返回True
            return any([is_change(i) for i in range(len(row) - 1)])

        check = {}

        check['Left'] = lambda field: any([move_left_possible(row) for row in field])
        # check['Right'] = lambda  field: any([ move_left_possible(row) for row in invert(field)])
        # 判断每行内容反转后的field能否向左移动， 即原field能否向右移动;
        check['Right'] = lambda field: check['Left'](self.invert(field))
        # 判断转置后的field能否向左移动， 即原field能否向上移动;
        check['Up'] = lambda field: check['Left'](self.tranpose(field))
        # 判断转置后的field能否向右移动， 即原field能否向下移动;
        check['Down'] = lambda field: check['Right'](self.tranpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def move(self, direction):

        def move_row_left(row):
            def tight(row):
                """把所有非0的聚集在最左边"""
                # [0,2,2,4]  === [2,2,4]
                new_row = [item for item in row if item != 0]
                # if len(new_row) != len(row):
                # [2,2,4]+ [0] ==> new_row=new_row+[0]
                # range(0)不报错;
                new_row += [0 for item in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                # 从左向右依次遍历， 如果两个值相等， 那么左边*2， 右边=0，
                for i in range(len(row) - 1):  # 0,1,2,3
                    if row[i] == row[i + 1]:
                        row[i] *= 2
                        row[i + 1] = 0
                        self.score += row[i]
                return row

            return tight(merge(tight(row)))

        moves = {}

        moves['Left'] = lambda field: \
            [move_row_left(row) for row in field]

        moves['Right'] = lambda field: \
            self.invert([move_row_left(row) for row in self.invert(field)])

        moves['Up'] = lambda field: \
            self.tranpose([move_row_left(row) for row in self.tranpose(field)])

        moves['Down'] = lambda field: \
            self.tranpose(moves['Right'](self.tranpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.random_create()
                return True
            else:
                return False


def get_user_action(stdscr):
    action = stdscr.getch()
    if action == curses.KEY_UP:
        return 'Up'
    if action == curses.KEY_DOWN:
        return 'Down'
    if action == curses.KEY_LEFT:
        return 'Left'
    if action == curses.KEY_RIGHT:
        return 'Right'
    if action == ord('r'):
        return 'Restart'
    if action == ord('q'):
        return 'Exit'


def main(stdscr):
    def init():
        # 初始化棋盘；
        game_field.reset()
        return 'Game'

    def game():
        # 画棋盘
        game_field.draw(stdscr)
        # 获取用户的操作
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'GameOver'
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)
        while True:
            action = get_user_action(stdscr)
            if action == 'Restart':
                return 'Init'
            if action == 'Exit':
                return 'Exit'

    state_actions = {
        'Init': init,
        'Game': game,
        'Win': lambda: not_game('Win'),
        # ‘Init’, 'Exit'
        'GameOver': lambda: not_game('GameOver')
    }

    game_field = GameField(win_value=2048)

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()


curses.wrapper(main)
