# META DATA:
# 200
# 32
# 2020-01-01Т12:51:32.124Z – [username1] - wanna top up 10l
# 2020-01-01Т12:51:34.769Z – [username2] - wanna scoop 50l
import random as r
import datetime as dt


def generate_time(n):
    return (dt.datetime.now()).isoformat()


def generate_times(n):
    times = []
    now = dt.datetime.now()

    for i in range(n):
        delta = dt.timedelta(seconds=r.randint(0, 59),
                             microseconds=r.randint(0, 999))
        now += delta
        times.append(now.isoformat() + "Z")
    return times


def generate_actions(n):
    users = []
    for i in range(r.randint(3, 7)):
        users.append(f"[username{i + 1}]")

    actions = []
    base_actions = ["top_up", "scoop"]
    for i in range(n):
        actions.append(f" - {r.choice(users)} - wanna {r.choice(base_actions)}"
                       + f" {r.randint(4, 100)}l\n")
    return actions


def get_log_body(n):
    times = generate_times(n)
    actions = generate_actions(n)
    body = []
    for i in range(n):
        body.append(times[i] + actions[i])
    return body


def create_log(n):
    volume = r.randint(200, 300)
    current_level = r.randint(20, 100)
    in_file = open("log.log", "w")
    in_file.write("META DATA:\n")
    in_file.write(f"{volume}\n")
    in_file.write(f"{current_level}\n")
    body = get_log_body(n)
    in_file.writelines(body)

    in_file.close()


create_log(17000)

