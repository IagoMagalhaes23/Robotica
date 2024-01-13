from kalmanFilter import KalmanFilter
import cv2

kf = KalmanFilter()

predicted = kf.predict(50,100)
predicted = kf.predict(100,100)
predicted = kf.predict(150,100)
predicted = kf.predict(200,100)

print(predicted)