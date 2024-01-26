import dlib
import cv2
import numpy as np

# 初始化Dlib的人脸检测器和关键点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("path_to_shape_predictor_68_face_landmarks.dat")

def align_face(image, landmarks, output_size=(160, 160)):
    # 定义对齐后人脸的标准关键点位置
    standard_points = np.float32([[30, 30], [130, 30], [80, 80]])

    # 选择用于对齐的三个关键点（左眼、右眼、鼻尖）
    points = np.float32([(landmarks.part(36).x, landmarks.part(36).y),
                         (landmarks.part(45).x, landmarks.part(45).y),
                         (landmarks.part(30).x, landmarks.part(30).y)])

    # 计算仿射变换矩阵
    M = cv2.getAffineTransform(points, standard_points)
    # 进行仿射变换，对齐人脸
    aligned = cv2.warpAffine(image, M, output_size)
    return aligned

def preprocess_face_image(image_path):
    # 加载图像
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = detector(gray)
    if len(faces) == 0:
        return None

    # 选择第一个检测到的人脸
    face = faces[0]

    # 人脸关键点检测
    landmarks = predictor(gray, face)

    # 人脸对齐
    aligned_face = align_face(gray, landmarks)

    # 人脸归一化和转换为灰度图像
    normalized_face = cv2.equalizeHist(aligned_face)
    return normalized_face

# 使用示例
preprocessed_image = preprocess_face_image('path_to_your_image.jpg')