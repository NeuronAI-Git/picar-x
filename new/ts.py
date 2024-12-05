import pimodule

pimodule.init()
pimodule.MUSIC.set_volume(10)
pimodule.MUSIC.music("../musics/macarena.mp3")

def start_loop():
    pimodule.CAR.set_motor_1(0)
    pimodule.CAR.set_motor_2(0)
    pimodule.CAR.set_pan(0)
    pimodule.CAR.set_tilt(0)
    pimodule.CAR.set_dir(0)

def first_loop():
    pimodule.CAR.set_motor_1(-30)
    pimodule.CAR.set_motor_2(30)
    pimodule.CAR.set_pan(30, .5)
    pimodule.CAR.set_tilt(-30, .5)
    pimodule.CAR.set_dir(30, .5)
    pimodule.CAR.set_dir(-30, .5)
    pimodule.CAR.set_dir(30, .5)
    pimodule.CAR.set_dir(0, .5)
    pimodule.CAR.set_motor_1(30)
    pimodule.CAR.set_motor_2(-30)
    pimodule.CAR.set_pan(-30, .5)
    pimodule.CAR.set_tilt(30, .5)
    pimodule.CAR.set_dir(-30, .5)
    pimodule.CAR.set_dir(30, .5)
    pimodule.CAR.set_dir(-30, .5)
    pimodule.CAR.set_dir(0, .5)
    # pimodule.CAR.stop(2.55)

def second_loop():
    start_loop()
    pimodule.CAR.forward(10)

    pimodule.CAR.set_pan(10, .5)
    pimodule.CAR.set_tilt(10, .5)
    pimodule.CAR.set_dir(30, .5)

    pimodule.CAR.set_pan(-10, .5)
    pimodule.CAR.set_tilt(-10, .5)
    pimodule.CAR.set_dir(-30, .5)

    pimodule.CAR.set_pan(0, .5)
    pimodule.CAR.set_tilt(0, .5)
    pimodule.CAR.set_dir(0, .5)

    pimodule.CAR.forward(0)

    pimodule.CAR.backward(10)
    pimodule.CAR.set_pan(10, .5)
    pimodule.CAR.set_tilt(10, .5)
    pimodule.CAR.set_dir(30, .5)

    pimodule.CAR.set_pan(-10, .5)
    pimodule.CAR.set_tilt(-10, .5)
    pimodule.CAR.set_dir(-30, .5)

    pimodule.CAR.set_pan(0, .5)
    pimodule.CAR.set_tilt(0, .5)
    pimodule.CAR.set_dir(0, .5)
    pimodule.CAR.backward(0)



def end_loop():
    pimodule.CAR.stop()
    pimodule.MUSIC.music("../musics/macarena.mp3")

start_loop()
first_loop()
first_loop()
start_loop()
second_loop()
second_loop()
end_loop()
start_loop()
