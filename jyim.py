#TODO: manage the recursive search function so it can handle many ways/subways

def searchProcess(name, process):
    liste = []
    for p in process:
        if name in p[2]:
            list1 = [p]
            for pneed in p[1]:
                list1.extend(searchProcess(pneed, process))
            liste.extend(list1)
            break
    return liste

def mainProgram(stock, process, optimize, val):
    lista = []

    print process
    # for st in optimize:
    #     if st in stock:
            # lst = searchProcess(st, process)
            # lst.reverse()
            # lista = [lst]
            # print st
