import tello    # Don't forget to import tello module

t = tello.tello()

t.take_off()
t.delay(3)
t.forward(50)
t.back(50)
t.left(50)
t.right(50)
t.up(50)
t.down(50)
t.flip("f")
t.cw(180)
t.ccw(180)
t.land()
