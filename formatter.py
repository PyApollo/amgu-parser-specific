# GET_INITIALS = lambda string : "".join([x[0].upper() for x in string.split()]).replace('(','').replace(')','')
GET_INITIALS = lambda string : string.replace(" ","_").replace('(','').replace(')','')

class Formatter:
    def __init__(self):
        pass

    def format_array(self,array):
        array = map(str,array)
        return "-".join([GET_INITIALS(x) for x in array])

    def format_day(self,array):
        return ";".join([self.format_array(x) for x in array])

    def format_week(self,array):
        return [self.format_day(x) for x in array]
    


# print(format_array([1, 'Физическая культура', 'Будлов Андрей Александрович', 'Неизвестно', 'лекция']))