

import numpy as np
import json
import matplotlib.pyplot as plt




def main():

    finaldatafile = "finaldata.json"
    finalData = None
    try:
        with open(finaldatafile) as data_file:
            finalData = json.load(data_file)
    except:
        print("Run analysis")
        exit()

    for appliName in finalData:
        cgscore, issuescore, classSize = finalData[appliName]
        j = 0
        issueVallueForGraph = []
        cgValueForGraph = []

        for key in issuescore:
            if key in cgscore:
                for k in range(int(issuescore[key]*1000)):
                    issueVallueForGraph.append(j)
                for k in range(int(cgscore[key]*1000)):
                    cgValueForGraph.append(j)
                j+=1

        if j>3:

            plt.hist(issueVallueForGraph, bins=j, histtype='stepfilled', normed=True, color='r', label='Issue')
            plt.hist(cgValueForGraph, bins=j, histtype='stepfilled', normed=True, color='b', alpha=0.5, label='Calls')
            titleplt = appliName + " (pearsonr="+ str(pearsonCorrelationCoefficient) + ")"
            plt.title(titleplt)
            plt.xlabel("Class")
            plt.ylabel("Value")
            plt.legend()
            subfolder = "newgraph"
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
            plt.savefig(subfolder + "/result" + appliName + ".png")
            plt.close()
        else:
            print("FAILURE : " + appliName)


if __name__ == '__main__':
    main()