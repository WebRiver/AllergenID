import requests
import re
import checker

def generateURL(foodName):
    start = "https://api.nal.usda.gov/ndb/search/?format=json&ds=Branded+Food+Products&q="
    end = "&sort=r&max=10&offset=0&api_key=SW5yC8FS6YfGlesX7P2s7vcM6yKVJ2WEPv0PXjxt"
    output = ""
    for i in range(len(foodName)):
        if foodName[i] == " ":
            output += "+"
        else:
            output+=foodName[i]
    return start + output + end


def getFoodList(query):
    url = generateURL(query)
    jOut = requests.get(url).json()
    itemList = jOut['list']['item']
    outList = []
    for foodItem in itemList:
        outList.append({'name':foodItem['name'], 'no':foodItem['ndbno']})
    return outList

def getNames(foodList):
    outlist = []
    for item in foodList:
        item['name']
    return outlist

def getIngredients(ndbno):
    startUrl = "https://api.nal.usda.gov/ndb/reports/?ndbno="
    endUrl = "&type=b&format=json&api_key=SW5yC8FS6YfGlesX7P2s7vcM6yKVJ2WEPv0PXjxt"
    url = startUrl + str(ndbno) + endUrl
    jOut = requests.get(url).json()
    return jOut['report']['food']['ing']['desc']


def integrate(ings):
    my_str = str(ings).lower()
    delims = ",", "(", ")"
    regexPattern = '|'.join(map(re.escape, delims))
    ings_str = re.split(regexPattern, my_str)
    ans = checker.check(ings)
    return ans


# print(getFoodList("nut harvest almonds"))
# print(str(getIngredients(45078606)).split(","))
# my_str = str(getIngredients(45078606)).lower()
# pattern = re.compile("^\s+|\s*,\s*|\s+$")
# print([x.split("(") for x in pattern.split(my_str) if x])
# delims = ",", "(", ")"
# regexPattern = '|'.join(map(re.escape, delims))
# ings = re.split(regexPattern, my_str)
# ans = checker.check(ings)



# print re.split(',', my_str)
