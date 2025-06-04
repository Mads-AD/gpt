import curses
import random
import time

# Constants
LANES = 3
HEIGHT = 20
SPEED = 0.1

CAR = "A"
OBSTACLE = "#"


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    width = LANES * 3
    car_lane = LANES // 2
    obstacles = []
    score = 0
    start_time = time.time()

    while True:
        # Handle input
        key = stdscr.getch()
        if key == curses.KEY_LEFT and car_lane > 0:
            car_lane -= 1
        elif key == curses.KEY_RIGHT and car_lane < LANES - 1:
            car_lane += 1
        elif key == ord("q"):
            break

        # Spawn obstacle
        if random.random() < 0.2:
            obstacles.append([0, random.randint(0, LANES - 1)])

        # Move obstacles
        for obs in obstacles:
            obs[0] += 1
        obstacles = [o for o in obstacles if o[0] < HEIGHT]

        # Collision check
        for o in obstacles:
            if o[0] == HEIGHT - 1 and o[1] == car_lane:
                stdscr.addstr(HEIGHT // 2, width // 2 - 5, "GAME OVER")
                stdscr.refresh()
                time.sleep(2)
                return

        # Draw
        stdscr.clear()
        for y, lane in obstacles:
            stdscr.addstr(y, lane * 3 + 1, OBSTACLE)
        stdscr.addstr(HEIGHT - 1, car_lane * 3 + 1, CAR)
        stdscr.addstr(0, 0, f"Score: {int(score)}")
        stdscr.refresh()

        score = time.time() - start_time
        time.sleep(SPEED)


if __name__ == "__main__":
    curses.wrapper(main)
