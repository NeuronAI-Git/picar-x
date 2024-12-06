#  @errors  ---------------------------------
#  ------------------------------------------

#  @imports  --------------------------------
import time
import datetime
import pimodule as pi
#  ------------------------------------------

#  @vars  -----------------------------------
# my_var: int = 0
#  ------------------------------------------

#  @init  -----------------------------------
def _ln(
    *args, **kwargs
) -> None:
    print('------------------------------------------')

pi.init()
_ln()
#  ------------------------------------------

#  @setup  ----------------------------------
def setup(
    *args, **kwargs
) -> None:
    print(">>> setup_start")
    
    # tests.VISION => check for working vision
    # tests.CAR => servo calibrations and zero
    # tests.GRAYSCALE => check for working grayscale
    # tests.ULTRASONIC => check for working ultra sonic
    # tests.SPEAKER => play non file
    
    print(">>> setup_end")
#  ------------------------------------------

#  @main  -----------------------------------
def main(
    *args, **kwargs
) -> None:
    print(">>> main_start")
    
    pi.VISION.camera_start()  # this might not work actually.. update pimodule
    pi.VISION.display()       # this might not work actually.. update pimodule
    
#  ------------------------------------------

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

#  @run  ------------------------------------
if __name__ == "__main__":
    try:
        time.sleep(0)
        print(
            f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}]",
            "PI_START:", pi.__name__,
            f">>> {__name__}"
        )
        (
            _ln(), setup(),
            _ln(), main(),
        )

    except Exception as e:
        print(e)
        
    finally:
        (
            print(">>> main_end"),
            _ln(), final(),
            _ln()
        )
        print(
            f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}]",
            "PI_END:", pi.__name__,
            f">>> {__name__}"
        )
        time.sleep(0)
        _ln()
#  ------------------------------------------
