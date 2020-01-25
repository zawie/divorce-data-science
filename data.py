import csv
import random

def shuffle(X,y):
    size = len(X)
    new_X,new_y = [],[]
    for _ in range(size):
        r = random.randint(0,len(X)-1)
        new_X.append(X.pop(r))
        new_y.append(y.pop(r))
    return new_X,new_y

def get():
    x = [] #questions
    y = [] #divorce or no divorce
    with open('divorce.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        first = True
        for row in spamreader:
            if first:
                first = False
            else:
                string = row[0]
                str_elements = string.split(',')
                elements = []
                for el in str_elements:
                    elements.append(int(el))
                y.append(elements.pop()) #add divorce stat to y list
                x.append(elements)  #add input matrix
    return x,y

def get_shuffled():
    X,y = get()
    return shuffle(X,y)
