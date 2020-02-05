import re, sys

def strcmp(a, b):
    return "OK" if (re.compile(b.replace("*", ".*"))).match(a) else "KO"


def main():
    print(strcmp(sys.argv[1], sys.argv[2]))
    
if __name__ == "__main__":
    main()