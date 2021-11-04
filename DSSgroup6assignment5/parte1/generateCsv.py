import csv
import random

def truncate(n):
    return int(n*100) / 100

def generateCSV(file, customersNumber, capacity):

        with open(file, 'w') as csv_file:
            filewriter = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([customersNumber])
            filewriter.writerow([capacity])
            filewriter.writerow(['id', 'x', 'y', 'd'])

            for i in range(customersNumber):
                x = truncate(random.uniform(0,100))
                y = truncate(random.uniform(0,100))
                d = random.randint(0, capacity)
                filewriter.writerow([i, x, y, d])
