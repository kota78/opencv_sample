#OpenCV 
[[2つの値を返す関数]]
[[tuple タプル]]
[[スライス操作]]


◎1ループごとに、画像を取得→顔認識→枠を上書き→画面に表示を実行してる

```python
import cv2  # OpenCVライブラリをインポート
# このスクリプトが直接実行されたときにのみ以下のコードが実行される
if __name__ == "__main__":
    # 内蔵カメラを起動
    cap = cv2.VideoCapture(0)

    # OpenCVに用意されている顔認識するためのxmlファイルのパス
    cascade_path = "/Users/ko_cha78/opencv/data/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)  # カスケード分類器の特徴量を取得

	# 顔に表示される枠の色
    color = (255, 255, 255)

    while True:
	    #retはフレームの読み込みが成功したかどうかを示すブール値
	    #frameは読み込まれたフレーム
        ret, frame = cap.read()

        # 顔認識の実行
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

        # 顔が見つかったら
        if len(facerect) > 0:
            for rect in facerect:
	            #顔に白枠を表示
	            #rectは顔検出の結果として得られる、検出された顔の領域(座標)を表すリスト
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
        #"frame": ウィンドウの名前。
        #同じ名前のウィンドウが既に存在→そのウィンドウに画像が表示
        #存在しない→新しいウィンドウが作成
		#frame: 表示する画像（ここでは矩形が描画されたカメラのフレーム）。
        cv2.imshow("frame", frame)  # 表示

        # qキーを押すとループ終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # 内蔵カメラを終了
    cv2.destroyAllWindows()  # すべてのウィンドウを閉じる

```

# 顔認識アルゴリズム
顔認識アルゴリズムは、画像全体をスキャンし、異なるサイズの窓を用いて、顔が存在する可能性のある領域を探し、それぞれの領域が顔の候補として評価される。
◎1つの顔に対してminNeighbors以上の数だけ顔検出アルゴリズムが反応した場合のみ顔だと認識される。
byGPT