from datetime import datetime
import os
import ui
import file


def mainLogic(schedule, tasks, lessons):
    if len(schedule) == 0:
        schedule = file.readSchedule()
    if len(tasks) == 0:
        tasks = file.readTasks()
    if len(lessons) == 0:
        lessons = file.readLessons()
    while True:
        choice = ui.showMenuAndGetChoice(ui.getMainMenuItems())
        
        # Показать расписание
        if choice == 1:
            showSchedule(schedule, tasks, lessons)

        # Показать домашнее задание
        elif choice == 2:
            ui.showHomeTask(tasks, lessons)

        # Добавить домашнее задание
        elif choice == 3:
            ui.addHomeTask(tasks, lessons)
            file.saveTasks(tasks) 
        
        # Редактировать расписание
        # elif choice == 4:
        #     date = ui.getDate()
        #     ui.editSchedule(schedule, date)
        #     file.saveSchedule(schedule)
        #     file.saveTasks(tasks)

        elif choice == 0:
            exit(0)
        
        input("Press Enter to continue...")
    


def showSchedule(schedule, tasks, lessons):
    while True:
        choice = ui.showMenuAndGetChoice(ui.getScheduleMenuItems())
        os.system('cls')
         # Показать расписание на сегодня
        if choice == 1:
            dayNum = datetime.today().isoweekday()
            ui.showDailySchedule(schedule, dayNum, lessons)

        # Показать расписание на завтра
        elif choice == 2:
            day = datetime.today()
            dayNum = (day.isoweekday()+1)%7
            ui.showDailySchedule(schedule, dayNum, lessons)

        # Показать расписание на эту неделю
        elif choice == 3:
            ui.showScheduleWeek(schedule, lessons)
        
        # Выход в предыдущее меню
        elif choice == 0:
            mainLogic(schedule, tasks, lessons)
        
        input("Press Enter to continue...")
        
    


def checkBadChoise(input, min, max):
    # Проверка на не цифры
    try:
        input = int(input)
    except:
        return True
    # Проверка числового значения на попадание в диапазон
    if input < min or input > max:
        return True
    else: 
        return False

def getLessonName(lessNum, lessons):
     for item in lessons:
        if(item[0] == lessNum):
            return item[1]
     return '-Предмет не найден-'
    