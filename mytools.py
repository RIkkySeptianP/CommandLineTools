import argparse
from pathlib import Path
import json



def runcommandtools():
    parser = argparse.ArgumentParser(description="Command Line Tools")


    parser.add_argument(
        'ffoldername',
        type=str,
        help="Enter your log folder addr"
    )

    parser.add_argument(
        '-t',
        type=str,
        help="Select your format file json or text, if none or not both of them will be plaintext"
    )

    parser.add_argument(
        '-o',
        type=str,
        help="Select your output folder, if none output will be at"
    )

    args = parser.parse_args()

    filename = args.ffoldername
    typefile = args.t
    if typefile == "json" or typefile == "text":
        pass
    else:
        typefile = "text"

    if typefile == "text":
        fileext = "txt"
    else:
        fileext = "json"
    outputfilename = args.o if args.o else "mytools.{0}".format(fileext)

    print("your folder name is {0} and yor type {1}".format(filename, typefile))
    fle = Path(outputfilename)
    fle.touch(exist_ok=True)
    with open(filename) as file:
        lines = file.readlines()
        count = 0
        data = {}
        text = ""
        data['data'] = []
        for line in lines:
            count += 1
            if fileext == "json":
                data['data'].append({
                    'count': f'{count}',
                    'text': f'{line}'
                })
            else:
                text += f'{line}\n'
        if fileext == "json":
            with open(outputfilename, 'w') as outfile:
                json.dump(data, outfile)
        else:
            with open(outputfilename, 'w') as the_file:
                the_file.write(f'{text}\n')


if __name__ == '__main__':
    runcommandtools()


