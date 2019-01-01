# Keras implementation of Image OutPainting

This is an implementation of [Painting Outside the Box: Image Outpainting](https://cs230.stanford.edu/projects_spring_2018/posters/8265861.pdf) paper from Standford University. 
Some changes have been made to work with 256*256 image:
  - Added Identity loss i.e from generated image to the original image
  - Removed patches from training data. (training pipeline)
  - Replaced masking with cropping. (training pipeline)
  - Added convolution layers.

## Results
The model was train with [scrapped beach data](https://drive.google.com/open?id=1hKIn-Z8Uf3voESbJZVsapLHESPabjjrb)  for 25 epochs.
![Demo](https://i.imgur.com/ZHtoeDF.jpg)

#### Recursive painting
![Demo](http://i.imgur.com/pDUpzcY.jpg)

### Install Requirements
sudo pip3 install -r requirements.txt

## Get Started

1. Prepare Data:
      ```sh
      # Downloads the beach data and converts to numpy batch data
      # saves the Numpy batch data to 'data/prepared_data/'
      sh prepare_data.sh
      ```
2. Build Model
    * To build Model from scratch you can directly run 'outpaint.ipynb'
  <br/>OR<br/>
    * You can [Download](https://drive.google.com/open?id=1MfXsRwjx5CTRGBoLx154S0h-Q3rIUNH0) my trained model and move it to 'checkpoint/' and run it.

## References
* [Painting Outside the Box: Image Outpainting](https://cs230.stanford.edu/projects_spring_2018/posters/8265861.pdf)