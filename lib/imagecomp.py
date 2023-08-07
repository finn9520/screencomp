from PIL import Image, ImageChops


def compare_images(image1_path, image2_path, output_path, threshold_value=0):
    try:
        # Open the images
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)

        # Ensure both images have the same mode and size
        image1 = image1.convert('RGB')
        image2 = image2.convert('RGB')

        if image1.size != image2.size:
            raise ValueError("Both images must have the same size.")

        # Compare the images pixel by pixel
        diff = ImageChops.difference(image1, image2)

        # Highlight the differences with a color (red in this case)
        highlight_color = (255, 0, 0)
        diff = diff.convert("RGB")
        diff_data = diff.load()
        is_issues = False

        for x in range(diff.width):
            for y in range(diff.height):
                pixel = diff_data[x, y]
                if pixel[0] > threshold_value or \
                   pixel[1] > threshold_value or \
                   pixel[2] > threshold_value:
                    diff_data[x, y] = highlight_color
                    is_issues = True
                else:
                    diff_data[x, y] = (0, 0, 0)

        # Save the difference image
        diff.save(output_path)
        print(f"Difference image saved as {output_path}")
    except Exception as e:
        print(f"Error comparing images: {e}")
        is_issues = False

    return is_issues


