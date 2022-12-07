import pyautogui

# Set the RGB values of the color you want to click
color = (255, 0, 0)

# Get the current screen width and height
width, height = pyautogui.size()

# Loop through all pixels on the screen
for x in range(width):
    for y in range(height):
        # Get the RGB values of the pixel at (x, y)
        pixel_color = pyautogui.pixel(x, y)

        # If the pixel color matches the color we want to click
        if pixel_color == color:
            # Move the mouse to the (x, y) coordinates
            pyautogui.moveTo(x, y)

            # Click the left mouse button
            pyautogui.click()