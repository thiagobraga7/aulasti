import turtle
import math
#AttributeError 'builtin_function_or_method'
turtle.distance
turtle.color 


scale = 75000

circumference = 2 * math.pi * scale
radius = circumference / 2 * math.pi

screen = turtle.Screen()
screen.bgcolor("black")

sun = turtle.Turtle()
sun.setposition(0,0)
sunRadius = 432690 / scale
#sun.color(254, 204, 51)

sun.begin_fill()

#circumference is 2 * pi * radius


sunCircumference = 2 * math.pi * sunRadius

for i in range(36):
    sun.forward(sunCircumference / 36)
    sun.right(10)

sun.end_fill()
sun.hideturtle()

planet = turtle.Turtle()
planet.speed()

planetScale = 100

orbit = turtle.Turtle()
orbit.color("white")

sunScale = 100

def drawPlanet(color, distance, radius):
    radius = radius * planetScale / scale
    circumference = 2 * math.pi * scale
    print(circumference)
    

distFromSun = sunRadius + ((radius + sum.distance) / scale) / 10

orbit.penup()
orbit.setposition(0,0)
orbit.showturtle()

orbit.setheading(0)
orbit.forward(sum.distFromSun)
orbit.setheading(270)
orbitCircumference = 2 * math.pi * sum.distFromSun

orbit.pendown()
for i in range(36):
  orbit.forward(orbitCircumference / 10)
  orbit.right(10)

orbit.hideturtle  

r = sum.color[0]
g = sum.color[1]
b = sum.color[2]

planet.setposition(0,0)
planet.showturtle()
planet.color(r,g,b)
planet.penup()



planet.forward(sum.distFromSun)
planet.pendown()
planet.begin_fill()
for i in range(36):
  planet.forward(circumference / 36)
  planet.right(10)

planet.end_fill()
planet.hideturtle()


drawPlanet([151, 151, 159], 35980000, 1516)

for i in range(36):
    planet.forward(circumference / 36)
    planet.right(10)


planet.end_fill()
planet.hideturtle()
planet.penup()



# draw mercury
drawPlanet([151, 151, 159], 35980000, 1516)

# venus
drawPlanet([211, 156, 126], 67240000, 3760.4)

# earth
drawPlanet([140, 177, 222], 92950000, 3958.8)

# mars
drawPlanet([198, 123, 92], 141600000, 2106.1)

# jupiter
drawPlanet([211, 156, 126], 483800000, 43441)

# saturn
drawPlanet([197, 171, 110], 890000000, 36184)

# uranus
drawPlanet([213, 251, 252], 1784000000, 15759)

# neptune
drawPlanet([62, 84, 232], 2793000000, 15299)

### RGB Codes ###
# Sun: (254, 204, 51) - [254, 204, 51]
# Mercury: (151, 151, 159) - [151, 151, 159]
# Venus: (211, 156, 126) - [211, 156, 126]
# Earth: (140, 177, 222) - [140, 177, 222]
# Mars: (198, 123, 92) - [198, 123, 92]
# Jupiter: (211, 156, 126) - [211, 156, 126]
# Saturn: (197, 171, 110) - [197, 171, 110]
# Uranus: (213, 251, 252) - [213, 251, 252]
# Neptune: (62, 84, 232) - [62, 84, 232]

### Planetary Distance from Sun (miles) ###
# Sun: 0 mi
# Mercury: 35.98 million mi
# Venus: 67.24 million mi
# Earth: 92.96 million mi
# Mars: 141.6
# Jupiter: 483.8 million mi
# Saturn: 890.9 million mi
# Uranus: 1.784 billion mi
# Neptune: 2.793 billion mi

### Planetary Radii (miles) ###
# Sun: 432690 mi
# Mercury: 1516 mi
# Venus: 3760.4 mi
# Earth: 3958.8 mi
# Mars: 2106.1 mi
# Jupiter: 43441 mi
# Saturn: 36184 mi
# Uranus: 15759 mi
# Neptune: 15299 mi


























 







