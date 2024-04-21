from ultralytics import YOLO
from pathlib import Path
from Utils.sideScripts import convert_tif_to_jpg

# Define directories and file paths
sample_dir = "SampleData"
in_dir = f"{sample_dir}/Input"
out_dir = f"{sample_dir}/Output"
int_dir = "Intermediate/Images/"

# Input file path
input_file = f"{in_dir}/tm583bc2ak1w1akq71.tif"
name_jpg = Path(input_file).stem
converted_jpg_file_path = f"{int_dir}/{name_jpg}.jpg"

#  Convert tif into jpg and save it in input folder using the same name as input tif file
convert_tif_to_jpg(input_file, converted_jpg_file_path)

# Output file path
output_file = f'{out_dir}/{name_jpg}_pred.jpg'

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
    result.save(filename=output_file)

# Display the result image
result.show()
