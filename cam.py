import cv2
import numpy as np
import kociemba


CUBE_LENGTH = 4


class Side:
    def __init__(self):
        self.colors = [['NULL'] * CUBE_LENGTH for i in range(CUBE_LENGTH)]

    def add_colors(self, array):
        self.colors = array

    def get_colors(self):
        return self.colors


VIDEO = cv2.VideoCapture(0)
SIZE = int(0.40 * int(VIDEO.get(4)))

front = Side()
right = Side()
back = Side()
left = Side()
top = Side()
bottom = Side()

# print("Front: {}" .format(front.get_colors()))
# print()
# print(SIZE)
blank_image = np.zeros((SIZE*3, SIZE*6, 3), np.uint8)


def get_starts(ky, kx):
    start_x = int(ky / 2) - int(SIZE/2)
    start_y = int(kx / 2) - int(SIZE/2)
    pos = (int(start_x), int(start_y))
    return pos


def get_ends(start_x, start_y):
    end_x = int(start_x + SIZE)
    end_y = int(start_y + SIZE)
    ends = (int(end_x), int(end_y))
    return ends


def __draw_cube(img, starts, ends):

    thickness = 10
    cv2.rectangle(img, starts, ends, (0, 0, 0), thickness)

    diff = int(SIZE / CUBE_LENGTH)

    for x in range(CUBE_LENGTH):
        cv2.line(img, (starts[0] + (diff*x), starts[1]), (starts[0] + (diff*x), ends[1]), (0, 0, 0), thickness)
        cv2.line(img, (starts[0], starts[1] + (diff*x)), (ends[0], starts[1] + (diff*x)), (0, 0, 0), thickness)


def __print2darray(array):
    for i in range(CUBE_LENGTH):
        print(array[i])


def get_color(red, green, blue):
    diffcolors = abs(green - red)
    diffcolors1 = abs(green - blue)
    difforange = blue - green

    if diffcolors1 <= 10 and diffcolors <= 10:
        return 'White'
    elif diffcolors <= 10 and blue < 115 and green > blue and red > blue:
        return 'Yellow'
    elif red > green*2 and red > blue * 2:
        return 'Red'
    elif red > green + 10 and red > blue + 10 and difforange < 10:
        return 'Orange'
    elif green > red + 10 and green > blue + 10:
        return 'Green'
    elif blue > red + 10 and blue > green + 10:
        return 'Blue'
    else:
        return 'NOIDEA'
    pass


def put_sides(img, starts, blank, which):
    COLORS = [[0] * CUBE_LENGTH for i in range(CUBE_LENGTH)]
    diff = int(SIZE / CUBE_LENGTH)
    img = cv2.flip(img, 1)
    for i in range(CUBE_LENGTH):
        for j in range(CUBE_LENGTH):

            x = starts[1] + (diff * i)
            x_end = starts[1] + (diff * i) + diff

            y = starts[0] + (diff * j)
            y_end = starts[0] + (diff * j) + diff

            b = img[x:x_end, y:y_end, 0]

            g = img[x:x_end, y:y_end, 1]

            r = img[x:x_end, y:y_end, 2]

            b_mean = int(np.mean(b))
            g_mean = int(np.mean(g))
            r_mean = int(np.mean(r))
            print(r_mean, g_mean, b_mean)

            dominant = get_color(r_mean, g_mean, b_mean)

            if dominant == 'White':
                COLORS[i][j] = 'White'
                blank[x-starts[1] + SIZE: x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (255, 255, 255)
            elif dominant == 'Yellow':
                COLORS[i][j] = 'Yellow'
                blank[x-starts[1] + SIZE: x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (100, 255, 255)
            elif dominant == 'Red':
                COLORS[i][j] = 'Red'
                blank[x-starts[1] + SIZE:x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (0, 0, 255)
            elif dominant == 'Orange':
                COLORS[i][j] = 'Orange'
                blank[x-starts[1] + SIZE:x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (26, 118, 245)
            elif dominant == 'Green':
                COLORS[i][j] = 'Green'
                blank[x-starts[1] + SIZE:x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (0, 255, 0)
            elif dominant == 'Blue':
                COLORS[i][j] = 'Blue'
                blank[x-starts[1] + SIZE:x_end-starts[1] + SIZE, (y - starts[0]) + (SIZE * which):(y_end - starts[0]) + (SIZE * which)] = (255, 0, 0)
            else:
                COLORS[i][j] = 'NOIDEA'

    __print2darray(COLORS)

    if which == 0:
        print("Adding Front")
        front.add_colors(COLORS)
        print(front.get_colors())

    elif which == 1:
        right.add_colors(COLORS)
        print(right.get_colors())
        print("Adding Right")

    elif which == 2:
        back.add_colors(COLORS)
        print(back.get_colors())
        print("Adding Back")

    elif which == 3:
        left.add_colors(COLORS)
        print(left.get_colors())
        print("Adding Left")

    elif which == 4:
        top.add_colors(COLORS)
        print(top.get_colors())
        print("Adding Top")

    elif which == 5:
        bottom.add_colors(COLORS)
        print(bottom.get_colors())
        print("Adding Bottom")

    for x in range(CUBE_LENGTH):
        cv2.line(blank, (SIZE * which + (diff*x), 0), (SIZE * which + (diff*x), SIZE), (0, 0, 0), 10)
        cv2.line(blank, (SIZE * which, (diff*x)), (SIZE * which + SIZE, (diff*x)), (0, 0, 0), 10)

    cv2.rectangle(blank, (SIZE * which, SIZE), (SIZE + SIZE * which, SIZE*2), (255, 255, 255), 10)


def capture_sides(times):
    while VIDEO.isOpened():

        ret, frame = VIDEO.read()
        width = int(VIDEO.get(3))
        height = int(VIDEO.get(4))

        startPos = get_starts(width, height)
        endPos = get_ends(startPos[0], startPos[1])

        frame = cv2.flip(frame, 1)

        if ret:
            __draw_cube(frame, startPos, endPos)
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                put_sides(frame, startPos,  blank_image, times)
                break

        else:
            break


def main():

    for x in range(6):
        capture_sides(x)

    print(front.get_colors())
    print(right.get_colors())
    print(back.get_colors())
    print(left.get_colors())
    print(top.get_colors())
    print(bottom.get_colors())

    VIDEO.release()
    cv2.destroyAllWindows()

    while True:
        if cv2.waitKey(1) & 0xFF == ord(' ') :
            cv2.imshow('image', blank_image)
            print(blank_image.shape)
            cv2.waitKey(0)
            cv2.destroyWindow('image')
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # print(kociemba.solve('UUUUUUUUUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'))


if __name__ == "__main__":
    main()
