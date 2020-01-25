import csv
import random

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

def split(num_train):
    x_test,y_test = get()
    x_train, y_train = [],[]
    for i in range(num_train):
        size = len(x_test)
        r = random.randint(0,size-1)
        x_train.append(x_test.pop(r))
        y_train.append(y_test.pop(r))
    return  x_train,y_train,x_test,y_test