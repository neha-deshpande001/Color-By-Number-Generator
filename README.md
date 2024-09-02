# Color-By-Number-Generator

A program that converts a simple color image into a color-by-number image. This includes finding shapes in the image using OpenCV's contours, finding center of each shape, and labeling it with the correct color label. The key has the corresponding colors and labels and resizes based on the number of colors and size of the image.


### Flower Example
Original             |  Color-By-Numbers
:-------------------------:|:-------------------------:
![flower](https://github.com/user-attachments/assets/b8d4a9a3-9b76-42a4-858d-8f41d0e33deb) |  ![final_flower](https://github.com/user-attachments/assets/77677b84-d496-4f51-a785-6fbc2fa0be29)

### Car Example
Original             |  Color-By-Numbers
:-------------------------:|:-------------------------:
![car](https://github.com/user-attachments/assets/6ed179cd-e62f-46a1-a9bd-6f37f3f34f20) |  ![final_car](https://github.com/user-attachments/assets/f2ad5457-9a53-4285-84c1-ce6979b90a77)

### Failure Cases
Here's some instances where the program does not work:
- The label will not appear when the calculated center of the shape is not in the shape, or it is inside a different shape
- For a shape with a outline, the outline will either appear very thick or it will appear as a second shape. Either way, the label will not display
- Shapes next to each other that have colors that are too similar will combine

Original             |  Color-By-Numbers
:-------------------------:|:-------------------------:
![failure_cases](https://github.com/user-attachments/assets/17121086-ff8b-4293-9f9a-e82146758baa) |  ![final_failure_cases](https://github.com/user-attachments/assets/1fd68bf5-131a-4e89-9cbb-3dbbacaf019e)
