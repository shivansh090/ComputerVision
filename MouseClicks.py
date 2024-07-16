import cv2
import numpy as np 

# Initialize an array to store the coordinates of the 4 points
circles = np.zeros((4, 2), int)
count = 0  # Counter to keep track of the number of points selected

# Function to handle mouse events
def MousePoints(event, x, y, flags, params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:  # If left mouse button is clicked
        circles[count] = x, y  # Store the (x, y) coordinates
        count += 1  # Increment the count

# Set the desired width and height for the image
width, height = 400, 500
# Read the input image
img = cv2.imread("./Resources/tilted.jpeg")
# Resize the image to the specified dimensions
img = cv2.resize(img, (width, height))

while True:
    # Use a temporary copy of the image to avoid drawing multiple circles on the original image
    temp_img = img.copy()
    
    # Once 4 points are selected
    if count == 4:
        # Define the points for perspective transformation
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # Get the transformation matrix
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        # Apply the perspective transformation
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        # Show the transformed image
        cv2.imshow("Output", imgOutput)
        
    # Draw circles at the selected points
    for i in range(count):
        cv2.circle(temp_img, (circles[i][0], circles[i][1]), 5, (0, 0, 255), cv2.FILLED)
        
    # Display the image with the circles
    cv2.imshow("IMG", temp_img)
    # Set the mouse callback function to handle mouse events
    cv2.setMouseCallback("IMG", MousePoints)
    
    # Check for a key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
