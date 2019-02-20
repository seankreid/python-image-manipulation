# Python Image Manipulator

This python application allows users to load images and rotate them.

## Getting Started

The app can be downloaded an ran on its own, no other files needed besides the image you want to use.

### Prerequisites

To run this application. You will need python3, the tkinter module, and pillow module.

```
pip3 install pillow
```

```
pip3 install tkinter
```

### Running
```
python3 image.py
```
### Using

- Has a menu with three options: "Load image", "Rotate 90 Clockwise", "Rotate 90 Counter-clockwise".
- **Load Image:** Menu option allows user to select an image from their system, once completed the file path will appear in the box.
- **Rotate 90 Degrees Clockwise:** Menu option loads the image that is set in the text field into Pillow, it then rotates the image 90 degrees clockwise and then saves the image.
- **Rotate 90 Degrees Counter-Clockwise:** Menu option loads the image that is set in the text field into Pillow, it then rotates the image 90 degrees counter-clockwise and then save the image.
- **Close:** Close the program.

### Built With

* [Python3](https://www.python.org/downloads/) - Language used
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Used for GUI
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Used for image manipulation

### Authors

* **Sean Reid** - [Sean Reid](https://github.com/seankreid)
