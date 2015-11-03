import getpass
import requests
import json
import copy
from bs4 import BeautifulSoup


def findNbrIssues():
    filename = 'datagithubrepos.json'
    result = {}
    with open(filename) as data_file:
        data = json.load(data_file)

    i = 0
    for key in data:
        i+=1
        print(str(i) + "/" + str(len(data)))
        baseUrl = data[key]["issue"]
        baseUrl = baseUrl.replace("https://github.com/", "https://api.github.com/repos/")
        baseUrl += "?state=closed"
        try :
            js = json.loads(api.get(baseUrl))
            result[key] = copy.deepcopy(data[key])
            result[key]["number-issue"] = len(js)
        except:
            pass

    with open("new" + filename , 'w') as fp:
        json.dump(result, fp)


def selectMoreThanOnePageIssue():
    filename = 'usabledatagithubrepos.json'
    result = {}
    with open(filename) as data_file:
        data = json.load(data_file)
    for key in data:
        if "number-issue" in data[key]:
            if int(data[key]["number-issue"]) > 500:
                result[key] = copy.deepcopy(data[key])

    print(str(len(result)) + "/" + str(len(data)))
    with open("new" + filename , 'w') as fp:
        json.dump(result, fp)

def findCloseIssue():
    filename = 'newnewdatagithubrepos.json'
    result = {}
    with open(filename) as data_file:
        data = json.load(data_file)
    i = 0
    for key in data:
        if "number-issue" in data[key]:
            i+=1
            print("Repo numéro : " + str(i))
            result[key] = copy.deepcopy(data[key])
            r = requests.get(result[key]["issue"])
            soup = BeautifulSoup(r.text, 'html.parser')
            for aTag in soup.find_all('a'):
                if "is%3Aissue+is%3Aclosed" in str(aTag):
                    string = str(aTag)[str(aTag).find("</span>"): str(aTag).find("</a>")]
                    nbr = int(''.join(c for c in string if c.isdigit()))
                    result[key] = copy.deepcopy(data[key])
                    result[key]["number-issue"] = nbr
                    print(nbr)

    with open("new" + filename , 'w') as fp:
        json.dump(result, fp)