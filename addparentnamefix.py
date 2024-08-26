import os
import re

# Set the path to your folder
folder_path = r"C:\Users\andrew\Desktop\textures_to_rename"

# List of keywords to keep in filenames
keywords = [
    "color", "Color", "Colour", "colour", "basecolour", "Basecolour", "base_colour", "Base_colour", "base_Colour", "Base_Colour", "basecolor", "Basecolor", "base_color", "Base_color", "base_Color", "Base_Color",
    "normal", "Normal", "roughness", "Roughness", "emission", "Emission", "Albedo", "AO", "Displacement", "Opacity", "preview", "Roughness", "Specular", "Translucency",
    "metallic", "Metallic", "metallness", "Metallness", "metal", "Metal", "rough", "Rough", "sss", "SSS", "alpha", "Alpha", "nmap", "spec", "Spec",
    "specular", "Specular", "mask", "Mask","albedo", "Albedo", "Displacement", "Translucency", "opacity"
]

# Function to extract keywords from the filename
def extract_keywords(filename):
    pattern = '|'.join(re.escape(keyword) for keyword in keywords)
    found_keywords = re.findall(pattern, filename, re.IGNORECASE)
    return '_'.join(found_keywords)

# Function to normalize filenames by replacing '-' and spaces with '_'
def normalize_filename(filename):
    return filename.replace('-', '_').replace(' ', '_')

# Traverse the directory and its subdirectories
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        base_name, ext = os.path.splitext(filename)
        
        # Get the parent folder name
        parent_folder_name = os.path.basename(root)
        
        # Extract keywords and create new filename
        extracted_keywords = extract_keywords(base_name)
        
        if extracted_keywords:
            new_filename = f"{parent_folder_name}-{extracted_keywords}{ext}"
        else:
            # If no keywords were found, use the base name as a fallback
            new_filename = f"{parent_folder_name}{ext}"
        
        # Normalize the filename
        new_filename = normalize_filename(new_filename)
        
        old_file_path = os.path.join(root, filename)
        new_file_path = os.path.join(root, new_filename)
        
        # Handle filename conflicts by adding a suffix only if necessary
        counter = 1
        original_new_file_path = new_file_path
        while os.path.exists(new_file_path):
            new_filename = f"{parent_folder_name}-{extracted_keywords}_{counter}{ext}"
            new_filename = normalize_filename(new_filename)
            new_file_path = os.path.join(root, new_filename)
            counter += 1
        
        # Rename the file only if the new path is different
        if old_file_path != new_file_path:
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

print("Files have been renamed successfully.")





## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'