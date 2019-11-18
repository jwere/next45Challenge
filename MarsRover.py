class Rover():
    direction = ""
    xCoordinate = 0
    yCoordinate = 0
    validDirections = "NEWS"
    validCommands = "MLR"
    zoneWidth = 0
    zoneHeight = 0
    commands = ""

    # method that reads and validates the three lines of input from user
    def getUserInput(self):
        # first line of input
        while True:
            lineOne = input()
            zone = lineOne.split(" ")
            # check if first line contains 2 positive numbers seperated by a space
            if len(zone) == 2 and zone[0].isdigit() is True and zone[1].isdigit() is True\
                and int(zone[0]) > 0 and int(zone[1]) > 0:

                self.zoneWidth = int(zone[0])
                self.zoneHeight = int(zone[1])
                break
            else:
                print("Invalid zone-BOUNDARY: Enter zone-BOUNDARY again.")
        # second line of input
        while True:
            lineTwo = input()
            position = lineTwo.split(" ")
            # check if 2nd line contains a positive number and a valid direction seperated by a space
            if len(position) == 3 and position[0].isdigit() is True\
                 and position[1].isdigit() is True\
                    and self.validDirections.find(position[2]) > -1\
                        and int(position[0]) <= self.zoneWidth\
                             and int(position[1]) <= self.zoneHeight:

                    self.xCoordinate = int(position[0])
                    self.yCoordinate = int(position[1])
                    self.direction = position[2]
                    break
            else:
                print("Invalid start position or position out of range: Enter Position again.")
        # third line of input
        while True:
            runInputs = True
            lineThree = input()
            for c in lineThree:
                if self.validCommands.find(c) == -1:
                    print(c + " in "  + lineThree + " is not a valid command.")
                    print("Valid commands: M, L or R")
                    runInputs = False
                    break
            if runInputs is True:
                self.commands = lineThree
                break
   
   # method that enables Rover to move
    def move(self):
        if self.direction == "S" and self.yCoordinate > 0:
            self.yCoordinate -= 1
        elif self.direction == "N" and self.yCoordinate < self.zoneHeight:
            self.yCoordinate += 1
        elif self.direction == "E" and self.xCoordinate < self.zoneWidth:
            self.xCoordinate += 1
        elif self.direction == "W" and self.xCoordinate > 0:
            self.xCoordinate -= 1
    
    #method that enables Rover to rotate/change direction
    def rotate(self, rotate):
        if rotate == "L":
            if self.direction == "E":
                self.direction = "N"
            elif self.direction == "N":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "E"
        elif rotate == "R":
            if self.direction == "E":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "N"
            elif self.direction == "N":
                self.direction = "E"
   
    # method that enables Rover to do the survey 
    def survey(self):
        for c in self.commands:
            if c == "M":
                self.move()
            else:
                self.rotate(str(c))

#headquarters have a rover
class HQ():
    rover = Rover()
    roverPosition = ""

    #method that controls rover and returns rover position
    def controlRover(self):
        self.rover.getUserInput()
        self.rover.survey()
        self.roverPosition = str(self.rover.xCoordinate) + " " +\
             str(self.rover.yCoordinate) + " " + self.rover.direction
        return (self.roverPosition)

marsRover = HQ()
print(marsRover.controlRover())