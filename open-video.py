import cv2 as cv

video_path = "path/to/video"  # example: C:/Users/Me/Videos/cats.mp4

video = cv.VideoCapture(video_path, 0)
window_name = "my video"

if video.isOpened():
    validation, frame = video.read()

    while validation:
        validation, frame = video.read()

        cv.imshow(window_name, frame)

        button = cv.waitKey(2)

        if button == 27:  # ESC button (ASCII table)
            break
else:
    print("Error...")

video.release()
cv.destroyAllWindows()
