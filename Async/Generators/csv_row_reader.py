import csv
import sys
from typing import Generator


def csv_row_reader(file_path: str) -> Generator[list[str], None, None]:
    with open(file_path, 'r') as csv_file:
        for row in csv.reader(csv_file):
            yield row


def main() -> None:
    reader: Generator[list[str], None, None] = csv_row_reader('data.csv')
    print(next(reader))

    while True:
        try:
            for i in range(3):
                print(next(reader))
            input('Continue retrieving rows?')
        except StopIteration as e:
            print('No more rows..')
            sys.exit()  # To make sure we shouldn't get stuck in this infinite loop


if __name__ == "__main__":
    main()
