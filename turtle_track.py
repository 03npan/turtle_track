import turtle

def track(t, color):
  t.begin_fill()
  t.color(color)
  t.circle(250)
  t.end_fill()
  t.up()
  t.left(90)
  t.forward(60)
  t.right(90)
  t.color("green")
  t.down()
  t.begin_fill()
  t.circle(200)
  t.end_fill()
  t.color("yellow")
  t.right(90)
  t.forward(60)
  t.up()
  t.color("orange")
  for i in range(0,2):
    t.left(90)
  t.forward(300)
  t.left(90)
  t.forward(115)
  t.write("Farrell's Track!", font = ("Arial",30, "normal"))
  t.color("blue")
  t.left(90)
  t.forward(270)
  t.left(90)
  t.forward(114)
  t.down()


def main():
  t = turtle.Turtle()
  t.speed(50)
  track(t, "black")

  print("Move the turtle around the race track to get the fastest time, while staying on the track!")
  print("Here are your controls:")
  
  print("W: To move forward\nS: To move backwards\nA: To move left\nD: To move right\nQ: To quit")
  while True:
    controls = input(">>>").lower()
    if controls == "w":
      t.forward(60)
    elif controls == 's':
      t.backward(60)
    elif controls == "a":
      t.left(30)
    elif controls == "d":
      t.right(30)
    elif controls == "q":
      print("Ok quitting now.")
      break
    else:
      print("Sorry that was not an option")
      
main()
