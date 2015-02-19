import time

from rfController import RFController



def main():
    rf = RFController()
    rf.turn_on("test1")
    rf.turn_on("test2")
    rf.turn_on("test3")
    time.sleep(3)
    rf.turn_off("test1")
    rf.turn_off("test2")
    rf.turn_off("test3")

if __name__ == "__main__":
    main()
