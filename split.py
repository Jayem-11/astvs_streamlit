from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def split_video(video_path, chunk_size=18):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(video_path)
    duration = clip.duration

    chunk_counter = 0
    start_time = 0
    end_time = chunk_size

    while start_time < duration:
        ffmpeg_extract_subclip(video_path, start_time, min(end_time, duration), targetname=f"chunk{chunk_counter}.mp4")
        chunk_counter += 1
        start_time += chunk_size
        end_time += chunk_size
