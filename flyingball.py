class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self):
       print(f"{self.x}, {self.y}")

    def move(self):
        self.x += 1
        self.y += 1

if __name__=="__main__":
    c = Circle(10, 100, 100)

    window_width = 500
    window_height = 500

    vx = 1
    vy = 1

    for i in range(1000):
        c.move(vx, vx)
        c.draw()

        if c.x < window_width:
            vx = -vx
            

