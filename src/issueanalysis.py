import subprocess
import json
import os
from os import listdir
from os.path import isfile, join

def subprocess_cmd(commands):
    process = subprocess.Popen(commands,stdout=subprocess.PIPE,stderr=subprocess.PIPE ,shell=True)
    proc_stdout = process.communicate()[0].strip()
    process.wait()
    return proc_stdout


def getGitCommit():
    datafilename = 'finalrepos.json'
    subdir = "data/"
    res = {}
    with open(datafilename) as data_file:
        data = json.load(data_file)
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        directory = subdir + key.replace(" ", "_")
        directoryIssue = directory + "/issues/"
        directoryGit = directory + "/git/"
        issuefilename = 'closedrealissues.json'

        res[key] = []

        with open(directoryIssue + issuefilename) as dataIssueFile:
            issuedata = json.load(dataIssueFile)
        for issueevent in issuedata:
            if "commit_id" in issueevent:
                if issueevent["commit_id"] != None:
                    commitHash = issueevent["commit_id"]
                    temp = subprocess_cmd('cd ' + directoryGit + '; git show --format=raw '+commitHash)
                    res[key].append(temp)

        print(key + " :  done !")
        if "nten" in key:
            return res
    return res


def score():
    a = getGitCommit()
    res = {}
    for commit in a["AntennaPod"]:
        for line in commit.split("\n"):
            if "public class" in line:
                for iword, word in enumerate(line.split()):
                    if word == "public" and line.split()[iword+1] == "class":
                        klass = line.split()[iword+2]
                        if klass in res:
                            res[klass] += 1
                        else:
                            res[klass] = 1

    return res

if __name__ == '__main__':
    main()