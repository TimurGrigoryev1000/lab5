from helper_functions import camera, computer_vision, sensehat
### TO-DO: You may require more imports
import os
import time

def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is 
    
    # --- TO-DO: Should be a user input (match screenshot text) ---
    os.makedirs("data/images", exist_ok=True)

    print("Enter '1' if a background image is saved in data/images/background.png")
    print("Enter '2' to take the background image")
    choice = input().strip()

    take_background_image = (choice == "2") #TO-DO: Should be a user input

    if take_background_image:
        ### TO-DO: Countdown image capture of background  
        print("Get out of the scene")
        print("Background image will be taken in 10 seconds...")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)

        preview = False
        countdown = 0
        camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=countdown, preview=preview) #DO NOT MODIFY, function call must work as is 
    
    # --- TO-DO: Should be a user input (match screenshot text) ---
    arm_answer = input("Would you like to arm the system? y/n\n").strip().lower()
    arm_system = (arm_answer == "y") #TO-DO: Should be a user input

    if arm_system:
        interval = int(input("Enter the interval between test images in seconds:\n").strip()) #TO-DO: Should be a user input
        t1 = float(input("Enter the threshold t1:\n").strip()) #TO-DO: Should be a user input
       
        ### TO-DO: Countdown to monitoring
        print("Monitoring will begin in 10 seconds...")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)

        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval) #DO NOT MODIFY, function call must work as is 
            person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is 
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()
