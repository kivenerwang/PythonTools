#!/usr/bin/python
#_*_ coding:utf-8 _*_  
import os

findCount = 0
findId = "E:/project"
findDir = "/data/ijkplayer/"
newString = "/data/ijkplayer"

resultFile = os.path.join(findDir,"result.txt")


def writeResultAndPrint(fullPath,content):
    print (fullPath)
    file = open(fullPath,'w')
    file.write(content)
    file.close()


def findKey(fullPath):
    file = open(fullPath,'r')
    content = file.read()
    file.close()
    print('content', content)
    deleteFirstLine(fullPath,content)
    #print("findId", findId, '---content', content,'---content.find(findId)', content.find(findId))
    if content.find(findId) == 0:
        global findCount
        newString = "/data/ijkplayer"
        findCount = findCount + 1
        print('content', content)
        newString = content.replace(findId, newString)
        print("newString", newString)
        writeResultAndPrint(fullPath, newString)



def deleteFirstLine(fullPath, content):
    stinglist = content.split('\n')
    print('newcontent', stinglist[0])
    newcontent = stinglist[0]
    writeResultAndPrint(fullPath, newcontent)


def findFiles():
    for dirPath,dirNames,fileNames in os.walk(findDir):
        for file in fileNames:
            if (file.find("*.sh")):
                fullPath = os.path.join(dirPath,file)
                #findKey(fullPath)
                modifyFileType(fullPath)
    print("找到了字符串个数=" + str(findCount))

def clean():
    if os.path.exists(resultFile):
        os.remove(resultFile)

def modifyFileType(fielPah):
    os.system("dos2unix " + fielPah)

clean()
findFiles()
