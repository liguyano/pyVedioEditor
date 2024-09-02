from moviepy.editor import VideoFileClip

def clip_video(input_path, output_path, start_time, end_time):
    """
    截取视频片段。

    :param input_path: 输入视频文件的路径。
    :param output_path: 输出视频文件的路径。
    :param start_time: 视频片段的开始时间，格式为（小时，分钟，秒）或秒数。
    :param end_time: 视频片段的结束时间，格式同上。
    """

    # 加载视频文件
    video = VideoFileClip(input_path)

    # 设置开始时间和结束时间
    start_time_in_seconds = convert_to_seconds(start_time)
    end_time_in_seconds = convert_to_seconds(end_time)

    # 截取视频片段
    clipped_video = video.subclip(start_time_in_seconds, end_time_in_seconds)

    # 保存视频片段
    clipped_video.write_videofile(output_path, codec='libx264')

    # 释放资源
    video.close()

def convert_to_seconds(time_tuple):
    """
    将时间元组转换为秒数。
    :param time_tuple: 时间元组，格式为 (小时, 分钟, 秒) 或直接提供秒数。
    :return: 时间以秒为单位。
    """
    if isinstance(time_tuple, tuple) and len(time_tuple) == 3:
        hours, minutes, seconds = time_tuple
        return hours * 3600 + minutes * 60 + seconds
    else:
        return time_tuple

# 使用示例
input_video_path = 'C:/Users/kurum/OneDrive - jxstnu.edu.cn/图片/Nitro/右矿中学22年元旦晚会 - 1.右矿中学22年元旦晚会(Av343121698,P1).mp4'
output_video_path = './output.mp4'
start = (1, 36, 0)  # 开始时间为视频的15秒处
end = (1, 41, 0)    # 结束时间为视频的45秒处

clip_video(input_video_path, output_video_path, start, end)