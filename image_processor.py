
image = [
    [0,   50,  100, 150, 200],
    [10,  60,  110, 160, 210],
    [20,  70,  120, 170, 220],
    [30,  80,  130, 180, 230],
    [40,  90,  140, 190, 240],
]
#######################################################################################
#To invert an image like black to white.
def invert_image(image):
    result = []
    for row in image:
        new_row = []
        for value in row:
            new_value = 255-value
            new_row.append(new_value)
        result.append(new_row)
    return result

# Prints an image as a grid, one row per line
def print_image(image):
    for row in image:
        for value in row:
            print(f"{value:4}", end="")
        print()

print("Original Image:")
print_image(image)

print("\nInverted Image:")
print_image(invert_image(image))

#################################################################################

#Display image to threshold limit, if more then white if less then black.
def threshold(image, limit):
    result = []
    for row in image:
        new_row = []
        for value in row:
            if value > limit:
                value = 255
            else:
                value = 0
            new_row.append(value)
        result.append(new_row)
    return result
print("\nOriginal Image:")
print_image(image)
print("\nThresholded Image at limit 100:")
print_image(threshold(image, 100))
###########################################################################################

#To make the entire image more bright. 
def brighten(image, amount):
    result = []
    for row in image:
        new_row = []
        for value in row:
            new_value = value + amount
            if new_value > 255:
                new_value = 255
            new_row.append(new_value)
        result.append(new_row)
    return result
print("\nOriginal Image:")
print_image(image)
print("\nBrightened by 50:")
print_image(brighten(image, 50))

################################################################################

#right becomes left and left becomes right.
def flip_horizontal(image):
    result = []
    for row in image:
        new_row = row[::-1]
        result.append(new_row)
    return result
print("\nOriginal Image:")
print_image(image)
print("\nFlipped Horizontally:")
print_image(flip_horizontal(image))
#####################################################################################

#Crop the image to a specific rectangle defined by top, bottom, left, and right indices.
def crop(image, top, bottom, left, right):
    result = []
    for row in image[top:bottom]:
        new_row = row[left:right]
        result.append(new_row)
    return result
print("\nOriginal Image:")
print_image(image)
print("\nCropped (rows 1-3, columns 1-3):")
print_image(crop(image, 1, 4, 1, 4))
############################################################################################

#Bluriing the image by averaging the values of each pixel with its neighbors.
def blur_image(image):
    result = []
    for row in image:
        result.append(row[:])
    for r in range(1, len(image)-1):
        for c in range(1, len(image[0])-1):
            total = 0
            for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        total += image[r+dr][c+dc]
            result[r][c] = round(total / 9)
    return result

print("\nOriginal Image:")
print_image(image)
print("\nBlurred Image:")
print_image(blur_image(image))

# The gradient image looks unchanged after blur, so this spiky image shows the effect clearly.
spiky = [
    [0, 0,   0, 0, 0],
    [0, 0,   0, 0, 0],
    [0, 0, 255, 0, 0],
    [0, 0,   0, 0, 0],
    [0, 0,   0, 0, 0],
]

print("\nSpiky Image:")
print_image(spiky)

print("\nBlurred Spiky Image:")
print_image(blur_image(spiky))

#The function is not defined for edges because the edges dont have a 3x3 matrix around them.
#So they are left untouched as is and code is only aplied for the ones that can be solved.
#The disadvantage of this is that the edges will note blur at all.

#########################################################################################################

rgb_image = [
    [[255, 0, 0],   [0, 255, 0],   [0, 0, 255]],
    [[255, 255, 0], [0, 0, 0],     [255, 255, 255]],
]

def print_rgb_image(image):
    for row in image:
        for pixel in row:
            print(f"({pixel[0]:3},{pixel[1]:3},{pixel[2]:3})", end=" ")
        print()

print("RGB Image:")
print_rgb_image(rgb_image)

def invert_rgb_image(image):
    result = []
    for row in image:
        new_row = []
        for pixel in row:
            new_pixel = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]
            new_row.append(new_pixel)
        result.append(new_row)
    return result
print("\nInverted RGB Image:")
print_rgb_image(invert_rgb_image(rgb_image))