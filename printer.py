class Printer:
    def __init__(self,*,group_id,old_schedule=None,new_schedule,weekday):
        self.group_id = group_id
        self.old = old_schedule
        self.new = new_schedule
        self.weekday = weekday
    def telegram_message(self):
        string = '''
❗️ Изменения в расписании
Группа : {}
День недели : {}
Новое расписание - 
        {}
        '''.format(
            self.group_id,self.weekday,self.insert_day(self.new)
        ).replace('\n\n','\n')
        return string
    def insert_lesson(self,lesson):
        string = '''
Номер пары : {}
Дисциплина : {}
Преподаватель : {}
Аудитория : {}
Тип занятия : {} 
        '''.format(*lesson)
        return string
    def insert_day(self,day):
        string = ''
        for i in day:
            string += self.insert_lesson(i)
        return string