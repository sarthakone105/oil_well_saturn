from PIL import Image

def convert_tif_to_jpg(tif_path, jpg_path):
    try:
        # Open the TIF image
        tif_image = Image.open(tif_path)
        # Convert and save as JPG
        tif_image.convert("RGB").save(jpg_path, "JPEG")
    except Exception as e:
        print(f"Error converting {tif_path} to JPG: {e}")

