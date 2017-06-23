class grade:
    def __init__(self):
        self.__private()                    #self._grade__private()
        self.public()
    def __private(self):
        print('grade_private')
    def public(self):
        print('grade_public')

class GPA(grade):
    def __private(self):                    #self._GPA__private()
        print('gpa_private')
    def public(self):
        print('gpa_public')

a = GPA()
a._GPA__private()
a.public()