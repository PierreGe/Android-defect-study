
import getpass
import requests
import json
import copy
from bs4 import BeautifulSoup

class GitHubAPI():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._rateLimit = None
        self._rateRemaining = None
        self._rateReset = None

    def get(self, url):
        r = requests.get(url, auth=(self._user, self._password))
        self._rateLimit = r.headers['X-RateLimit-Limit']
        self._rateRemaining = r.headers['X-RateLimit-Remaining']
        self._rateReset = r.headers['X-RateLimit-Reset']
        print("Rate Limit : " + self.getLimit())
        return r.text

    def getLimit(self):
        return (self._rateRemaining + "/" + self._rateLimit)

def main():
    user = "PierreGe"
    passord = getpass.getpass(str(user) + "'s password : ")
    api = GitHubAPI(user, passord)
    baseUrl = ""
    js = json.loads(api.get(baseUrl))





if __name__ == "__main__":
    selectMoreThanOnePageIssue()