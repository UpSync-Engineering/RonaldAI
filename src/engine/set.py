import sys
import getopt


if __name__ == "__main__":

    openai__ = ""
    argv = sys.argv[1:]
    try:
        options, args = getopt.getopt(argv, "openai:", ["openai = "])
    except:
        print("Error")

    for name, value in options:
        if name in ['-openai', '--openai__']:
            openai__ = value

    print(openai__)
    print("Argument list:", str(sys.argv))
