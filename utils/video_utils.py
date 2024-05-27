import cv2

# Read in frames
def read_video(video_path):
    # Create a VideoCapture object to read the video from the specified path
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        # ret: boolean whether there is actually a frame i.e. end of video
        if not ret:
            break
        frames.append(frame)
    return frames

# Takes a list of frames and saves them as a video file using the XVID codec at 24 frames per second
def save_video(output_video_frames, output_video_path):
    # Output video format
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()