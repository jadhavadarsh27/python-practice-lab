class student:
    def __init__(self):
        self.__marks=80

    def get_marks(self):
        return self.__marks

s = student()
print(s.get_marks())
