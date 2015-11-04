
import getpass
import requests
import json
import copy
import os
import time
from bs4 import BeautifulSoup

class GitHubAPI():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._rateLimit = None
        self._rateRemaining = None
        self._rateReset = None

    def get(self, url , payload = None):
        if not payload:
            r = requests.get(url, auth=(self._user, self._password))
        else:
            r = requests.get(url, auth=(self._user, self._password), params=payload)
        self._rateLimit = r.headers['X-RateLimit-Limit']
        self._rateRemaining = r.headers['X-RateLimit-Remaining']
        if int(self._rateRemaining) < 10:
            print("Going to sleep for an hour waiting for GitHub . Zzzzzzzzz")
            time.sleep(3600)
        self._rateReset = r.headers['X-RateLimit-Reset']
        print("Rate Limit : " + self.getLimit())
        return r.text

    def getLimit(self):
        return (self._rateRemaining + "/" + self._rateLimit)

    def getAllIssue(self,url):
        r = requests.get(url, auth=(self._user, self._password))
        self._rateLimit = r.headers['X-RateLimit-Limit']
        self._rateRemaining = r.headers['X-RateLimit-Remaining']
        self._rateReset = r.headers['X-RateLimit-Reset']
        print("Rate Limit : " + self.getLimit())
        res = json.loads(r.text)
        nextp,last = r.headers["Link"].split(",")
        nexturl = nextp.split(";")[0].strip().replace("<","").replace(">","")
        lasturl = last.split(";")[0].strip().replace("<","").replace(">","")
        print(r.headers["Link"])
        print(nexturl)
        print(lasturl)

        while nexturl != lasturl:
            r = requests.get(nexturl, auth=(self._user, self._password))
            self._rateLimit = r.headers['X-RateLimit-Limit']
            self._rateRemaining = r.headers['X-RateLimit-Remaining']
            self._rateReset = r.headers['X-RateLimit-Reset']
            print("Rate Limit : " + self.getLimit())
            res += json.loads(r.text)
            print(r.headers["Link"])
            nextp,last,first,prev = r.headers["Link"].split(",")
            nexturl = nextp.split(";")[0].strip().replace("<","").replace(">","")
            lasturl = last.split(";")[0].strip().replace("<","").replace(">","")
            print(r.headers["Link"])
            print(nexturl)
            print(lasturl)


        r = requests.get(nexturl, auth=(self._user, self._password))
        self._rateLimit = r.headers['X-RateLimit-Limit']
        self._rateRemaining = r.headers['X-RateLimit-Remaining']
        self._rateReset = r.headers['X-RateLimit-Reset']
        print("Rate Limit : " + self.getLimit())
        res += json.loads(r.text)
        print(r.headers["Link"])
        first,prev = r.headers["Link"].split(",")
        nexturl = nextp.split(";")[0].strip().replace("<","").replace(">","")
        lasturl = last.split(";")[0].strip().replace("<","").replace(">","")
        print(r.headers["Link"])
        print(nexturl)
        print(lasturl)

        return res



def MakeIssuesFile():
    user = "PierreGe"
    passord = getpass.getpass(str(user) + "'s password : ")
    api = GitHubAPI(user, passord)


    filename = 'finalrepos.json'
    with open(filename) as data_file:
        data = json.load(data_file)

    subdir = "data/"
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]

        directory = subdir + key.replace(" ", "_")
        directory += "/issues/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        baseUrl = issue
        baseUrl = baseUrl.replace("https://github.com/", "https://api.github.com/repos/")
        #baseUrl += "?state=closed"
        print(baseUrl)

        result = api.getAllIssue(baseUrl)
        print(len(result))
        print("_"*100)

        filename = "openissues.json"
        with open(directory + filename , 'w') as fp:
            json.dump(result, fp)


def main():

    user = "PierreGe"
    passord = getpass.getpass(str(user) + "'s password : ")
    api = GitHubAPI(user, passord)

    #url = "https://api.github.com/repos/asksven/BetterBatteryStats/issues/699/events"

    #js = json.loads(api.get(url, {"scopes":"closed_by"}))
    #print(js)

    resultRL = {}
    resultPR = {}

    datafilename = 'finalrepos.json'
    with open(datafilename) as data_file:
        data = json.load(data_file)
    total = 0


    subdir = "data/"
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        resultRL = []
        resultPR = []

        directory = subdir + key.replace(" ", "_")
        directory += "/issues/"

        issuefilename = 'closedissues.json'
        with open(directory + issuefilename) as data_file:
            issuedata = json.load(data_file)

        for issue in issuedata:
            js = json.loads(api.get(issue["events_url"]))
            if "pull_request":
                resultPR += js
            else:
                resultRL += js

        filenameRI = "closedrealissues.json"
        with open(directory + filenameRI , 'w') as fp:
            json.dump(resultRL, fp)
            print("-"*100)
            print("DONE FOR A FILE")

        filenamePR = "closedrealissues.json"
        with open(directory + filenamePR , 'w') as fp:
            json.dump(resultPR, fp)


if __name__ == "__main__":
    main()