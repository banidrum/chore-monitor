import sys, csv

def main():
    file = open('chores.csv', "a")

    with open('chores.csv', newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in reader:
            print(', '.join(row))

    file.write(input() + "\n" + "\n")

    file.close()

main()    