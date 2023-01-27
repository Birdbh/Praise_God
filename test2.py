import cv2
import numpy as np

# Initialize the camera and get the frame size
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Load the haar cascade for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the cursor position
cursor_x = frame_width // 2
cursor_y = frame_height // 2

while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If a face is detected, track its movement
    if len(faces) > 0:
        # Get the coordinates of the face
        (x, y, w, h) = faces[0]

        # Calculate the center of the face
        face_x = x + w // 2
        face_y = y + h // 2

        # Calculate the movement of the face relative to the center of the frame
        delta_x = face_x - frame_width // 2
        delta_y = face_y - frame_height // 2

        # Update the cursor position based on the face movement
        cursor_x += delta_x
        cursor_y += delta_y

        # Clamp the cursor position within the frame bounds
        cursor_x = max(0, min(cursor_x, frame_width))
        cursor_y = max(0, min(cursor_y, frame_height))

        # Use the cursor position to move the mouse cursor on the laptop
        # Replace "Mouse" with the name of your laptop's mouse device
        with open('/dev/input/Mouse', 'rb') as mouse_device:
            mouse_device.seek(0)
            mouse_device.write(bytearray([2, 0, cursor_x, 0, cursor_y]))

    # Display the frame
    cv2.imshow('Frame', frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the camera and destroy the window
cap.release()
cv2.destroyAllWindows()
