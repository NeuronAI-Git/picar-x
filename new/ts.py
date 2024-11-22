import pimodule

pimodule.SPEAK.pico2wave("Hi there! I am looking around.")

for _ in range(2):
    pimodule.CAR.set_pan(30, 1)
    pimodule.CAR.set_pan(-30, 1)

pimodule.CAR.set_pan(0, 1)
pimodule.SPEAK.pico2wave("Nice room!", 0.5)
pimodule.LLM.generate("So, how are you?", 1)
