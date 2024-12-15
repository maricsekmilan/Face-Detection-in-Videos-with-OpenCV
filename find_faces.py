import cv2
import sys

# Load the video file
video = cv2.VideoCapture("*ORIGINAL_VIDEO_NAME*.mp4")
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Get the total number of frames in the video

success, frame = video.read()  # Read the first frame of the video

# Extract frame dimensions (height and width)
height = frame.shape[0]
width = frame.shape[1]

# Load the face detection cascade (Haar Cascade XML file)
face_cascade = cv2.CascadeClassifier('faces.xml')

# Initialize the video writer to save the processed video
output = cv2.VideoWriter(
    '*OUTPUT_VIDEO_NAME*.avi',  # Output file name
    cv2.VideoWriter_fourcc(*'DIVX'),  # Codec for video compression
    30,  # Frames per second (FPS)
    (width, height)  # Frame dimensions
)

current_frame = 0  # Track the index of the current frame

while success:
    # Detect faces in the current frame
    faces = face_cascade.detectMultiScale(frame, 1.4, 2)  # You can change that to find the best settings (like 1.5, 2)
    for (x, y, w, h) in faces:
        # Draw a rectangle around each detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 4)
    output.write(frame)  # Write the processed frame to the output video

    # Read the next frame from the video
    success, frame = video.read()
    current_frame += 1

    # Calculate and display the processing progress percentage in a single line
    progress = (current_frame / total_frames) * 100
    sys.stdout.write(f"\rProcessing: {progress:.2f}%")  # Overwrite the current line in the console
    sys.stdout.flush()  # Ensure the progress is displayed immediately

# Release the video writer and other resources
output.release()
print("\nProcessing complete!")  # Print completion message
