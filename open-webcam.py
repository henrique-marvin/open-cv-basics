import cv2 as cv

webcam = cv.VideoCapture(0)
window_name = "my webcam"

if webcam.isOpened():
    validation, frame = webcam.read()

    while validation:
        validation, frame = webcam.read()

        cv.imshow(window_name, frame)

        button = cv.waitKey(2)

        if button == 27:  # ESC button (ASCII table)
            break

else:
    print("Error...")

webcam.release()
cv.destroyAllWindows()
