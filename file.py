import codecs


def readTasks():
    with codecs.open('db\homeTasks.txt', 'r', 'utf-8') as file:
        line = file.readline()
        homeTask = []
        if len(line) != 0:
            line = file.readline()
            while len(line) > 0:
                line = line.replace('\r', '').replace('\n', '')
                record = line.split(';')
                homeTask.append(record)
                line = file.readline()
    return homeTask
    

def readSchedule():
    with codecs.open('db\schedule.txt', 'r', 'utf-8') as file:
        line = file.readline()
        schedule = []
        if len(line) != 0:
            line = file.readline()
            while len(line) > 0:
                line = line.replace('\r', '').replace('\n', '')
                record = line.split(';')
                schedule.append(record)
                line = file.readline()
    return schedule

def readLessons():
    with codecs.open('db\lessons.txt', 'r', 'utf-8') as file:
        line = file.readline()
        lessons = []
        if len(line) != 0:
            line = file.readline()
            while len(line) > 0:
                line = line.replace('\r', '').replace('\n', '')
                record = line.split(';')
                lessons.append(record)
                line = file.readline()
    return lessons

def saveTasks(tasks):
    with codecs.open('db\homeTasks.txt', 'w', 'utf-8') as file:
        file.write("#Дата;Номер предмета;Д/з\n")
        for record in range(len(tasks)):
            for item in range(len(tasks[record])):
                file.write(str(tasks[record][item]).strip())
                if item != len(tasks[record])-1:
                    file.write(';')
            if record != len(tasks)-1:
                file.write('\n')


# def saveSchedule(schedule):
#     #День недели;Номер урока;Номер предмета
#     pass
