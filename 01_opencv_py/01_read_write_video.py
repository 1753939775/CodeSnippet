# -*- coding: utf-8 -*-
import cv2


def start_detect_video(src_video_path, target_video_path):
    # VideoCapture方法是cv2库提供的读取视频方法
    cap = cv2.VideoCapture(src_video_path)
    # 设置需要保存视频的格式“xvid”
    # 该参数是MPEG-4编码类型，文件名后缀为.avi
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 设置视频帧频
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 设置视频大小
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # VideoWriter方法是cv2库提供的保存视频方法
    # 按照设置的格式来out输出
    out = cv2.VideoWriter(target_video_path, fourcc, fps, size)

    # 确定视频打开并循环读取
    i = 0
    while (cap.isOpened()):
        # 逐帧读取，ret返回布尔值
        # 参数ret为True 或者False,代表有没有读取到图片
        # frame表示截取到一帧的图片
        ret, frame = cap.read()
        if ret == True:
            i = i + 1
            # 每10帧处理一张
            if i % 10 != 0:
                continue
            # 进行相关的图像处理操作
            frame_res = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 保存图片到视频流
            out.write(frame_res)
            # 在界面中显示处理结果
            cv2.imshow('frame', frame_res)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # 释放资源
    cap.release()
    out.release()
    # 关闭窗口
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    src_video = "./test.mp4"
    target_video = "./test_res.avi"
    start_detect_video(src_video, target_video)
