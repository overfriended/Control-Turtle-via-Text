import turtle
import math

t = turtle.Turtle()
i = input("Instructions: \n")

colors = ["red", "blue", "yellow", "green", "black", "purple", "white"]
keywords = ["forward", "backward", "left", "right", "rforward", "lforward", "rbackward", "lbackward"]

def draw(color="black", forward=True, left=True, angle=90, count="auto"):

  if type(count) == str and type(angle) == int: 
    count = (90.0 / angle) * 4
  elif type(count) == int and type(angle) == int:
    pass
  else:
    print("Angle must be an integer.")
    return

  for i in range(int(count)):
    if left != None:
      if left:
        t.left(angle)
      else:
        t.right(angle)
    if forward != None:
      if forward:
        t.forward(angle)
      else:
        t.backward(angle)

def dirdraw(color, direction="forward", x=90, y="auto"):
  directions = {
    "forward": [True, None],
    "backward": [False, None],
    "left": [None, True],
    "right": [None, False],
    "rforward": [True, False],
    "lforward": [True, True],
    "rbackward": [False, False],
    "lbackward": [False, True]
  }

  if direction in directions:
    draw(color, directions[direction][0], directions[direction][1], x, y)

def instruct(args):
  args = args.split(" ")
  result = []

  for i, v in enumerate(args):
    if v.split("-")[0] in keywords:
      if len(args) > (i + 1):
        if not args[i + 1].isdigit():
          result.append([v, 1])
        else:
          result.append([v, args[i + 1]])
      else:
        result.append([v, 1])
    else:
      if v in colors:
        result.append(v)
  return result
  

def compdraw(instructions):
  new = instruct(instructions)

  for i in new:
    if i in colors:
      t.color(i)
      continue

    if "-" in i[0]:
      direction = i[0].split('-')
    else:
      direction = [i[0]]

    if len(direction) == 1:
      dirdraw(None, direction[0], 90, int(i[1]))
    else:
      dirdraw(None, direction[0], int(direction[1]), int(i[1]))
      
compdraw(i)