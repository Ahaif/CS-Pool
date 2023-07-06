import argparse
from PIL import Image, ExifTags
import os

def extract_metadata(image_file):
    try:
        image = Image.open(image_file)
        image_info = image._getexif()
        
        if image_info is None:
            print(f"No metadata found for {image_file}")
            return
        
        print(f"Metadata for {image_file}:")
        
        for tag, value in image_info.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
        
        print()
        
    except IOError as e:
        print(f"Error opening {image_file}: {str(e)}")
        

def main():
    parser = argparse.ArgumentParser(description='Scorpion - Image Metadata Parser')
    parser.add_argument('files', nargs='+', help='Image files to parse')

    args = parser.parse_args()
    files = args.files
    
    for file in files:
        if os.path.isfile(file) and file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            extract_metadata(file)
        else:
            print(f"Invalid file: {file}. Skipping...")
    

if __name__ == '__main__':
    main()
