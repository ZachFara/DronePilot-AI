import cv2
import matplotlib.pyplot as plt
from UAV import UAV
import time


def main():
    # Initialize the drone
    drone_ip = "10.0.0.179"  # Replace with your drone's IP if needed
    uav = UAV(drone_ip)
    uav.connect()

    # Turn on the video stream
    uav.streamon()

    # Matplotlib setup for live display
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots()
    
    # Get the first frame to initialize the display
    frame = uav.get_frame_read().frame
    # img_display = ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img_display = ax.imshow(frame)
    ax.axis("off")  # Hide axes

    try:
        while True:
            time.sleep(.1)
            # Capture a frame from the drone's camera
            frame = uav.get_frame_read().frame

            frame_rgb = frame[:, :, ::-1]  # Reverse the last axis to convert BGR to RGB
            img_display.set_data(frame_rgb)
            
            # Update Matplotlib display
            img_display.set_data(cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB))
            plt.draw()
            plt.pause(0.001)  # Small pause to allow the display to refresh

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        # Cleanup: Turn off the video stream and close the Matplotlib window
        uav.streamoff()
        plt.close()

if __name__ == "__main__":
    main()