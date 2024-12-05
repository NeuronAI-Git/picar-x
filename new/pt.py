import pimodule as pi
import time

def main():
    pi.CAR.set_dir(30)
    time.sleep(2)
    pi.CAR.set_dir(0)
    
if __name__ == "__main__":
    main()
