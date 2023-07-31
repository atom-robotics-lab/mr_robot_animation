import cv2
import keyboard
import pygame
from pygame.locals import *

def play_video(video_path):
    pygame.init()

    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    pygame.display.set_mode((1920, 1080), DOUBLEBUF | FULLSCREEN)

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
        scale_factor = 0.8
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)

        surface = pygame.surfarray.make_surface(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        pygame.display.get_surface().blit(surface, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                cap.release()
                pygame.quit()
                return

        if keyboard.is_pressed('1'):
            video_path = video_paths['1']
            cap = cv2.VideoCapture(video_path)

        elif keyboard.is_pressed('2'):
            video_path = video_paths['2']
            cap = cv2.VideoCapture(video_path)

        elif keyboard.is_pressed('3'):
            video_path = video_paths['3']
            cap = cv2.VideoCapture(video_path)

if __name__ == '__main__':
    video_paths = {
        '1': 'default.mp4',  # Replace 'video1.mp4' with the path to your first video
        '2': 'bored.mp4',  # Replace 'video2.mp4' with the path to your second video
        '3': 'angry.mp4'   # Replace 'video3.mp4' with the path to your third video
    }

    play_video(video_paths['1'])
