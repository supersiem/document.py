import os
def getlengt():
    file = document
    file_path = file

    with open(file_path, "r") as f:
       num_lines = 0
       for line in f:
            num_lines += 1


    
    return num_lines
def read_full():
    file = document
    openfile = open(file)
    re = openfile.read()
    openfile.close()
    return re

def read_line(num):
    file = document
    openfile = open(file)
    re = openfile.read()
    openfile.close()
    return re

def write_to_line(line, input):
    #krijg de lengte van het bestand
    file = document
    file_lengt = getlengt(file)
    file_line = line - 1
    
    
    #maak lijst klaar
    list = []
    #maak back up
    loop = 1
    #backup = ""
    while loop <= file_lengt:
        #voeg line toe aan lijst
        list.append(get(loop, file))
        #backup = backup + get(loop, file)
        #volgende line
        loop += 1
    #over wite de line van de list
    if len(list)==0:
        list.append(1)
    if 1 == 1:
        list[file_line] = input + "/n"
    else:
        list[file_line] = input
    ##print(list)
    list2=[]
    loop =0 
    while loop != len(list):
        if loop == file_line:
            list2.append(input)
        else:
            list2.append(list[loop])
        loop+=1


    loop =0 
    out = ""
    while loop != len(list2):
        out += list2[loop]
        loop += 1
    f = open(file, "w")
    f.write(out)
    f.close()
    
def overwrite(data):
     f = open(document, "w")
     f.write(data)
     f.close()
     return data

def set_doc(file):
    global document
    document = file
    if os.path.exists(document):
        return
    else:
        document = ''
        return 404


def make(name):
    if not os.path.exists(name):
         open(name, "x")
    set_doc(name)
    
def delete():
    if os.path.exists(document):
      return os.remove(document)
    else:
     return 404