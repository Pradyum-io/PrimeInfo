import sys
from PIL import Image
import os

def crop_team_image(input_path):
    try:
        img = Image.open(input_path)
    except IOError:
        print(f"Error: Could not open {input_path}")
        return
    
    width, height = img.size
    mid_x = width // 2
    mid_y = height // 2
    
    # Define the bounding boxes for the 4 quadrants (left, upper, right, lower)
    boxes = {
        'avery-chen.jpg': (0, 0, mid_x, mid_y),
        'jordan-patel.jpg': (mid_x, 0, width, mid_y),
        'taylor-brooks.jpg': (0, mid_y, mid_x, height),
        'morgan-ellis.jpg': (mid_x, mid_y, width, height)
    }
    
    output_dir = os.path.dirname(os.path.abspath(input_path))
    
    for filename, box in boxes.items():
        cropped_img = img.crop(box)
        output_path = os.path.join(output_dir, filename)
        cropped_img.save(output_path, quality=95)
        print(f"Saved {filename}")

if __name__ == "__main__":
    input_file = "team-grid.jpg"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_file)
    
    if os.path.exists(input_path):
        crop_team_image(input_path)
    else:
        print(f"Could not find '{input_file}' in the images directory.")
        print("Please save the attached image as 'team-grid.jpg' in the assets/images directory and run this script.")
