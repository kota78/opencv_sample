import cv2  # OpenCVライブラリをインポート

# このスクリプトが直接実行されたときにのみ以下のコードが実行される
if __name__ == "__main__":
    # 内蔵カメラを起動
    cap = cv2.VideoCapture(0)

    # OpenCVに用意されている顔認識するためのxmlファイルのパス
    cascade_path = "/Users/ko_cha78/opencv/data/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)  # カスケード分類器の特徴量を取得

    color = (255, 255, 255)  # 顔に表示される枠の色を指定（白色）

    while True:
        ret, frame = cap.read()  # 内蔵カメラから読み込んだキャプチャデータを取得

        # 顔認識の実行
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

        # 顔が見つかったらcv2.rectangleで顔に白枠を表示
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

        cv2.imshow("frame", frame)  # 表示

        # qキーを押すとループ終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # 内蔵カメラを終了
    cv2.destroyAllWindows()  # すべてのウィンドウを閉じる
