#deel 1: #https://dodona.be/nl/courses/5447/series/67762/activities/1284696370/
class Session:
    def __init__(self, team, trainer, field, timeslot: str): #constructor
        self.team == team
        self.trainer == trainer
        self.field == field
        self.timeslot == timeslot
    def __str__(self):
        return f"{self.team} -> {self.timeslot} with {self.trainer} on {self.field}" #voor de print(self)
    def conflicts_with(self, other_session): #T: conflict, F: geen conflict
        return self.timeslot == other_session.timeslot and (self.trainer == other_session.trainer or self.field == other_session.field)
if __name__ == '__main__': #test cases
    s1 = Session("U10", "Sara", "Field 1", "Mon 18-19")
    s2 = Session("U12", "Tom", "Field 2", "Wed 19-20")
    schedule = []
    schedule.append(s1)
    schedule.append(s2)
    print(s1)
    print(s2)
#deel 2: https://dodona.be/nl/courses/5447/series/67762/activities/516420910/
def read_csv_single_column(path, column_name):
    inputFile = open(path, "r")
    header = inputFile.readline() #header apart zodat we de index kunnen vinden van column_name: de hoeveelste kolom is column_name?
    header.strip("\n")
    header.split(",")
    count = 0
    while header[count] != column_name:
        count += 1
    index = count #kijken op welke index (= in welke kolom) onze column_name staat, voor de gegeven excel files is dit altijd 0
    data = inputFile.readlines()
    kolomlijst = []
    for row in data:
        gestript = data.strip('\n') #\n weg
        gestript2 = gestript.strip(' ') #spaties weg
        gesplit = gestript2.split(',') #splitsen in een lijst obv komma's (CSV)
        kolomlijst.append(gesplit[index]) #toevoegen aan de lijst als het op de "index" plaats in de row staat
    for element in kolomlijst: #verwijder lege waarden
        if len(element) == 0:
            kolomlijst.remove(element)
    for i in kolomlijst: #verwijder dubbels
        for j in kolomlijst:
            if kolomlijst[i] == kolomlijst[j] and i != j:
                kolomlijst.remove(lijst[j])
    return kolomlijst

if __name__ == '__main__': #test cases
    #teams.csv, trainers.csv, fields.csv, timeslots.csv
    teamslist = read_csv_single_column(teams.csv, 'team')
    print(teamslist)
    trainerslist = read_csv_single_column(trainers.csv, 'trainer')
    print(trainerslist)
    fieldslist = read_csv_single_column(fields.csv, 'field')
    print(fieldslist)
    timeslotslist = read_csv_single_column(timeslots.csv, 'timeslot')
    print(timeslotslist)

#deel 3: https://dodona.be/nl/courses/5447/series/67762/activities/1566615416/
#FUNCTION Backtrack(state):
 #   IF state is a complete solution:
  #      record or return solution
   #     RETURN true

    #FOR each choice in possibleChoices(state):
     #   IF choice is valid for state:
      #      apply(choice, state)

       #     IF Backtrack(state) == true:
        #        RETURN true    // stop bij eerste oplossing
         #           // of: ga door, als je ALLE oplossingen wil

          #  undo(choice, state)    // restore state

    #RETURN false
def is_valid_session(new_session, schedule): #T = geen conflict; F: conflict
    for session in schedule:
        if conflicts_with(new_session, session):
            return False
    return True
def plan_trainings(teams, i, schedule, trainers, fields, timeslots):
    if i == len(teams):
        return True
    else:
        for trainer in trainers:
            for field in fields:
                for timeslot in timeslots:
                    tempsession = Session(team[i], trainer, field, timeslot) #over alle mogelijkheden gaan
                    for session in schedule:
                        count = 0
                        if is_valid_session(tempsession, session):
                            count += 1
                        if count == len(schedule): #als het compatible is met alle sessions momenteel in schedule
                            schedule.append(tempsession)
                            plan_trainings(teams, i+1, schedule, trainers, fields, timeslots)
    schedule == schedule[0:len(schedule)-i] #remove previously added schedules if no match in iteration i
    return False

def create_schedule(teams, trainers, fields, timeslots):
    schedule = []
    if plan_trainings(teams, 0, schedule, trainers, fields, timeslots):
        for session in schedule:
            print(session) #alle sessions printen, zie __str__(self)
    else:
        print("Er is geen geldige planning mogelijk")

if __name__ == '__main__': #test cases
    teamslist = read_csv_single_column(teams.csv, 'team')
    trainerslist = read_csv_single_column(trainers.csv, 'trainer')
    fieldslist = read_csv_single_column(fields.csv, 'field')
    timeslotslist = read_csv_single_column(timeslots.csv, 'timeslot')
    create_schedule(teamslist, trainerslist, fieldslist, timeslotslist)





































