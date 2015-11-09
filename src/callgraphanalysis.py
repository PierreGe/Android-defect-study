


def getDictClass(callGraphFile, restriction):
    res = {}
    with open(callGraphFile) as data_file:
            datas = data_file.readlines()
            for data in datas:
                data = data.strip()
                if data[:2] == "C:":
                    data = data[2:]
                    caller, called = data.split()
                    #if restriction in caller and restriction not in called and "android" in called:
                    if True:
                        if caller in res:
                            res[caller].append(called)
                        else:
                            res[caller] = [called]

    return res




def score(callgraphPath, packageName):
    graph = getDictClass(callgraphPath, packageName)

    res = {}
    for i in graph:
        caller = i.split(".")[-1].split("$")[-1] if "$" in i.split(".")[-1] else i.split(".")[-1]
        if caller in res:
            res[caller] += len(graph[i])*10
        else:
            res[caller] = len(graph[i])*10

    return res




if __name__ == '__main__':
    main()