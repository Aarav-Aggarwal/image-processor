# Pure Python Image Processor

A small image processor written in plain Python (no NumPy, OpenCV or Pillow).
An image is stored as a list of lists, with values from 0 (black) to 255 (white).

## Functions

### invert_image(image)
Replaces every pixel with 255 minus its value, so black becomes white and white becomes black.
Output: the first pixel 0 becomes 255, and 50 becomes 205.

### threshold(image, limit)
Pixels brighter than limit become 255 (white), all others become 0 (black).
Output: with limit 100, the image becomes only black and white.

### brighten(image, amount)
Adds amount to every pixel, but never goes above 255.
Output: With amount 50, 0 becomes 50 and 240 becomes 255 as max is 255.

### flip_horizontal(image)
Flips the columns from each row which is called horizontal flipping.
Output: index 0,0 becomes 200 from 0 and index 0,4 becomes 0 from 200.

### crop(image, top, bottom, left, right)
Keeps only the rectangle between the given rows and columns. The start is included and the stop is not.
Output: crop(image, 1, 4, 1, 4) keeps rows 1-3 and columns 1-3, so the outer border is removed and a 3x3 image remains.

### blur_image(image)
Replaces each inside pixel with the average of the 3x3 block around it.
Output: on the spiky test image, the single 255 pixel spreads into its 8 neighbors, which each become 28 (255 / 9, rounded).

## Border handling
Border pixels are left unchanged, because they do not have a full 3x3 neighborhood.
This is simple and keeps the image size the same. The downside is that the outer edge is not blurred.

## Extra test images
A second image with one bright pixel (spiky) is used for blur, because the gradient image looks the same after blur.

## Bonus: RGB
An RGB image is a grid where each pixel is [R, G, B].
### invert_rgb_image(image)
Replaces each of the three channels of every pixel with 255 minus its value.
Output: red (255,0,0) becomes (0,255,255), and black becomes white.

### ascii_art(image) (bonus)
Turns each pixel into a text character, from light to heavy: ' .:-=+*#%@'. Brighter pixels get heavier characters.
Output: 0 becomes a space, 50 becomes '.', and 200 becomes '#'.

### Importing a photo (bonus)
Uses Pillow only to open the file and convert it to grayscale. The pixel grid, resizing logic and ASCII conversion are done in plain Python.

## Note
Every function returns a new image and does not change the original.
