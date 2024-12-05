#  @imports  --------------------------------
import time
import datetime
import pimodule as pi
#  ------------------------------------------

#  @setup  ----------------------------------
def setup(
    *args, **kwargs
) -> None:
    print(">>> setup_start")
    
    # pi.init(vision=False, music=False, tts=False)
    pi.init()
    
    print(">>> setup_end")
#  ------------------------------------------

#  @main  -----------------------------------
def main(
    *args, **kwargs
) -> None:
    print(">>> main_start")
    
    
    
    print(">>> main_end")

#  ------------------------------------------

#  @final  ----------------------------------
def final(
    *args, **kwargs
) -> None:
    print(">>> final_start")
    
    
    print(">>> final_end")
#  ------------------------------------------

#  @run  ------------------------------------
if __name__ == "__main__":
    time.sleep(0)
    print(
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}]",
        "PI_START:", pi.__name__,
        f">>> {__name__}"
    )
    (
        print('------------------------------------------'),
        setup(),
        print('------------------------------------------'),
        main(),
        print('------------------------------------------'),
        final(),
        print('------------------------------------------')
    )
    print(
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}]",
        "PI_END:", pi.__name__,
        f">>> {__name__}"
    )
    time.sleep(0)
#  ------------------------------------------
