from picamera2 import Picamera2
import time


# returns camera instance
def get_camera():
    camera = Picamera2()
    camera.configure(camera.create_still_configuration(main={"size": (640, 480)}))
    camera.start()
    time.sleep(0.5)  # allow camera to stabilize
    return camera


# Takes in camera instance and preview time
# displays camera preview for the indicated amount of time
def camera_preview(camera, preveiw_time):
    # headless-safe preview delay
    time.sleep(max(0.0, float(preveiw_time)))


# Takes in camera instance, output image location, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the image is taken and stored in the indicated location
# the preview is stopped if it was started
def capture_image(camera, image_out_location, countdown_time=0, preview=False):

    if preview:
        camera_preview(camera, countdown_time)

    if int(countdown_time) > 0:
        print(f"Image will be taken in {countdown_time} seconds...")
        for i in range(int(countdown_time), 0, -1):
            print(i)
            time.sleep(1)

    camera.capture_file(image_out_location)
    return image_out_location


# Takes in camera instance, output video location, video length, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the video is taken for the indicated amount of time 
# and stored in the indicated location
# the preview is stopped if it was started
def capture_video(camera, video_out_location, video_length, countdown_time=0, preview=False):

    if preview:
        camera_preview(camera, countdown_time)

    if int(countdown_time) > 0:
        print(f"Video will start recording in {countdown_time} seconds...")
        for i in range(int(countdown_time), 0, -1):
            print(i)
            time.sleep(1)

    camera.start_and_record_video(video_out_location, duration=video_length)
    return video_out_location
