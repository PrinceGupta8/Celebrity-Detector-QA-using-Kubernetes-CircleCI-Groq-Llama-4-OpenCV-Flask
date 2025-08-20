from io import BytesIO
import numpy as np
import cv2

def process_image(image_file):
    in_memory_file=BytesIO()
    image_file.save(in_memory_file)
    
    image_bytes=in_memory_file.getvalue()
    nparr=np.frombuffer(buffer=image_bytes,dtype=np.uint8)
    img=cv2.imdecode(nparr,flags=cv2.IMREAD_COLOR)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    faces=face_cascade.detectMultiScale(image=gray,scaleFactor=1.1,minNeighbors=5)
    
    if len(faces)==0:
        return image_bytes,None
    
    largest_face=max(faces,key=lambda r:[r[2] * r[3]])

    (x,y,w,h)=largest_face

    cv2.rectangle(img=img,pt1=(x,y),pt2=((x+w),(y+h)),color=(0,255,0),thickness=3)

    is_success, buffer=cv2.imencode(ext=".jpg",img=img)
    return buffer.tobytes(), largest_face 
    

    