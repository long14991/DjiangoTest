from xml.etree import ElementTree as ET
xmltree = ET.parse('devices.xml')
root = xmltree.getroot()
for child in root:
    print(child.tag)
    print(child.text)

def getApkPath():
    for child in root:
        if child.tag=='apkPath':
            return child.text

def getPackageName():
    for child in root:
        if child.tag=='packageName':
            return child.text

def getActivityName():
    for child in root:
        if child.tag=='activityName':
            return child.text

def getTestId():
    for child in root:
        if child.tag=='testId':
            return child.text

def writeXML(packageName,activityName,apkPath,testId):
    for child in root:
        if child.tag=='activityName':
            child.text=activityName
        elif child.tag=='packageName':
            child.text=packageName
        elif child.tag=='apkPath':
            child.text=apkPath
        elif child.tag=='testId':
            child.text=testId
    xmltree.write('devices.xml')

