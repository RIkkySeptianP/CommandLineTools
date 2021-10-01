import argparse


def runcommandtools():
    parser = argparse.ArgumentParser(description="Command Line Tools")


    parser.add_argument(
        'ffoldername',
        type=str,
        help="Enter your folder addr"
    )

    args = parser.parse_args()

    filename = args.ffoldername

    print("your folder name is {0}".format(filename))
    with open(filename) as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            count += 1
            print(f'line {count}: {line}')


if __name__ == '__main__':
    runcommandtools()


