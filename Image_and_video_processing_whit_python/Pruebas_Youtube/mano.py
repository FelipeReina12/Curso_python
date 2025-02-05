import cv2
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
mhands = mphands.Hands(False)
mpdraw = mp.solutions.drawing_utils

p_time = 0
cTIme = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mhands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)
    
    # cTime = time.time()
    # fps = 1/(cTIme -  p_time)
    # p_time = cTime
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 