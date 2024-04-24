import cv2
from cvzone.HandTrackingModule import HandDetector
from currency_converter import CurrencyConverter
import pyttsx3

# Initialize hand detector and currency converter
detector = HandDetector(detectionCon=0.8, maxHands=1)
currency_converter = CurrencyConverter()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Open the default camera (0)
video = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not video.isOpened():
    print("Error: Failed to open camera.")
    exit()

while True:
    # Read a frame from the video feed
    ret, frame = video.read()

    if not ret:
        print("Error: Failed to capture frame from camera.")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Use the hand detector to find hands in the frame
    hands, img = detector.findHands(frame)

    if hands:
        # Get landmarks of the detected hand
        lmList = hands[0]

        # Detect fingers up
        fingerUp = detector.fingersUp(lmList)

        # Perform currency recognition and conversion
        # Here, you need to implement the logic to recognize the currency sign
        # and convert it into the corresponding value in USD using currency_converter

        # For demonstration, let's assume currency_sign and currency_value
        currency_sign = "USD"
        currency_value = 20

        # Speak the recognized currency and its value
        speak(f"In your hand is {currency_value} {currency_sign}")

    # Display the frame
    cv2.imshow("frame", frame)

    # Check for the key 'k' to break out of the loop
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

# Release the video capture and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
