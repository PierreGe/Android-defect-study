
import requests
from bs4 import BeautifulSoup
import json
import copy



def getDict():
    baseUrl = "https://f-droid.org/repository/browse/?fdpage=PAGENUMBER"
    result = {}
    appDone = 0
    lastpage = 56

    for pagnbr in range(1,lastpage+1):
        url = baseUrl.replace("PAGENUMBER", str(pagnbr))
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for aTag in soup.find_all('a'):
            if 'id="appheader"' in str(aTag):
                targetRepo = str(aTag['href'])
                repoPage = requests.get(targetRepo)
                repoSoup = BeautifulSoup(repoPage.text, 'html.parser')
                for span in repoSoup.find_all('span'):
                    if 'style="font-size:20px' in str(span):
                        key = span.string
                result[key] = {}
                result[key]["url"] = targetRepo
                for paragraph in repoSoup.find_all('p'):
                    if "Issue Tracker" in str(paragraph) or "Source Code" in str(paragraph):
                        for i,el in enumerate(paragraph):
                            if "Issue Tracker" in str(el):
                                try :
                                    result[key]["issue"] = str(list(paragraph)[i+2]['href'])
                                except:
                                    pass
                            if "Source Code" in str(el):
                                try :
                                    result[key]["src"] = str(list(paragraph)[i+2]['href'])
                                except:
                                    pass

                appDone +=1
                print("Number of app parsed : " + str(appDone) + "/" + str(lastpage*30))

    return result

def fdroidjson():
    data = getDict()
    with open('datafdroido.json', 'w') as fp:
        json.dump(data, fp)

def githubjson():
    with open('datafdroid.json') as data_file:
        data = json.load(data_file)

    result = {}
    for key in data:
        if "src" in data[key] and "issue" in data[key]:
            if "github.com" in data[key]["src"] and "github.com" in data[key]["issue"]:
                result[key] = copy.deepcopy(data[key])

    with open('datagithubrepos.json', 'w') as fp:
        json.dump(result, fp)

def jirajson():
    with open('datafdroid.json') as data_file:
        data = json.load(data_file)

    result = {}
    i = 0
    for key in data:
        i+=1
        print(str(i) + "/" + str(len(data)))
        if "src" in data[key] and "issue" in data[key]:
            if not ("github.com" in data[key]["src"] and "github.com" in data[key]["issue"]):
                try :
                    page = requests.get(data[key]["issue"])
                    if len([i for i in range(len(page.text)) if page.text.startswith('jira', i)]) > 10:
                        result[key] = copy.deepcopy(data[key])
                except:
                    pass

    with open('datajirarepos.json', 'w') as fp:
        json.dump(result, fp)

if __name__ == "__main__":
    #fdroidjson()
    #githubjson()
    jirajson()