import cv2
tracker = cv2.TrackerMOSSE_create()
roi=None
cap=cv2.VideoCapture("video1.mp4")
# cap=cv2.VideoCapture(0)
while True:
   ret,frame=cap.read()
   if roi is not None:
      success,box=tracker.update(frame)
      if success:
         x,y,w,h=[int(c) for c in box ]
         cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),2)
      else:
         print("tracking is failed")
         roi=None
         tracker
   cv2.imshow("frame",frame)
   key=cv2.waitKey(30)
   if key==ord("s"):
      roi=cv2.selectROI('tracker',frame)
      tracker.init(frame,roi)
   elif key==ord("q"):
      break

cap.release()
cap.destroyAllWindow()


