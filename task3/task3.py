# Некоторое количество человек то наливают воду в бочку, то черпают из бочки.
# Если человек пытается налить больше воды,
# чем есть свободного объема – это ошибка,
# при этом объем воды в бочке не меняется.
# Так же если человек пытается зачерпнуть больше воды,
# чем есть в бочке – ошибка,
# объем воды также при этом не меняется. В остальных случаях – успех.
# Вам дан лог файл. Напишите программу, которая ответит на следующие вопросы:
# - какое количество попыток налить воду в бочку было за указанный период?
# - какой процент ошибок был допущен за указанный период?
# - какой объем воды был налит в бочку за указанный период?
# - какой объем воды был не налит в бочку за указанный период?
# - … тоже самое для забора воды из бочки …
# - какой объем воды был в бочке в начале указанного периода?
# Какой в конце указанного периода? "%Y-%d-%mT%H:%M:%S.%")
import datetime as dt
import sys


class Action:
    user = ""
    date = dt.datetime.now()
    action = ""
    amount = 0

    def __init__(self, user, date, action, amount):
        self.user = user
        self.date = dt.datetime.fromisoformat(date)
        self.action = action
        self.amount = amount


class Barrel:
    overall = 0
    current = 0

    def __init__(self, overall, current):
        self.overall = overall
        self.current = current

    def topup(self, amount):
        if amount > (self.overall - self.current):
            return False
        else:
            self.current += amount
            return True

    def scoop(self, amount):
        if amount > self.current:
            return False
        else:
            self.current -= amount
            return True

# 2020-02-06T05:26:33.920714Z - [username1] - wanna scoop 77l


def parse_line(line):
    date = line[: line.find("Z")]
    user = line[line.find("[") + 1: line.find("]")]
    action = "scoop" if "scoop" in line else "top_up"
    if action == "scoop":

        amount = int(line[line.find("scoop") + 6: line.find("l")])
    else:
        amount = int(line[line.find("top_up") + 6: line.find("l")])
    return Action(user, date, action, amount)


def parse_log(path, start, end):
    log_file = open(path, "r")
    log_file.readline()
    barrel = Barrel(int(log_file.readline()), int(log_file.readline()))
    for line in log_file:
        action = parse_line(line)
        print(action.user, action.date, action.action, action.amount)
        break
    print(barrel.overall, barrel.current)
    log_file.close()


def main():
    usage = ("\033[1m" + "\033[91m" +
             "Usage:" + " python3 task3.py " +
             "path_to_log beg_datetime end_datetime" +
             "\033[0m")
    if len(sys.argv != 4):
        print(usage)
        exit()
    parse_log(sys.argv[1], sys.argv[2], sys.argv[3])
