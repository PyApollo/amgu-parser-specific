import sqlite3

class Database:
    def __init__(self):
        self.create_db()


    def create_db(self):
        with sqlite3.connect('database.db') as connection:
            cur = connection.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS schedule(
                    group_name TEXT NOT NULL,
                    mon TEXT NOT NULL,
                    tue TEXT NOT NULL,
                    wed TEXT NOT NULL,
                    thu TEXT NOT NULL,
                    fri TEXT NOT NULL,
                    sat TEXT NOT NULL,
                    sun TEXT NOT NULL
                    )'''
            )
            connection.commit()
    
    def get_schedule(self,group_id):
        with sqlite3.connect('database.db') as connection:
            cur = connection.cursor()
            result = cur.execute(
                ''' SELECT * FROM schedule WHERE group_name='{}'
                '''.format(group_id)
            )
            return result.fetchone()

    def update(self,group_id,new_schedule):
        sql_schedule = [f"'{x}'" for x in new_schedule]
        sql_schedule.insert(0, group_id)
        sql_schedule = ",".join(sql_schedule)
        with sqlite3.connect('database.db') as connection:
            cur = connection.cursor()
            cur.execute(
                '''DELETE FROM schedule WHERE group_name={}
                '''.format(group_id)
            )
            cur.execute(
                '''INSERT INTO schedule VALUES ({})
                '''.format(sql_schedule)
            )
            connection.commit()