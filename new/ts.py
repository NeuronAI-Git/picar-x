import time
import datetime
import pimodule as pi
import random

class AutonomousDriver:
    def __init__(self):
        self.min_distance = 30  # cm
        self.turning = False
        self.turn_duration = 0.5
        self.turn_start_time = 0
        
    def check_obstacles(self):
        distance = pi.CAR.get_distance()
        return distance < self.min_distance
        
    def check_cliffs(self):
        cliff_status = pi.CAR.get_cliff()
        return any(cliff_status)
        
    def start_random_turn(self):
        self.turning = True
        self.turn_start_time = time.time()
        direction = random.choice([-1, 1])
        pi.CAR.set_dir(30 * direction)
        
    def handle_turn(self):
        if time.time() - self.turn_start_time > self.turn_duration:
            self.turning = False
            pi.CAR.set_dir(0)
            
    def drive(self):
        if self.turning:
            self.handle_turn()
            return
            
        if self.check_obstacles() or self.check_cliffs():
            pi.CAR.stop()
            pi.CAR.backward(50)
            time.sleep(0.5)
            pi.CAR.stop()
            self.start_random_turn()
        else:
            pi.CAR.forward(50)

def setup():
    print(">>> setup_start")
    pi.VISION.camera_start()
    pi.CAR.set_power(1)
    print(">>> setup_end")

def main():
    print(">>> main_start")
    driver = AutonomousDriver()
    
    try:
        while True:
            driver.drive()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    
#  @final  ----------------------------------
def final(
    *args, **kwargs
) -> None:
    print(">>> final_start")
    
    # end.PROCESSES
    
    if pi._picar is not None:
        pi.CAR.set_dir(0)
        pi.CAR.set_tilt(0)
        pi.CAR.set_pan(0)
        pi.CAR.set_cliff([0, 0, 0])
        pi.CAR.set_speed(0)
        pi.CAR.set_motor_1(0)
        pi.CAR.set_motor_2(0)
        pi.CAR.set_grayscale([0, 0, 0])
        pi.CAR.set_line([0, 0, 0])
        pi.CAR.set_power(0)
        pi.CAR.forward(0)
        pi.CAR.stop()
    
    if pi._music is not None:
        pi.MUSIC.disable()
        
    if pi._vision is not None:
        pi.VISION.camera_close()
    
    print(">>> final_end")
#  ------------------------------------------

if __name__ == "__main__":
    try:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}]", 
              "PI_START:", pi.__name__, f">>> {__name__}")
        setup()
        main()
    except Exception as e:
        print(e)
    finally:
        final()
