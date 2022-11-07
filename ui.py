import calendar
from datetime import datetime
import os
import logic


def showMenuAndGetChoice(menuItems):
    isBadChoise = False
    while True:
        os.system('cls')
        if isBadChoise:
            print('!!!', 'Не допустимое значение - ' + str(choice), "!!!")
            isBadChoise = False
        for menuItem in range(len(menuItems)):
            print(menuItem, '-', menuItems[menuItem])
        choice = input("Выберете действие:")
        isBadChoise = logic.checkBadChoise(choice, 0, len(menuItems)-1)
        if not isBadChoise:
            return int(choice)


def getMainMenuItems():
    menuItems = [
        'Выход',
        'Показать расписание',
        'Показать домашнее задание',
        'Добавить домашнее задание'
    ]
    return menuItems

def getScheduleMenuItems():
    menuItems = [
        'Выход в предыдущее меню',
        'Показать расписание на сегодня',
        'Показать расписание на завтра',
        'Показать расписание на эту неделю'
    ]
    return menuItems

# def getHomeTaskMenuItems():
#     menuItems = [
#         'Выход в предыдущее меню',
#         'Показать Д/З на сегодня',
#         'Показать Д/З на завтра',
#         'Показать Д/З на эту неделю',
#         'Показать Д/З на следующую неделю',
#     ]
#     return menuItems


############ SHOW SCHEDULE ############
def showDailySchedule(schedule, dayNum, lessons):
    print('~'*27)
    day = calendar.day_name[dayNum-1]
    print(f'         {day}')
    print('~'*27)
    for item in schedule:
        if(int(item[0]) == dayNum):
            lesson = logic.getLessonName(item[2], lessons)
            print(f"| №{item[1]} | {lesson}")
            print('-'*27)
    
    
def showScheduleWeek(schedule, lessons):
    if(len(schedule) > 0):
        for i in range(8):
            showDailySchedule(schedule, i, lessons)
            print()


def showHomeTask(tasks, lessons):
    os.system('cls')
    todayStr = datetime.today().strftime('%Y%m%d')

    for item in tasks:
        if(int(item[0]) >= int(todayStr)):
            print('-'*50)
            lesson = logic.getLessonName(item[1], lessons)
            print(f"{item[0]} {lesson} {item[2]}")
    print('-'*50)
    

# def getDate():
#     # TODO: 
#     date = ""
#     return date


# def editSchedule(schedule, date):
#     # TODO:
#     pass


def addHomeTask(tasks, lessons):
    date = input('Введите дату в формате ггггммдд: ')
    for i in lessons:
       print(i)
    lessonId = input('Введите номер предмета: ')
    text = input('Введите домашнее задание: ')
    record = [date, lessonId, text]
    tasks.append(record)
    