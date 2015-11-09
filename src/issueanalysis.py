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


def getGitCommit(targetKey):
    datafilename = 'finalrepos.json'
    subdir = "data/"
    res = {}
    with open(datafilename) as data_file:
        data = json.load(data_file)
    for key in data:
        if key == targetKey:
            repo = data[key]
            url = repo["url"]
            src = repo["src"]
            issue = repo["issue"]
            directory = subdir + key.replace(" ", "_")
            directoryIssue = directory + "/issues/"
            directoryGit = directory + "/git/"
            issuefilename = 'closedrealissues.json'
            pullreqfilename = 'closedpullrequestissues.json'

            res[key] = []

            with open(directoryIssue + issuefilename) as dataIssueFile:
                issuedata = json.load(dataIssueFile)
            with open(directoryIssue + pullreqfilename) as dataIssueFile:
                issuedata += json.load(dataIssueFile)
            for issueevent in issuedata:
                if "commit_id" in issueevent:
                    if issueevent["commit_id"] != None:
                        commitHash = issueevent["commit_id"]
                        temp = subprocess_cmd('cd ' + directoryGit + '; git show --format=raw '+commitHash)
                        if "+++" in temp:
                            res[key].append(temp)
                        else : # c'est aussi un merge
                            if "commit" in temp:
                                parent = temp.split("\n")[0].split()[1]
                                merge = temp.split("\n")[2].split()[1]
                                commit = temp.split("\n")[3].split()[1]
                                temp = subprocess_cmd('cd ' + directoryGit + '; git diff --format=raw '+parent + " "+ merge)
                                res[key].append(temp)
                                temp = subprocess_cmd('cd ' + directoryGit + '; git diff --format=raw '+parent + " "+ commit)
                                res[key].append(temp)

            print(key + " :  done !")
    return res


def score(targetKey):
    a = getGitCommit(targetKey)
    res = {}
    for commit in a[targetKey]:
        ponderation = commit.count("public class")
        for line in commit.split("\n"):
            if "public class" in line:
                for iword, word in enumerate(line.split()):
                    if word == "public" and line.split()[iword+1] == "class":
                        klass = line.split()[iword+2]
                        if klass in res:
                            res[klass] += 100./ponderation
                        else:
                            res[klass] = 100./ponderation

    return res

if __name__ == '__main__':
    getGitCommit("lol")
    main()