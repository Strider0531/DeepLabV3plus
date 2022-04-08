This DeepLabV3plus project is the modified 
Human-Image-Segmentation-with-DeepLabV3Plus-in-TensorFlow project.

================================================================

DeepLabV3plus project configured for human segmentation. Example images of DeepLabV3+ algorithm are on the test_images/mask folder.

Project developed in Python 3.7

Using of human segmentation project:

- Recognition from image:

Open Flask_Api_DeepLabV3+.ipynb notebook, put your ngrok token and run all cells. Use webpage for uploading image with human (in .png format). Click on "predict image" button, after that API must demonstrate resulted image with input image and mask. 

- Training of custom DeepLabV3+ model in Colab:

First of all you should prepare custom dataset. Set data_path with your dataset folder with images and their masks. Set in "new_data/train/" augment = True for data_augmentation (this function increase dataset by 4 times).

Secondly, you should set dataset_path with "new_data" path.

Also you can change other folders paths and learning configurations. For more information see tutorial bellow.

https://youtu.be/4LhUpCWBzT8

=======================================================================

Link on Human-Image-Segmentation-with-DeepLabV3Plus-in-TensorFlow project:
GitHub : https://github.com/nikhilroxtomar/Human-Image-Segmentation-with-DeepLabV3Plus-in-TensorFlow


