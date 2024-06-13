import json

with open("ghostship.json") as file:
    rooms = json.load(file)

def get_room(room_num):
    for room in rooms:
        if room.get("room_num") == room_num:
            return room

def print_room(room):
    if room.get("room_num") == room_num:
        print(room.get("title"))
        print(room.get("description"))
        print()
        print("Valid exits: ", end="")
        for exit in room.get("exits"):
            print(exit.get("dir_name"), end="")
            print(" ", end="")
        print()

room_num = 1

while True:
    room = get_room(room_num)
    print_room(room)

    inp = ""
    while not inp:
        inp = input("Where do you want to go? ")
        inp = inp.upper().strip()
        inp = inp[0:1]
        if inp not in room.get("valid_exits"):
            print("Invalid direction!")
            inp = ""

    for exit in room.get("exits"):
        if inp == exit.get("dir"):
            room_num = exit.get("room_num")
            




