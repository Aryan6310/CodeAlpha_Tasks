import cv2
from ultralytics import YOLO

# --- Task 4: Real-time Object Tracking System ---
# Modified by: Aryan Patel (CodeAlpha Internship 2025)

def run_vision_system():
    # Load the YOLOv8 model (Nano version for speed)
    print("🚀 Initializing Aryan's Vision Engine...")
    model = YOLO('yolov8n.pt')

    # Initialize Webcam (0 is default)
    video_stream = cv2.VideoCapture(0)

    if not video_stream.isOpened():
        print("❌ System Error: Webcam access denied.")
        return

    print("✅ Tracking Active! Press 'ESC' or 'Q' to terminate.")

    while True:
        # Capture frame-by-frame
        ret, frame = video_stream.read()
        if not ret:
            break

        # Process the frame using the track method
        # We use conf=0.5 to only show high-confidence detections
        results = model.track(frame, persist=True, conf=0.5, verbose=False)

        # Generate the visual box overlays
        output_frame = results[0].plot()

        # --- Minor Visual Change: Add a Status Header ---
        cv2.putText(output_frame, "Aryan Patel - CodeAlpha Task 4", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Display object count if available
        if results[0].boxes.id is not None:
            obj_count = len(results[0].boxes.id)
            cv2.putText(output_frame, f"Tracking: {obj_count} Objects", (20, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Show the processed video
        cv2.imshow("Aryan's AI Vision System", output_frame)

        # Exit logic (handles both Q and ESC key)
        key = cv2.waitKey(1)
        if key & 0xFF == ord("q") or key == 27:
            break

    # Shutdown sequence
    video_stream.release()
    cv2.destroyAllWindows()
    print("🔒 System offline.")

if __name__ == "__main__":
    run_vision_system() 