import os
def getlengt():
    file = document
    file_path = file

    with open(file_path, "r") as f:
       num_lines = 0
       for line in f:
            num_lines += 1


    
    return num_lines
def get(num):
    file = document
    openfile = open(file)
    loop = 1
    while loop != num:
        returning = openfile.readline()
        loop += 1
    re = openfile.readline()
    openfile.close()
    return re

def write(regel, input, nieuwen_regel):
    #krijg de lengte van het bestand
    file = document
    file_lengt = getlengt(file)
    file_regel = regel - 1
    
    
    #maak lijst klaar
    list = []
    #maak back up
    loop = 1
    #backup = ""
    while loop <= file_lengt:
        #voeg regel toe aan lijst
        list.append(get(loop, file))
        #backup = backup + get(loop, file)
        #volgende regel
        loop += 1
    #over wite de regel van de list
    if len(list)==0:
        list.append(1)
    if nieuwen_regel == 1:
        list[file_regel] = input + "/n"
    else:
        list[file_regel] = input
    ##print(list)
    list2=[]
    loop =0 
    while loop != len(list):
        if loop == file_regel:
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
    
def set_doc(file):
    global document
    document = file


def make(name):
    open(name, "x")
    set_doc(name)
    
def delete():
    if os.path.exists(document):
      return os.remove(document)
    else:
     return 404