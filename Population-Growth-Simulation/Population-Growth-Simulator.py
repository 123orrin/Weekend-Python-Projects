"""
Population Growth Simulator
Adapted by Orrin Dahanaggamaarachchi
Originally by Sitif: https://siti2718f.medium.com/building-simulations-in-python-a-step-by-step-walkthrough-a3972729027c

This program simulates population growth based on the set of conditions specified below. It calculates basic statistics and exports the data into an excel sheet where the user can conduct analysis. 
"""

import random
import xlwt
from xlwt import Workbook
import time
import statistics

# Initialize Excel Sheet
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

# variables
initialPopulation = 10000
endPopulation = 1000000
year = 0

infantMortality = 7
agriculture = 4
disasterChance = 0
fertilityLowerBound = 25
fertilityUpperBound = 60
intelligence = 80

food = 0

peopleList = []

# Person Object
class Person():
    def __init__(self, age, intelligence):
        self.age = age
        self.gender = random.randint(0, 1) # 0 is male, 1 is female
        self.intelligence = intelligence

# Functions
def Harvest(food, agriculture):
    ablePeople = 0
    researchPeople = 0
    for person in peopleList:
        if person.age > 16 and person.intelligence < intelligence:
            ablePeople += 1
        elif person.age > 20 and person.intelligence >= intelligence:
            researchPeople += 1

    agriculture += 0.001 * researchPeople
    food += ablePeople * agriculture

    if food < len(peopleList):
        del peopleList[0:int(len(peopleList) - food)]
        food = 0
    else:
        food -= len(peopleList)


def School():
    for person in peopleList:
        if 5 < person.age < 18:
            person.intelligence += random.randint(-5, 10)


def Reproduce(fertilityLowerBound, fertilityUpperBound, infantMortality):
    for person in peopleList:
        if person.gender == 1:
            if fertilityLowerBound < person.age < fertilityUpperBound:
                if random.randint(0, 4) == 0:
                    if random.randint(0, 100) > infantMortality:
                        peopleList.append(Person(0, random.randint(10, 50)))


def Age():
    for person in peopleList:
        if person.age > random.randint(80, 100):
            peopleList.remove(person)
        else:
            person.age += 1


def Disaster(disasterChance):
    if random.randint(0, 100) < disasterChance:
        del peopleList[0: int(random.uniform(0.05, 0.2) * len(peopleList))]


def RunYear(food, agriculture, fertilityLowerBound, fertilityUpperBound, 
            infantMortality, disasterChance):
    School()
    Harvest(food, agriculture)
    Reproduce(fertilityLowerBound, fertilityUpperBound, infantMortality)
    Disaster(disasterChance)
    Age()

    global year
    year += 1

    print("Year: " + str(year) + ", " + "Population: " + str(len(peopleList)))
    sheet1.write(year, 0, year)
    sheet1.write(year, 1, len(peopleList))

    infantMortality *= 0.985
    return infantMortality


def BeginSim(year, initialPopulation):
    print("Year: " + str(year) + ", " + "Population: " + str(initialPopulation))
    sheet1.write(year, 0, year)
    sheet1.write(year, 1, initialPopulation)

    for x in range(initialPopulation):
        peopleList.append(Person(random.randint(18, 50), random.randint(10, 100)))


# Run Simulation
BeginSim(year, initialPopulation)
while len(peopleList) < endPopulation and len(peopleList) > 1:
    infantMortality = RunYear(food, agriculture, fertilityLowerBound, 
                              fertilityUpperBound, infantMortality, disasterChance)


# Calculate Statistics
def CalculateStats():
    maxIntelligence = 0
    minIntelligence = 0
    intelligenceList = []

    for person in peopleList:
        intelligenceList.append(person.intelligence)

        if person.intelligence > maxIntelligence:
            maxIntelligence = person.intelligence
        if person.intelligence < minIntelligence:
            minIntelligence = person.intelligence

    meanIntelligence = statistics.mean(intelligenceList)
    medianIntelligence = statistics.median(intelligenceList)
      
    sheet1.write(0, 3, "Min Intelligence")
    sheet1.write(1, 3, minIntelligence)

    sheet1.write(3, 3, "Max Intelligence")
    sheet1.write(4, 3, maxIntelligence)

    sheet1.write(6, 3, "Mean Intelligence")
    sheet1.write(7, 3, meanIntelligence)

    sheet1.write(9, 3, "Median Intelligence")
    sheet1.write(10, 3, medianIntelligence)

CalculateStats()

# Save Simulation Data to Excel File
wb.save('populationGrowth.xls')
