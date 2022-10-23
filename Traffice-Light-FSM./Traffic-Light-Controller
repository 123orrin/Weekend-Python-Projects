from enum import Enum
import time

class TrafficLightStates(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 3

class TrafficLight():
    def __init__(self, name):
        self.name = name
        self.State = TrafficLightStates.RED
        self.previousState = None
        self.counter = 0.0

    def toGreen(self, otherLight):
        if otherLight.State == TrafficLightStates.RED and time.time() - self.counter > 5 and self.previousState != TrafficLightStates.GREEN:
            time.sleep(0.5)
            self.previousState = self.State
            self.State = TrafficLightStates.GREEN
            self.counter = time.time()
            print(f"{self.name} changed to {self.State.name}")
    
    def toYellow(self):
        if time.time() - self.counter > 5 and self.State == TrafficLightStates.GREEN and self.previousState != TrafficLightStates.YELLOW:
            self.previousState = self.State
            self.State = TrafficLightStates.YELLOW
            self.counter = time.time()
            print(f"{self.name} changed to {self.State.name}")

    def toRed(self):
        if time.time() - self.counter > 2 and self.State == TrafficLightStates.YELLOW and self.previousState != TrafficLightStates.RED:
            self.previousState = self.State
            self.State = TrafficLightStates.RED
            self.count = time.time()
            print(f"{self.name} changed to {self.State.name}")

    def changeState(self, otherLight):
        self.toRed()
        self.toYellow()
        self.toGreen(otherLight)

def runSim():
    northLight = TrafficLight("northLight")
    eastLight = TrafficLight("eastLight")

    count = 1
    while count < 100:
        northLight.changeState(eastLight)
        eastLight.changeState(northLight)
        time.sleep(0.5)
        count += 1
    
    print("The simulation is now done")
    return 1

if __name__ == '__main__':
    runSim()
