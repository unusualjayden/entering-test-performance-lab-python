import math as m
import sys


def get_distance_between_points(a, b):
    return m.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


def get_height_of_triangle(a, b, c):
    ab = get_distance_between_points(a, b)
    bc = get_distance_between_points(b, c)
    ac = get_distance_between_points(a, c)
    p = (ab + bc + ac) / 2
    return (2 * m.sqrt(p * (p - ab) * (p - bc) * (p - ac))) / bc


def parse_file(path):
    ifile = open(path, "r+")
    for line in ifile:
        tmp = (line.replace('sphere', '"sphere"')
                   .replace('center', '"center"')
                   .replace('radius', '"radius"')
                   .replace('line', '"line"')
                   .replace("{[", "([")
                   .replace("]}", "])")
                   .replace(" ", ""))
    return eval(tmp)


def find_intersection(c, a, b, r):
    aq = (b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2
    cq = (c[0] - a[0])**2 + (c[1] - a[1])**2 + (c[2] - a[2])**2 - r**2
    bq = -2*((b[0] - a[0]) * (c[0] - a[0]) +
             (b[1] - a[1]) * (c[1] - a[1]) +
             (b[2] - a[2]) * (c[2] - a[2]))
    dq = bq**2 - 4*aq*cq
    if dq < 0:
        return None
    elif dq == 0:
        t = -bq / (2 * aq)
        return [a[0] + (b[0] - a[0]) * t,
                a[1] + (b[1] - a[1]) * t,
                a[2] + (b[2] - a[2]) * t]
    else:
        t1 = (-bq + m.sqrt(dq)) / (2 * aq)
        t2 = (-bq - m.sqrt(dq)) / (2 * aq)
        return ([a[0] + (b[0] - a[0]) * t1,
                 a[1] + (b[1] - a[1]) * t1,
                 a[2] + (b[2] - a[2]) * t1],
                [a[0] + (b[0] - a[0]) * t2,
                 a[1] + (b[1] - a[1]) * t2,
                 a[2] + (b[2] - a[2]) * t2]
                )


def main():
    figures = parse_file(sys.argv[1])
    res = find_intersection(figures["sphere"]["center"],
                            figures["line"][0],
                            figures["line"][1],
                            figures["sphere"]["radius"])

    if res is None:
        print("Коллизий не найдено")
    elif len(res) == 2:
        print(res[0])
        print(res[1])
    else:
        print(res)


if __name__ == "__main__":
    main()
