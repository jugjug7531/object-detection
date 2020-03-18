import numpy as np
import cv2

#赤色検出および矩形配列の返却
def find_rect_of_target_red(image):
    #HSV空間に変換
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    #マスク作成（赤色抽出）
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h < 20) | (h > 200)) & (s > 128)] = 255
    #輪郭作成
    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    #輪郭情報から矩形作成
    rects = []
    for contour in contours:
        approx = cv2.convexHull(contour)#凹凸のある塊を内包する、凸状の形状を算出する関数 返り血は(X, Y)の配列
        rect = cv2.boundingRect(approx)#(x, y, width, height)という形式の矩形情報を返す
        rects.append(np.array(rect))
    return rects
