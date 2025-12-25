import argparse
from formbricks.up import up
from formbricks.down import down
from formbricks.generate import generate
from formbricks.seed import seed

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    fb = sub.add_parser("formbricks")
    fb_sub = fb.add_subparsers(dest="action")

    fb_sub.add_parser("up")
    fb_sub.add_parser("down")
    fb_sub.add_parser("generate")
    fb_sub.add_parser("seed")

    args = parser.parse_args()

    if args.command != "formbricks":
        parser.error("Invalid command")

    match args.action:
        case "up":
            up()
        case "down":
            down()
        case "generate":
            generate()
        case "seed":
            seed()
        case _:
            fb.print_help()

if __name__ == "__main__":
    main()
