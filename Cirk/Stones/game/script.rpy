# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Алиса', color="#000000")
define right_pos = Position(xalign=0.8,yalign=0.3)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    $ renpy.movie_cutscene("images/zoom_to_zdanie.webm", delay=2, loops=0, stop_music=True)

    scene bg room
    show alice_happy at right_pos 
    with dissolve
    a "Я веселая!"
    show alice_neutral at right_pos
    a "Я нейтральная!"
    show alice_sad at right_pos
    a "Я грустная!"

    return
