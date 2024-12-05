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
        _ln(),
        setup(),
        _ln(),
        main(),
        _ln(),
        final(),
        _ln()
    )
    print(
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}]",
        "PI_END:", pi.__name__,
        f">>> {__name__}"
    )
    time.sleep(0)
#  ------------------------------------------
