import inflect
from datetime import timedelta
import datetime as dt
p = inflect.engine()

class Student:
    def __init__(self, total_date):
        self.total_date = total_date
        print(self.total_date)

    
    @classmethod
    def get(cls):
        birth_date = input("Date of Birth: ")
        year, months, day = birth_date.split("-")
        year, months, day = int(year), int(months), int(day)
        birth_date = dt.datetime(year, months, day)
        current_date =  dt.datetime.now()
        total_date = (current_date - birth_date)*24
        num, string = total_date.split(" ")
        into_words = p.number_to_words(int(num))
        return cls(into_words)

def main():
    print(Student.get())

main()