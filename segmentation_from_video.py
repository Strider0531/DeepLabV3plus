import time
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.utils import CustomObjectScope

from metrics import iou, dice_loss_m, dice_coef_m


def segment_video(video_path, output_path):
    vid = cv2.VideoCapture(video_path)
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    # by default VideoCapture returns float instead of int
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, codec, fps, (width, height))
    frame = 0

    while True:
        _, img = vid.read()

        try:
            original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        except:
            break

        h, w, _ = original_image.shape
        x = cv2.resize(original_image, (512, 512))
        x = x / 255.0
        x = x.astype(np.float32)
        x = np.expand_dims(x, axis=0)

        t1 = time.time()

        y = model.predict(x)[0]
        y = cv2.resize(y, (w, h))
        y = np.expand_dims(y, axis=-1)

        masked_image = original_image * y
        masked_image = np.array(masked_image, dtype=np.uint8)

        if output_path != '': 
          out.write(masked_image)

          # progress viewing
          frame += 1
          print("Progress: {}/{:}".format(frame, total_frames))

    cv2.destroyAllWindows()


with CustomObjectScope({'iou': iou, 'dice_coef_m': dice_coef_m, 'dice_loss_m': dice_loss_m}):
        model = tf.keras.models.load_model("files/model_smooth=0.5.h5")