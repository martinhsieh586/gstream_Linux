import cv2

rtsp = 'rtsp://admin:ai123456@192.168.0.53'

cap = cv2.VideoCapture(rtsp)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')          # 設定影片的格式為 MJPG
# out = cv2.VideoWriter('output.mp4', fourcc, 60.0, (width,  height))  # 產生空的影片

while True:
    ret, frame = cap.read() 
    if ret:
        cv2.imshow('test', frame)
        # out.write(frame)
        if cv2.waitKey(1) == ord('q'):  # 1 millisecond
            break
    else:
        break
