from moviepy.editor import VideoFileClip

def convert_video_to_gif(input_path, output_path, start_time=None, duration=None):
    # 加载视频文件
    clip = VideoFileClip(input_path)
    
    # 如果指定了开始时间和持续时间，则剪辑视频
    if start_time is not None and duration is not None:
        clip = clip.subclip(start_time, start_time + duration)
    
    # 将视频保存为GIF格式
    clip.write_gif(output_path, fps=clip.fps)

# 使用方法
input_file = "./a.mp4"
output_file = "./a.gif"

# 可选参数：从视频的第5秒开始，转换接下来的10秒
start_time = 0  # 开始时间（秒）
duration = 10   # 持续时间（秒）

convert_video_to_gif(input_file, output_file, start_time=start_time, duration=duration)