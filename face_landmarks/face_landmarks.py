import face_recognition as face 
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, Frame = cap.read()

    landmarks = face.face_landmarks(Frame)
    count = len(landmarks)
    # print(Frame)
    datas = []

    for x in landmarks:
        for y in x:
            datas.append(y)


    plot_data = []
    for z in datas:
        # print(landmarks[0][z])
        plot_data.append(landmarks[0][z])

# print(plot_data)

    print(len(plot_data))
    data = []
    for a in plot_data:
        for b in a:
            data.append(b)


    for point in data:
        cv2.circle(Frame,point,2,(0,0,255),thickness=2)
    
    
    cv2.imshow("Frame",Frame)
    k = cv2.waitKey(1)
    if k == 32:
        break
cap.release()
cv2.destroyAllWindows()