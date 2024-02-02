import datetime
import argparse
import os
import re


NOTES_DIR = './notes'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', type=str)
    args = parser.parse_args()

    if args.create:
        # Remove any directory traversal characters from user input
        sanatized_input = re.sub(r'[.\/\\]', '', args.create)

        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

        now = datetime.datetime.now()
        filename = now.strftime('%Y-%m-%d_%r') + '_' + sanatized_input + '.md'
        with open(os.path.join(NOTES_DIR, filename), 'w') as f:
            f.write(sanatized_input + '\n')
        print('notes created: ', filename)


if __name__ == '__main__':
    main()
