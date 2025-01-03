import cv2
import cv2.data

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
vision = cv2.VideoCapture(0)
first_position = None
game_run = True
while vision.isOpened() and game_run:
    ret , frame = vision.read()
    if not ret:
        break 
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    movement = face.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in movement:
        corner = (x,y)
        if first_position is None:
            first_position = corner
            print("Initial angles captured:", first_position)
        is_detected = (
            abs(corner[0] - first_position[0]) > 10 or
            abs(corner[1] - first_position[1]) > 10
            )
        if is_detected:
            print("YOU FAILED")
            game_run = False
        cv2.rectangle(frame, (x , y), (x + w, y + h), (255,0,0), 2)
    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

vision.release()
cv2.destroyAllWindows() 