'''Harutyun Minasyan'''


'''applicant object definition'''
class applicant:
    ID = None
    value = None
    days = None
    partOf = None
    def __init__(self, applicant, fromSet):
        self.partOf = fromSet
        self.ID = applicant[:5]
        self.days = applicant[13:20]
        self.value = 0
        for day in self.days:
            if day == '1':
                self.value += 1


def analyseApplicantsAccepted(arr, file, num):
    for line in range(num):
        line = file.readline()
        id = line[:5]
        arr.append(id)


def buildApplicants(arr, file, num):
    for line in range(num):
        line = file.readline()
        arr.append(line)


def delOnesChosen(totalList, resources, info):
    for id in info:
        itemIndex = findItemIndex(totalList, int(id), 0, (len(totalList)))
        applicantInfo = totalList.pop(itemIndex)
        modifyDaysOfResource(resources, applicantInfo)
        

#Performs binary search based on the IDs of the applicants in the list to match
#The value passed in. 
#StartIndex and Endindex are the two beginning and the ending of the list. 
#Uses recursion to solve the problem on subproblems
def findItemIndex(list, value, startIndex, endIndex):
    middleIndex = ((endIndex-startIndex) /2) + startIndex
    id = int((list[middleIndex])[:5])
    if value == id:
        return middleIndex
    elif value > id:
        return findItemIndex(list, value, middleIndex, endIndex)
    elif value < id:
        return findItemIndex(list, value, 0, middleIndex)

    

#takes the information about the client and modifies the resources table. Takes the days that 
#are already used out of the picture
def modifyDaysOfResource(resources, item):
    days = item[13:20]
    i = 0
    for c in days:
        if c == '1':
            resources[i] = resources[i] - 1
        i = i + 1
        
   
            
#This function will take in the two lists, one where only applicants go that can be chosen by only S, 
# and the other that will store applicants that can be picked by both L and S. The totalList is taken to 
# analyze.
def separateApplicants(totalList, onlyS, both):
    for applicant in totalList:
        if applicant[10] == 'N' and applicant[11] == 'Y' and applicant[12] == 'Y':
            if applicant[5] =='F' and applicant[9] == 'N' and int(applicant[6:9]) > 17:
                both.append(applicant)
            else:
                onlyS.append(applicant)


#Takes the list of string version of applicant definition and turns them into objects containting
# applicant objects. 
def addToSuperset(superset, applcantListForBoth, applicantListForS):

    for a in applcantListForBoth:
        superset.append(applicant(a, "SandL"))
    for a in applicantListForS:
        superset.append(applicant(a, "S"))




#The choosing Engine is made up of several funcions. 
#First the applicant with highest value is chosen 
#Then days array of an applicant are compared against the available days.
def isCompatible(applicant, parkingSpots):
    for i in range(7):
        if parkingSpots[i] == 0 and applicant[i] == '1': 
            return False
    return True

def selectApplicant(selected, parkingSpots, applicant):
    selected.append(applicant)
    for i in range(7):
        if applicant.days[i] == '1':
            parkingSpots[i] -= 1   

def findNextPick(superset, parkingSpots):
    selectedApplicants = []
    for applicant in superset:
        if isCompatible(applicant.days, parkingSpots):
            selectApplicant(selectedApplicants, parkingSpots, applicant)

    for applicant in selectedApplicants:
        if applicant.partOf == "SandL":
            return applicant



'''global variables'''
daysInWeek = 7

chosenByL = []
chosenByS = []

allApplicants = []
applicantsForS = []
applicatnsForBoth =[]
input = open('input.txt','r')

numOfBeds = int(input.readline())
numOfSpots = int(input.readline())

beds = [numOfBeds] * daysInWeek
spots = [numOfSpots] * daysInWeek

numChosenByL = int(input.readline())
analyseApplicantsAccepted(chosenByL, input, numChosenByL)

numChosenByS = int(input.readline())
analyseApplicantsAccepted(chosenByS, input, numChosenByS)


numTotal = int(input.readline())
buildApplicants(allApplicants, input, numTotal)


input.close()


#deletes the applicatns from the total list that are already chosen by LAHSA and modifies the beds array
delOnesChosen(allApplicants, beds, chosenByL)

#deletes the applicatns from the total list that are already chosen by SHA and modifies the beds array
delOnesChosen(allApplicants, spots, chosenByS)

separateApplicants(allApplicants, applicantsForS, applicatnsForBoth)



superset = []

addToSuperset(superset, applicatnsForBoth, applicantsForS)



superset.sort(key = lambda x: x.value, reverse = True)





nextPick = findNextPick(superset, spots)


output = open('output.txt', 'w+')

if nextPick != None:
    output.write(nextPick.ID)

  



