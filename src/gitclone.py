import base64
import os
import json

# base64.encodestring(s)
# base64.decodestring(s)

subdir = "data/"

def main():
    filename = 'finalrepos.json'
    with open(filename) as data_file:
        data = json.load(data_file)

    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        directory = subdir + key.replace(" ", "_")
        directory += "/apk"
        if not os.path.exists(directory):
            os.makedirs(directory)


def getGit(data):
    for key in data:
        repo = data[key]
        url = repo["url"]
        src = repo["src"]
        issue = repo["issue"]
        directory = subdir + key.replace(" ", "_")
        directory += "/git"
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.system("git clone " + src + " " + directory)


if __name__ == '__main__':
    main()