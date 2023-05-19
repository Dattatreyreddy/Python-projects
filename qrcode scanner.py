import cv2
from pyzbar import pyzbar

def scan_qr_code():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes
        qr_codes = pyzbar.decode(gray)

        # Process each detected QR code
        for qr_code in qr_codes:
            # Extract the data from the QR code
            data = qr_code.data.decode("utf-8")
            print("QR Code:", data)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Wait for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

# Start the QR code scanning
scan_qr_code()
