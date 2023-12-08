from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.reset_sensor()

drone.takeoff()


def go_to_height(goal_height):
    h = None
    error = None
    while True:
        h = drone.get_height(unit="in")
        error = h - goal_height
        print("height", int(h))
        print("error", int(error))
        print()

        if abs(error) > 1:
            kp = 4
            throttle = max(min(-kp * error, 100), 0)
            drone.set_throttle(throttle)
            drone.move(.5)

        if abs(error) < 5:
            drone.hover(2)
            break

        x_angle = drone.get_x_angle()
        y_angle = drone.get_y_angle()
        z_angle = drone.get_z_angle()

        print(x_angle, y_angle, z_angle)

        time.sleep(.1)

go_to_height(72)

drone.set_pitch(20)
drone.move(10)

drone.land()

drone.close()
