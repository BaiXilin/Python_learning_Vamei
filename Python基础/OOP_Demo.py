class Bird():
    have_feather = True
    way_of_production = 'egg'
    def move(self, dx, dy): # method defined inside an object must include 'self' for self-reference
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print summer.way_of_production
print summer.move(5, 8)

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print summer.have_feather
print summer.move(5, 8)