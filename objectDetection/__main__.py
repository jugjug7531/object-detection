import cv2
import ballDetect

if __name__ == "__main__":

  #カメラ映像読み込み
  cap = cv2.VideoCapture(0)

  while(cap.isOpened()):
    ret, frame = cap.read()

    #赤色の物体検出
    rects = ballDetect.find_rect_of_target_red(frame)

    #一番大きい部分のみ抽出
    if len(rects) > 0:
      rect = max(rects, key=(lambda x: x[2] * x[3]))
      cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (0, 0, 255), thickness=2)

    cv2.imshow('movie', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
