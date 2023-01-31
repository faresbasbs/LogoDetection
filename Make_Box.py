import cv2

def draw_rectangle(image_path, top_left, bottom_right):
    # Read the image
    image = cv2.imread(image_path)
    
    # Get the coordinates of the rectangle
    x1, y1 = top_left
    x2, y2 = bottom_right
    
    # Draw the rectangle on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
    
    #save the image
    cv2.imwrite(image_path,image)
