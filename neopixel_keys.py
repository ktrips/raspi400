import sys,tty,termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()
    if char in ("r","red"):
        print("Red!")

    if char in ("g","green"):
        print("Green!")

    if char in ("b","blue"):
        print("Blue!")

    if char in ("z","zoom"):
        print("Zoom!")

    if char in ("x","q","quit"):
        print("Program Ended")
        break
