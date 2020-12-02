#!/usr/bin/env python

import csv
from datetime import datetime

class Scheduler:

    def __init__(self, name):
        self.name = name
        self.dateOffset = 12
        self.titleOffset = 0
        self.ind = 0
        self.CalculateOffset()

    def CalculateOffset(self):
        with open(self.name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if(len(row[1]) > self.titleOffset):
                    self.titleOffset = len(row[1]) + 2
                if(int(row[0]) > self.ind):
                    self.ind = int(row[0])
            csvfile.close()

    def ShowTasks(self):
        line = 0
        self.SortByColumn()
        with open(self.name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                if(line == 0):
                    print(row[0], " ", row[1]," "*(self.dateOffset) ,row[2], " "*(self.titleOffset - 6), row[3])
                else:
                    print(row[0], "  ", row[1], " ", row[2], " "*(self.titleOffset - len(row[2])), row[3])
                line += 1
            csvfile.close()

    def SortByColumn(self, col=0, order=False):

        with open(self.name, 'r') as inp:
            csv_reader = csv.reader(inp, delimiter=',')
            header = next(csv_reader)
            if(col == 1):
                s = sorted(csv_reader, key=lambda x:datetime.strptime(x[1],"%Y-%m-%d %H:%M"), reverse=order)
            if(col == 0):
                s = sorted(csv_reader, key=lambda x:x[0], reverse=order)   
            inp.close()
        
        lines = []

        with open(self.name, 'w') as out:
            writer = csv.writer(out)
            lines.append(header)
            for row in s:
                lines.append(row)
            writer.writerows(lines)
            out.close()
    

            
    def DeleteTask(self, k):
        lines = []

        with open(self.name, 'r') as inp:
            reader = csv.reader(inp)
            for row in reader:
                if row[0] != str(k):
                    lines.append(row)
            inp.close()

        with open(self.name, 'w') as out:
            writer = csv.writer(out)
            writer.writerows(lines)
            out.close()

    def AddTask(self, task):
        task = str(self.ind + 1) + "," + task
        task = task.split(',')
        lines = []

        with open(self.name, 'r') as inp:
            reader = csv.reader(inp)

            for row in reader:
                lines.append(row)

            inp.close()

        lines.append(task)

        with open(self.name, 'w', newline='') as out:
            writer = csv.writer(out)
            writer.writerows(lines)
            out.close()
        
        self.SortByColumn()


def instruction():
    print("This is scheduler for your task.")
    print("If you want to see tasks enter: 1")
    print("If you want to sort task by id column enter: 2")
    print("If you want to sort task by date and time column enter: 3")
    print("If you want to add new row enter: 4")
    print("If you want to delete row by id enter: 5")
    print("If you need instructions eneter: 6")
    print("If you want to close program enter: 7")



if __name__ == "__main__":
    s = Scheduler("tasks.csv")
    instruction()
    while(True):
        print("")
        print("")
        x = int(input("Enter the number."))
        if(x == 1):
            s.ShowTasks()
        if(x == 2):
            s.SortByColumn()
            s.ShowTasks()
        if(x == 3):
            s.SortByColumn(1)
            s.ShowTasks()
        if(x == 4):
            y = str(input("Enter your task date & time, title and description in that format: [YYYY-MM-DD HH:MM],[Title],[Description]"))
            s.AddTask(y)
        if(x == 5):
            y = int(input("Enter row id that you want to delete."))
            s.DeleteTask(y)
        if(x == 6):
            instruction()
        if(x == 7):
            break
            