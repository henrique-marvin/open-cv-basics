import cv2 as cv

image_path = "path/to/image"  # example: C:/Users/Me/Images/Robot.jpg
window_name = "my image"

if cv.haveImageReader(image_path):
    image = cv.imread(image_path)

    cv.imshow("my image", image)

    button = cv.waitKey(0)

    if button == 27:  # ESC button (ASCII table)
        cv.destroyAllWindows()
else:
    print("Error...")
