import click
import os
import csv
import re
from prettytable import PrettyTable


packageDir = ".\package"

mostMessagedServer = 0
mostUsedWord = 0
mostMessagesOnDate = ""
emojisUsed = {"kekw": 5, "lol": 10, "monkaS": 15}  # dummy data


@ click.command()
def main():
    messages = {"21-0-0": 0}
    cumulativeChars = 0
    cumulativeWords = 0

    for path, subdirs, files in os.walk(packageDir+"\messages"):
        for name in files:
            if name.endswith(".csv"):
                with open(os.path.join(path, name), "r", encoding='cp437') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        messages[row[0]] += 1
                        cumulativeChars += len(row[2])
                        cumulativeWords += len(re.findall(r'\w+', row[2]))

    cumulativeMessages = sum(messages.values)

    table = PrettyTable(['Stat', 'Value'])
    table.add_row(['Cumulative Messages', "{:,}".format(
        cumulativeMessages) + " messages"])
    table.add_row(['Average Message Length [characters]', str(round(
        cumulativeChars/cumulativeMessages, 2)) + " characters"])
    table.add_row(['Average Message Length [words]', str(round(
        cumulativeWords/cumulativeMessages, 2)) + " words"])
    table.add_row(["Chattiest Day", mostMessagesOnDate])

    print(table)
    print("Due to certain limitations on Discord's end, the name of the servers in the stats cannot be printed but their ID's can.")


if __name__ == '__main__':
    main()