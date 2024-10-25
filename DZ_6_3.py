class Horse:
    x_distance = 0
    sound = 'Frrrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.x_distance += dx
        self.y_distance += dy

    def get_post(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_post())

p1.move(10 , 15)
print(p1.get_post())
p1.move(-5, 20)
print(p1.get_post())

p1.voice()
