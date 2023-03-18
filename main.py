import cv2
import numpy as np
import argparse
import pyautogui


def print_coordinates(matches):
    for match in matches:
        x, y = match
        print(f"Match found at ({x}, {y})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--template", required=True, help="Path to the image template")
    args = vars(ap.parse_args())

    SCREEN_SIZE = (800, 600)

    template = cv2.imread(args["template"], cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("Error: Failed to load template image.")
    w, h = template.shape[::-1]
    threshold = 0.3

    while True:
        img = pyautogui.screenshot(region=(0,0, 800, 600))
        frame = np.array(img)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.3#

        loc = np.where(res >= threshold)
        matches = list(zip(*loc[::-1]))

        if len(matches) > 0:
            print_coordinates(matches)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    while True:
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
i=0