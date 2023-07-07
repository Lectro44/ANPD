import cv2
import easyocr
import pandas as pd

harcascade = "/content/haarcascade_russian_plate_number.xml"



select=st.selectbox("select",["camera","upload image"])
if select=="camera":
  cam=st.camera_input("capture a photo")
  if cam is not None:
    file_bytes = np.asarray(bytearray(cam.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    image(opencv_image)

else:
  uploaded_file = st.file_uploader("Choose a image file", type="jpg")
  if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image1= cv2.imdecode(file_bytes, 1)
    image(opencv_image1)

def image(cv_image):
  photo= cv2.imread(cv_image)
  return

while True:
  img=image(photo)

  plate_cascade = cv2.CascadeClassifier(harcascade)
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
  for (x,y,w,h) in plates:
    area = w * h
    if area > min_area:
      cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
      cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
      img_roi = img[y: y+h, x:x+w]
      cv2_imshow(img_roi)
      cv2_imshow(img)
      break
  break
reader = easyocr.Reader(['en'])
result=reader.readtext(img_roi)
text = result[0][-2]
print(text)




      #cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
      #cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
      #cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
      #cv2.imshow("Results",img)
      #cv2.waitKey(500)
      #count += 1



