import numpy as np
import json
from scipy.stats.stats import pearsonr, spearmanr, kendalltau, kstest
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std



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
        issueCallgraphValueForStats = []
        callGraphValueForStats = []

        issueSizeValueForStats = []
        classSizeValueForStats = []
        
        issueForModel = []
        callGraphForModel = []
        classSizeForModel = []

        for key in issuescore:
            if key in cgscore:
                j+=1
                issueCallgraphValueForStats.append(issuescore[key])
                callGraphValueForStats.append(cgscore[key])

        for key in issuescore:
            if key in classSize:
                issueSizeValueForStats.append(issuescore[key])
                classSizeValueForStats.append(classSize[key])
                
        for key in issuescore:
            if key in classSize:
                if key in cgscore:
                    issueForModel.append(issuescore[key])
                    callGraphForModel.append(cgscore[key])
                    classSizeForModel.append(classSize[key])

        if j>3:
            spearmanCorrelationCoefficient, spearmanpvalue = spearmanr(issueCallgraphValueForStats,callGraphValueForStats)
            kendalltauCorrelationCoefficient, kendalltaupvalue = kendalltau(issueCallgraphValueForStats,callGraphValueForStats)
            kstestdissueValueForStats, kstestpvalueissueValueForStats = kstest([issuescore[key] for key in issuescore],"norm")
            kstestdcgValueForGraph, kstestpvaluecgValueForGraph = kstest([cgscore[key] for key in cgscore],"norm")

            spearmanCorrelationCoefficient2, spearmanpvalue2 = spearmanr(issueSizeValueForStats,classSizeValueForStats)
            kendalltauCorrelationCoefficient2, kendalltaupvalue2 = kendalltau(issueSizeValueForStats,classSizeValueForStats)
            kstestdchissueSizeValueForStats, kstestpvaluechissueSizeValueForStats = kstest([issuescore[key] for key in issuescore],"norm")
            kstestdclassSizeValueForStats, kstestpvalueclassSizeValueForStats = kstest([classSize[key] for key in classSize],"norm")

            print(appliName)
            print("--- API Call <> Issue")
            print(" "*8 + "Spearman rho correlation coefficient = " + str(spearmanCorrelationCoefficient))
            print(" "*8 + "Spearman p-value = " + str(spearmanpvalue))
            print(" "*8 + "Kendall Tau = " + str(kendalltauCorrelationCoefficient))
            print(" "*8 + "Kendall p-value = " + str(kendalltaupvalue))
            print(" "*8 + "KS Test D = " + str(kstestdissueValueForStats))
            print(" "*8 + "KS p-value = " + str(kstestpvalueissueValueForStats))
            print(" "*8 + "KS Test D = " + str(kstestdcgValueForGraph))
            print(" "*8 + "KS p-value = " + str(kstestpvaluecgValueForGraph))
            print(" "*8 + "dataset size =" + str(j))
            print("--- Class Size <> Issue")
            print(" "*8 + "Spearman rho correlation coefficient = " + str(spearmanCorrelationCoefficient2))
            print(" "*8 + "Spearman p-value = " + str(spearmanpvalue2))
            print(" "*8 + "Kendall Tau = " + str(kendalltauCorrelationCoefficient2))
            print(" "*8 + "Kendall p-value = " + str(kendalltaupvalue2))
            print(" "*8 + "KS Test D = " + str(kstestdchissueSizeValueForStats))
            print(" "*8 + "KS p-value = " + str(kstestpvaluechissueSizeValueForStats))
            print(" "*8 + "KS Test D = " + str(kstestdclassSizeValueForStats))
            print(" "*8 + "KS p-value = " + str(kstestpvalueclassSizeValueForStats))

            y = issueForModel
            X = np.array([callGraphForModel,classSizeForModel]).transpose()
            X = list([list(i) for i in X])
            model = sm.OLS(y, X)
            results = model.fit()
            print(results.summary(yname="issues", xname =("APIcalls", "ClassSize")))

        else:
            print("FAILURE : " + appliName)

    print("|" * 80)
    print("-" * 80)
    print("-" * 80)
    print("|" * 80)

    issueForGlobalModel = []
    callGraphForGlobalModel = []
    classSizeForGlobalModel = []
    issueGlobalCallgraphValueForStats = []
    callGlobalGraphValueForStats = []
    NOissueGlobalCallgraphValueForStats = []
    issueGlobalSizeValueForStats = []
    classGlobalSizeValueForStats = []

    anova1issue = []
    anova2issue = []
    for appliName in finalData:
        cgscore, issuescore, classSize = finalData[appliName]
        for key in issuescore:
            if key in classSize:
                if key in cgscore:
                    issueForGlobalModel.append(issuescore[key])
                    callGraphForGlobalModel.append(cgscore[key])
                    classSizeForGlobalModel.append(issuescore[key])

        for key in issuescore:
            if key in cgscore:
                j+=1
                issueGlobalCallgraphValueForStats.append(issuescore[key])
                callGlobalGraphValueForStats.append(cgscore[key])
            else:
                NOissueGlobalCallgraphValueForStats.append(issuescore[key])

        for key in cgscore:
            if key in issuescore:
                anova1issue.append(cgscore[key])
            else:
                anova2issue.append(cgscore[key])


        for key in issuescore:
            if key in classSize:
                issueGlobalSizeValueForStats.append(issuescore[key])
                classGlobalSizeValueForStats.append(classSize[key])


    spearmanGlobalCorrelationCoefficient, spearmanpvalueGlobal = spearmanr(issueGlobalCallgraphValueForStats,callGlobalGraphValueForStats)
    kendalltauGlobalCorrelationCoefficient, kendalltaupvalueGlobal = kendalltau(issueGlobalCallgraphValueForStats,callGlobalGraphValueForStats)

    spearmanGlobalCorrelationCoefficient2, spearmanpvalue2Global = spearmanr(issueGlobalSizeValueForStats,classGlobalSizeValueForStats)
    kendalltauGlobalCorrelationCoefficient2, kendalltaupvalue2Global = kendalltau(issueGlobalSizeValueForStats,classGlobalSizeValueForStats)


    fvalueanova1, pvalueanova1 = f_oneway(issueGlobalCallgraphValueForStats, NOissueGlobalCallgraphValueForStats)

    fvalueanova2, pvalueanova2 = f_oneway(anova1issue, anova2issue)

    print(len(NOissueGlobalCallgraphValueForStats))
    print("--- Correlation : API Call <> Issue")
    print(" "*8 + "Spearman rho correlation coefficient = " + str(spearmanGlobalCorrelationCoefficient))
    print(" "*8 + "Spearman p-value = " + str(spearmanpvalueGlobal))
    print(" "*8 + "Kendall Tau = " + str(kendalltauGlobalCorrelationCoefficient))
    print(" "*8 + "Kendall p-value = " + str(kendalltaupvalueGlobal))
    print(" "*8 + "ANOVA F-value = " + str(fvalueanova1))
    print(" "*8 + "ANOVA p-value = " + str(pvalueanova1))
    print(" "*8 + "ANOVA F-value = " + str(fvalueanova2))
    print(" "*8 + "ANOVA p-value = " + str(pvalueanova2))
    print("--- Correlation : Class Size <> Issue")
    print(" "*8 + "Spearman rho correlation coefficient = " + str(spearmanGlobalCorrelationCoefficient2))
    print(" "*8 + "Spearman p-value = " + str(spearmanpvalue2Global))
    print(" "*8 + "Kendall Tau = " + str(kendalltauGlobalCorrelationCoefficient2))
    print(" "*8 + "Kendall p-value = " + str(kendalltaupvalue2Global))


    print("_"*80)
    print("_"*80)
    print("-- GLOBAL OLS --")
    y = issueForGlobalModel
    X = np.array([callGraphForGlobalModel,classSizeForGlobalModel]).transpose()
    X = list([list(i) for i in X])
    X = sm.add_constant(X,prepend=False)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary(yname="issues", xname =("APIcalls", "ClassSize", "const")))


    print("API CALLS only")
    X = callGraphForGlobalModel
    X = sm.add_constant(X,prepend=False)
    model2 = sm.OLS(y, X)
    results = model2.fit()
    print(results.summary(yname="issues",xname =["APIcalls","const"]))
    print("Size only")
    X = classSizeForGlobalModel
    X = sm.add_constant(X,prepend=False)
    model3 = sm.OLS(y, X)
    results = model3.fit()
    print(results.summary(yname="issues",xname =["ClassSize","const"]))

if __name__ == '__main__':
    main()