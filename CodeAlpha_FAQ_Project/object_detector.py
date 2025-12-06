# --- START OF object_detector.py CODE (Task 4) ---

import cv2
import numpy as np

# --- Configuration for YOLO Model ---
CONFIG_FILE = 'yolov3.cfg'
WEIGHTS_FILE = 'yolov3.weights'
NAMES_FILE = 'coco.names'
TEST_IMAGE = 'test_image.jpg' # Make sure this image is in the folder!

def run_object_detection():
    """
    Loads YOLO, performs object detection on a test image, and displays the result.
    """
    
    # Check if necessary files exist
    import os
    if not all(os.path.exists(f) for f in [CONFIG_FILE, WEIGHTS_FILE, NAMES_FILE, TEST_IMAGE]):
        print("❌ ERROR: Missing required files in the project folder!")
        print("Ensure you have yolov3.cfg, yolov3.weights (237MB), coco.names, and test_image.jpg.")
        return

    # Load class names (labels)
    with open(NAMES_FILE, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
        
    # Generate random colors for the bounding boxes
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Load YOLO network from the configuration and weights files
    net = cv2.dnn.readNet(WEIGHTS_FILE, CONFIG_FILE)
    
    # Load the image
    img = cv2.imread(TEST_IMAGE)
    height, width, _ = img.shape
    
    # Create the blob (pre-process the image for the model)
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
    
    # Perform a forward pass through the network
    net.setInput(blob)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    # Get the detection results
    outs = net.forward(output_layers)

    # --- Process the Detection Results ---
    class_ids = []
    confidences = []
    boxes = []
    
    # Loop over all outputs from the YOLO model
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            # Filter weak predictions (e.g., below 50% confidence)
            if confidence > 0.5:
                # Calculate the bounding box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression to remove redundant overlapping boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # --- Draw the Final Boxes on the Image ---
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            
            # Draw rectangle and label
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 3, color, 3)

    # --- Display the Result ---
    cv2.imshow("Object Detection Result (Task 4)", img)
    print("\n✅ Object Detection Complete.")
    print("Press any key to close the image window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Run the detection function
if __name__ == "__main__":
    run_object_detection()

# --- END OF object_detector.py CODE ---