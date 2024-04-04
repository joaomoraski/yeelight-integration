import yeelight
import sys


# Define colors dictionary
# Bulb just can handle 9 different transitions
colors = {
    'like1': (61, 95, 1),
    'like2': (104, 94, 447),
    'like3': (157, 31, 19),
    'like4': (167, 117, 35),
    'blue': (0, 0, 255),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'orange': (255, 165, 0),
    'purple': (128, 0, 128),
}

# Initialize a list to store transitions
transitions = []

# Iterate over each color in the colors dictionary
for color_name, rgb_values in colors.items():
    # Create RGBTransition for each color and add it to the transitions list
    transition = yeelight.RGBTransition(rgb_values[0], rgb_values[1], rgb_values[2], duration=1000)
    transitions.append(transition)


def main():

    bulbs = yeelight.discover_bulbs()
    bulb = yeelight.Bulb(bulbs[0]['ip'])

    print("If you need help, try send the command help.")

    while (True):
        if len(sys.argv) < 2:
            command = input("Insert command: ")
            if(command == "exit"): return
            if(command == "off"): bulb.turn_off()
            if(command == "on"): bulb.turn_on()
            changeColor(command, bulb, bulbs)
        else:
            command = str(sys.argv[1])
            changeColor(command, bulb, bulbs)
            break;
        
def changeColor(command, bulb, bulbs):
    if command == "purple":
        bulb.set_rgb(104,94,447)
        bulb.set_hsv(277, 86, 100)
    if command == "bulb":
        print(yeelight.discover_bulbs())
    elif command == "red":
        bulb.set_rgb(255,0,0)
    elif command == "blue":
        bulb.set_rgb(0,0,255)
        bulb.set_hsv(240, 100, 100)
    elif command == "white":
        bulb.set_rgb(255,255,255)
        bulb.set_color_temp(4000)
    elif command == "flow":
        flow = yeelight.Flow(
            count=0,
            action=yeelight.Flow.actions.stay,
            transitions=transitions
        )

        

        bulb.start_flow(flow)

main()