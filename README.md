# Color-By-Number-Generator

A program that converts a simple color image into a color-by-number image. This includes finding shapes in the image using OpenCV's contours, finding center of each shape, and labeling it with the correct color label. The key has the corresponding colors and labels and resizes based on the number of colors and size of the image.


### Flower Example


### Car Example


### Failure Cases
Here's some instances where the program does not work:
- the calculated center of the shape is not in the shape, or it is inside a different shape
- depending on the thickness of the outline, it will appear as a second shape and the key will not display
- two shapes next to each other that have colors that are too similar will combine