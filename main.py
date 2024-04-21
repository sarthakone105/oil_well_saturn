from ultralytics import YOLO
from pathlib import Path

# Define directories and file paths
sample_dir = "SampleData"
in_dir = f"{sample_dir}/Input"
out_dir = f"{sample_dir}/Output"

# Input file path
input_file = f"{in_dir}/24_jpg.rf.ddd99848038b1a40f63a854139acc8d3.jpg"

# Output file path
name = Path(input_file).stem
output_file = f'{out_dir}/{name}_pred.jpg'

# Load the YOLO model
model = YOLO('/home/satyukt/Sarthak/oil_well_saturn/Models/best.onnx')

# Run inference on the input file
results = model(input_file)

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
