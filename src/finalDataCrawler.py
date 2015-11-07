import subprocess
import json
import os
from os import listdir
from os.path import isfile, join



def subprocess_cmd(commands):
    process = subprocess.Popen(commands,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    process.wait()
    return proc_stdout

def getJarFiles():
    datafilename = 'finalrepos.json'
    subdir = "data/"
    with open(datafilename) as data_file:
        data = json.load(data_file)
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        directory = subdir + key.replace(" ", "_")
        directoryApk = directory + "/apk/"
        directoryJar = directory + "/jar/"
        if not os.path.exists(directoryJar):
            os.makedirs(directoryJar)
        onlyfiles = [ f for f in listdir(directoryApk) if isfile(join(directoryApk,f)) ]
        for apk in onlyfiles:
            if ".apk" in str(apk):
                res = subprocess_cmd('sh ../tools/dex2jar-2.0/d2j-dex2jar.sh ' + directoryApk + apk)
        print(res)

def getCallGraph():
    datafilename = 'finalrepos.json'
    subdir = "data/"
    with open(datafilename) as data_file:
        data = json.load(data_file)
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        directory = subdir + key.replace(" ", "_")
        directorycallGrah = directory + "/callGraph/"
        if not os.path.exists(directorycallGrah):
            os.makedirs(directorycallGrah)
        directoryJar = directory + "/jar/"
        issuefilename = 'closedrealissues.json'
        onlyfiles = [ f for f in listdir(directoryJar) if isfile(join(directoryJar,f)) ]
        for jar in onlyfiles:
            if ".jar" in str(jar):
                res = subprocess_cmd('java -jar ../tools/javacg-0.1-SNAPSHOT-static.jar ' + directoryJar + jar)
                with open(directorycallGrah + "callgraph.txt" , 'w') as fp:
                        fp.write(res)



if __name__ == '__main__':
    #getGitCommit()
    #getJarFiles()
    getCallGraph()