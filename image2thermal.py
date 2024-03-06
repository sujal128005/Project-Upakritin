import cv2
import numpy as np
import matplotlib.pyplot as plt
def apply_thermal_effect(image_path, colormap='jet'):
    """
    Applies a thermal-like effect to an image.

    Args:
        image_path (str): Path to the input image file.
        colormap (str, optional): Name of the colormap to use. 
                                  Defaults to 'jet'. See Matplotlib documentation
                                  for other options.

    Returns:
        numpy.ndarray: The image with the thermal effect applied.
    """

    # Load the image and convert to grayscale
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize grayscale image for better color mapping
    normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Apply the colormap
    colormap = plt.get_cmap(colormap)
    thermal_image = colormap(normalized_image)

    # Convert the result from RGBA to BGR (OpenCV format)
    thermal_image = cv2.cvtColor(thermal_image, cv2.COLOR_RGBA2BGR) * 255  # Multiply for visibility

    return thermal_image

# Example usage
image_path = 'c:\\Users\\connt\\Downloads\\imgofpeople.jpeg'  # Replace with your image path
thermal_image = apply_thermal_effect(image_path)

# Display the result
cv2.imshow("Original Image", cv2.imread(image_path))
cv2.imshow("Thermal Image", thermal_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
