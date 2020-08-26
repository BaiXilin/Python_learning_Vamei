class Human():
    def _init_(self, input_gender):
        self.gender = input_gender
    def print_gender(self):
        print self.gender

li_lei = Human('male')
li_lei.print_gender()