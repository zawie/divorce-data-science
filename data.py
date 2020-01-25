import csv
 
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