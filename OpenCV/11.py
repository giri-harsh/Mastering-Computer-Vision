import cv2
import numpy as np
import time

# load imag
img_path = r"C:\Work\Programing Language\Python\Libraries\OpenCV\data\image.png"
img = cv2.imread(img_path)

drawing = False
ix, iy = -1, -1
mode = "blur"
history = []

# function to draw instruction panel
def show_instructions(frame):
    overlay = frame.copy()

    instructions = [
        "INSTRUCTIONS:",
        "Drag mouse: Select area to censor",
        "b : Blur mode",
        "p : Pixelation mode",
        "u : Undo last action",
        "s : Save image",
        "x : Exit",
        f"Current mode: {mode.upper()}"
    ]

    y0 = 25
    for i, text in enumerate(instructions):
        y = y0 + i*25
        cv2.putText(
            overlay, text, (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0,255,0), 2, cv2.LINE_AA
        )

    return overlay


# mouse callback
def draw(event, x, y, flags, params):
    global ix, iy, drawing, img, history

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        history.append(img.copy())

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp = img.copy()
        cv2.rectangle(temp, (ix, iy), (x, y), (0,0,255), 2)
        temp = show_instructions(temp)
        cv2.imshow("window", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        x1, x2 = sorted([ix, x])
        y1, y2 = sorted([iy, y])
        roi = img[y1:y2, x1:x2]

        if roi.size == 0:
            return

        # blur censor
        if mode == "blur":
            roi = cv2.GaussianBlur(roi, (51,51), 0)

        # pixelation censor
        elif mode == "pixel":
            small = cv2.resize(roi, (16,16), interpolation=cv2.INTER_LINEAR)
            roi = cv2.resize(small, (x2-x1, y2-y1), interpolation=cv2.INTER_NEAREST)

        img[y1:y2, x1:x2] = roi


cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

while True:
    frame = show_instructions(img.copy())
    cv2.imshow("window", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('x'):
        break

    elif key == ord('s'):
        filename = f"censored_{int(time.time())}.png"
        cv2.imwrite(filename, img)
        print("Saved:", filename)

    elif key == ord('u'):
        if history:
            img = history.pop()

    elif key == ord('b'):
        mode = "blur"

    elif key == ord('p'):
        mode = "pixel"

cv2.destroyAllWindows()
