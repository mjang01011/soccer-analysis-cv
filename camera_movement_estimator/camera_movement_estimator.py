import pickle

class CameraMovementEstimator():
    def __init__(self):
        pass
    def get_camera_movement(self, frames, read_from_stub=False, stub_path=None):
        # Read the stub
        camera_movement = [[0,0]*len(frames)]