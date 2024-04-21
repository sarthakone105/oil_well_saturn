from ultralytics import YOLO
from pathlib import Path
from Utils.sideScripts import convert_tif_to_jpg, convert_jpg_to_tif

# Define directories and file paths
sample_dir = "SampleData"  # Main directory
in_dir = f"{sample_dir}/Input"  # Input images directory
out_dir = f"{sample_dir}/Output"  # Output images directory
int_dir = "Intermediate/"  # Intermediate images directory

# Input file path
input_file = f"{in_dir}/tm583bc2ak1w1akq71.tif"
name_tif = Path(input_file).stem  # Extract filename without extension

# Paths for converted JPG, predicted JPG, and final predicted TIF files
converted_jpg_file_path = f"{int_dir}/{name_tif}.jpg"
predicted_jpg_file_path = f"{int_dir}/{name_tif}_pred.jpg"
final_pred_out_path = f"{out_dir}/{name_tif}_pred.tif"

# Convert TIF to JPG and save it in the intermediate folder using the same name as the input TIF file
convert_tif_to_jpg(input_file, converted_jpg_file_path)

# Load the YOLO model
model = YOLO('Models/best.onnx')

# Run inference on the input file
results = model(converted_jpg_file_path)

# Process the inference results
for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs

    # Save the result image
    result.save(filename=predicted_jpg_file_path)

# Convert predicted JPG to TIF format
convert_jpg_to_tif(predicted_jpg_file_path, final_pred_out_path)

# Display the result image
result.show()