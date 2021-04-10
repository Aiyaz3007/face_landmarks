import face_recognition as face 
import cv2

image_file = "/Users/aiyaz/Desktop/rajini.jpg"
img = cv2.imread(image_file)

image = face.load_image_file(image_file)




landmarks = face.face_landmarks(img)
count = len(landmarks)
print(count)

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
    cv2.circle(img,point,1,(0,0,255),thickness=2)
# for x in landmarks[0]["chin"]:
    # print(x)
    # datas.append(x)

# print(datas)

cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


