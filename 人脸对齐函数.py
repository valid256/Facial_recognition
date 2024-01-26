import cv2
import dlib
import numpy as np

# 预训练的人脸关键点检测模型路径
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

# 初始化 dlib 的人脸检测器和关键点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def align_face(image):
    # 使用 dlib 的人脸检测器来检测人脸
    rects = detector(image, 1)

    if len(rects) > 0:
        # 使用预训练的人脸关键点检测模型来找到人脸的关键点
        landmarks = np.matrix([[p.x, p.y] for p in predictor(image, rects[0]).parts()])

        # 选择左眼和右眼的中心点
        left_eye = landmarks[42:48].mean().astype(int)
        right_eye = landmarks[36:42].mean().astype(int)

        # 计算两眼的角度
        dy = right_eye[1] - left_eye[1]
        dx = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(dy, dx)) - 180

        # 计算图像的中心点
        center = np.array(image.shape[:2][::-1]) / 2

        # 计算旋转矩阵
        rotation_matrix = cv2.getRotationMatrix2D(tuple(center), angle, 1)

        # 对图像进行旋转
        aligned_image = cv2.warpAffine(image, rotation_matrix, tuple(np.array(image.shape[:2][::-1])), flags=cv2.INTER_LINEAR)

        return aligned_image

    else:
        print("No face detected.")
        return None