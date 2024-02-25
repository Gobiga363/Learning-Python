command = ""
is_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if is_started == False:
            print("Car started...")
            is_started = True
        else:
            print("Car is already started...")
    elif command == "stop":
        if is_started == True:
            print("Car stopped.")
            is_started = False
        else:
            print("Car is already stopped...")
    elif command == "help":
        print("""
        start  -to start the car
        stop   -to stop the car
        quit   -to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand your command")
