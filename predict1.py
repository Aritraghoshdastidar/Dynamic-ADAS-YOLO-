import argparse
import torch
from pathlib import Path
from ultralytics import YOLO
import cv2
import os

def run_inference(image_path, weights_path, output_dir):
    # Load the YOLO model
    model = YOLO(weights_path)

    # Read the input image
    img = cv2.imread(image_path)
    if img is None:
        print(f"[ERROR] Could not read image at {image_path}")
        return

    # Predict with YOLO
    results = model.predict(source=img, show=False, save=False, conf=0.25, imgsz=640)

    # Annotate the image
    annotated_img = results[0].plot()  # Draw predictions

    # Prepare output directory and save image
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "output.jpg")
    cv2.imwrite(output_path, annotated_img)

    print(f"[INFO] Inference completed. Saved output to {output_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, required=True, help="Path to the model weights")
    parser.add_argument('--source', type=str, required=True, help="Path to the input image")
    parser.add_argument('--output', type=str, required=True, help="Directory to save the output image")
    args = parser.parse_args()

    # Run inference on the provided image
    run_inference(args.source, args.weights, args.output)

if __name__ == "__main__":
    main()
