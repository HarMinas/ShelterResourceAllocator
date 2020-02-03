'''
    First Line: 32 bit int = num beds in shelter <= 40
    Second Line: 32 bit int = num spaces in the parking lot
    Thrid Line: 32 bit int num applicants chosen by LAHSA so far
    Next L lines: L num of applicant IDs
    Next line: number of applicants chosen by SPLA so far 
    Next S lines: S num of applicant IDs
    Next Line: total number of applicants 
    Next A lines: a list of A applicant infos

    OUTPUT = next applicant chosen by SPLA: applicant ID (5 digits)

    info entered into the app 
    5 digit ID _ GENDER(M/F/O)__3 digit Age__PETS?__MedCond?__CAR?__DRVLCNS?__daysNeeded(7switches)
    
    Reqs 
    SLPA: Must have car and Driver License, but no medical conditions
    LAHSA: Shelter can only serve women over 17 without pets
'''



import support

'''These are the global variables that hold info'''
daysInWeek = 7
chosenByL = []
chosenByS = []

allApplicants = []
applicantsForS = []
applicatnsForBoth =[]
input = open('input3.txt','r')

numOfBeds = int(input.readline())
numOfSpots = int(input.readline())
beds = [numOfBeds] * daysInWeek
spots = [numOfSpots] * daysInWeek

numChosenByL = int(input.readline())
support.analyseApplicantsAccepted(chosenByL, input, numChosenByL)

numChosenByS = int(input.readline())
support.analyseApplicantsAccepted(chosenByS, input, numChosenByS)

numTotal = int(input.readline())
print(numTotal)
support.buildApplicants(allApplicants, input, numTotal)

#deletes the applicatns from the total list that are already chosen by LAHSA and modifies the beds array
support.delOnesChosen(allApplicants, beds, chosenByL)

#deletes the applicatns from the total list that are already chosen by SHA and modifies the beds array
support.delOnesChosen(allApplicants, spots, chosenByS)

support.separateApplicants(allApplicants, applicantsForS, applicatnsForBoth)

print("applicantsForS:",  applicantsForS)
print("applicantsForBoth:",  applicatnsForBoth)
print("allApplicants: ", allApplicants)
print(chosenByL)
print(chosenByS)
print(allApplicants)
#print(allApplicants)



superset = []

support.addToSuperset(superset, applicatnsForBoth, applicantsForS)



superset.sort(key = lambda x: x.value, reverse = True)

for applicant in superset:
    print(applicant.value, applicant.ID, applicant.days, applicant.partOf)
print("spots: ", spots)
print("max value is: ", numOfSpots * 7)

nextPick = support.findNextPick(superset, spots)
if nextPick != None:
    print(nextPick.ID)
else:
    print("no applicant could be chosen because there are not enough resources for accomodation")    


totalValue = 0
for spot in spots:
    totalValue += (numOfSpots - spot)

print("spots: ", spots)
print("max value is: ", numOfSpots * 7)
print("value: ", totalValue)