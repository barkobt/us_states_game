import turtle
import pandas as pd

# Ekran ayarları
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "./blank_states_img.gif"
screen.addshape(image)

# Ana harita turtle'ı oluştur
map_turtle = turtle.Turtle()
map_turtle.shape(image)
map_turtle.penup()  # Turtle'ı ekrana çizmeden koymak için

# Yeni turtle: Yazı yazmak için
text_turtle = turtle.Turtle()
text_turtle.penup()  # Çizim yapılmasın
text_turtle.hideturtle()  # Turtle şekli gizli

# CSV dosyasını oku
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

# Doğru tahmin edilen eyaletler listesi
count = 0
guessed_states = []
unguessed_states = []




while len(guessed_states) < 50:
    # Kullanıcıdan input al
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?")
    
    # Kullanıcı "exit" yazarak oyundan çıkabilir
    if answer_state is None or answer_state.lower() == "exit":
        for state in states:
            if state in guessed_states:
               continue
            else:
                unguessed_states.append(state)
        
        df = pd.DataFrame(unguessed_states)
        df.to_csv("Unguessed_States.csv")
        break


    # Doğru tahmin
    if answer_state.title() in states and answer_state.title() not in guessed_states:
        guessed_states.append(answer_state.title()) # ! Title makes first letter capitalized. 
        
        # Eyaletin konumunu bul
        correct_state = data[data["state"] == answer_state.title()]
        x_coord = correct_state["x"].item()
        y_coord = correct_state["y"].item() # .item() basically takes the first item of the  data series.
 
        # Turtle kullanarak eyalet ismini yazdır (sadece yazı turtle'ı hareket eder)
        text_turtle.goto(x_coord, y_coord)  # Yazı turtle'ı belirlenen koordinata gider
        text_turtle.write(answer_state.title(), align="center", font=("Courier", 10, "bold"))

        # Sayacı güncelle
        count += 1










screen.mainloop()
