import callgraphanalysis
import issueanalysis
import json
import csv

def getData():
    finaltarget = [('OsmAnd Parking','net.osmand.parkingPlugin'),
               ('Conversations','eu.siacs.conversations'),
               ('AntennaPod',"de.danoeh.antennapod"),
               ('OsmAnd Contour lines','net.osmand.srtmPlugin'),
               ('BetterBatteryStats','com.asksven.betterbatterystats'),
               ('Mozilla Stumbler','org.mozilla.mozstumbler'),
               ('ownCloud','com.owncloud.android'),
               ('MPDroid','com.namelessdev.mpdroid'),
               ('andFHEM','li.klass.fhem'),
               ('OpenKeychain','org.sufficientlysecure'),
               ('AnkiDroid','com.ichi2'),
               ('AdAway','org.adaway'),
               ('PPSSPP','org.ppsspp'),
               ('OsmAnd~','net.osmand')]
    finaltarget.remove(('PPSSPP','org.ppsspp'))
    finaltarget.remove(('OsmAnd Parking','net.osmand.parkingPlugin'))
    #finaltarget = [('AntennaPod',"de.danoeh.antennapod")]

    finaldatafile = "finaldata.json"
    finalData = None
    try:
        with open(finaldatafile) as data_file:
            finalData = json.load(data_file)

    except:
        res = {}
        for appliName, signature in finaltarget:
            cgscore = callgraphanalysis.scoreApiCall("data/" + appliName.replace(" ", "_") + "/callGraph/callgraph.txt", signature)
            classSizescore = callgraphanalysis.scoreClassSize("data/" + appliName.replace(" ", "_") + "/callGraph/callgraph.txt",signature)
            issuescore = issueanalysis.score(appliName)
            res[appliName] = [cgscore,issuescore,classSizescore]
        finalData = res

        with open('finaldataconj.csv', 'w') as csvfile:
            fieldnames = ['Application', 'class', 'Number_Api_Calls','Class_Size', 'Issue_Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for appli in res:
                cgscore,issuescore,classSizescore = res[appli]
                merge = []
                for i in cgscore:
                    if i in issuescore:
                        if i in classSizescore:
                            merge.append(i)
                for klass in merge:
                    nbrCalls = cgscore[klass] if klass in cgscore else 0
                    klassSize = classSizescore[klass] if klass in classSizescore else 0
                    IssueScore = issuescore[klass] if klass in issuescore else 0
                    writer.writerow({'Application': appli, 'class': klass, 'Number_Api_Calls': nbrCalls, "Class_Size" : klassSize, "Issue_Score": IssueScore})

        with open(finaldatafile, "w") as data_file:
            json.dump(finalData,data_file)
    return finalData

def main():

    getData()


if __name__ == '__main__':
    main()