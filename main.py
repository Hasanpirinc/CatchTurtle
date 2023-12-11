import time
import turtle
import random
score = 0
counter = 60
level = 1


turtle_instance = turtle.Turtle()

turtle_instance.write("Score: " + str(score), align="center", font=("Arial", 18, "bold"))
turtle_instance.goto(0, 350)
turtle_instance.write("Level: " + str(level), align="center", font=("Arial", 18, "bold"))
turtle_instance.goto(0, 330)
# Sayacı ekranın üst ve orta kısmına yazdırın
turtle_instance.goto(0, 300)
turtle_instance.write("Counter: " + str(counter), align="center", font=("Arial", 20, "bold"))

# Kaplumbağayı oluşturun
turtle_2 = turtle.Turtle()
turtle_2.shape("turtle")
turtle_2.speed(2)
turtle_2.color("blue")
# Kaplumbağayı her defasinda farkli bir yere yerleştirin
def place_turtle():
    turtle_2.penup()
    turtle_2.hideturtle()
    time.sleep(1)
    turtle_2.goto(random.randrange(-200, 200), random.randrange(-200, 200))
    turtle_2.pendown()
    turtle_2.showturtle()
    time.sleep(1)





# Kaplumbağayı ekrana yerleştirin
place_turtle()

# Bir sonraki levele geçiş tuşu oluşturmak için `next_level()` işlevini kullanın
def next_level():
    global level
    level += 1
    counter = level
    place_turtle()

# Oyunu bitirmek için `game_over()` işlevini kullanın
def game_over():
    turtle.clear()
    turtle.write("Game Over! Your score is " + str(score), align="center", font=("Arial", 20, "bold"))
    turtle.hideturtle()

while True:
    # Kaplumbağayı yakalamak için farenin sol tuşunu kontrol edin
    if turtle_2.shape() == "turtle":
         #Kaplumbağayı yakalarsanız, skoru artırın
        if turtle_2.distance(turtle_2.xcor(), turtle_2.ycor()) < 20:
            score +=1
            place_turtle()
    counter -= 1

    if counter == 0:
    # Skor 10'dan az ise oyun biter
       if score < 10:
           game_over()

       else:
           next_level()
          # turtle_2.clear()
         #  turtle_2.write("Game Over! Your score is " + str(score), align="center", font=("Arial", 20, "bold"))
          # turtle_2.hideturtle()
          # break




    # Skor 10'dan fazla ise level artar
    #   else:
         #  level += 1
         #  counter = level
          # place_turtle()

    turtle_instance.clear()
    turtle_instance.write("Score: " + str(score), align="center", font=("Arial", 18, "bold"))
    turtle_instance.goto(0, 330)
    turtle_instance.write("Level: " + str(level), align="center", font=("Arial", 18, "bold"))
    turtle_instance.goto(0, 350)
    turtle_instance.write("Counter: " + str(counter), align="center", font=("Arial", 18, "bold"))
    turtle_instance.goto(0, 370)


turtle.mainloop()