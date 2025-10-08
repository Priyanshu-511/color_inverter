from PIL import Image
import sys

def invert_image_colors(input_path, output_path=None):
    try:
        img = Image.open(input_path)
        
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        pixels = img.load()
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (255 - r, 255 - g, 255 - b)
        
        if output_path:
            img.save(output_path)
            print(f"Inverted image saved to: {output_path}")
        
        return img
    
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_image> [output_image]")
        print("Example: python script.py input.jpg output.jpg")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        name_parts = input_path.rsplit('.', 1)
        if len(name_parts) == 2:
            output_path = f"{name_parts[0]}_inverted.{name_parts[1]}"
        else:
            output_path = f"{input_path}_inverted.png"
    
    invert_image_colors(input_path, output_path)
    print("Done!")

if __name__ == "__main__":
    main()