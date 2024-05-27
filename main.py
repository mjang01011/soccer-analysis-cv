from utils import read_video, save_video
from trackers import Tracker
import cv2
from team_assigner import TeamAssigner

def main():
    # Read video
    video_frames = read_video('input_videos/08fd33_4.mp4')
    
    
    # Initialize Tracker
    tracker = Tracker('models/finetuned_yolo_v5/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')
    
    # # Save cropped image of a player
    # for track_id, player in tracks["players"][0].items():
    #     bbox = player['bbox']
    #     frame = video_frames[0]
        
    #     #crop bbox from frame
    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
    #     cv2.imwrite(f'output_videos/cropped_player.jpg', cropped_image)
    #     break
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            # print("Player id:", player_id)
            # print("Team:",team)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]
    
    # Draw object tracker
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')
    
if __name__ == '__main__':
    main()