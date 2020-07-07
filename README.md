# Pneumonia classification using Xception Network
This projects uses Xception CNN for pneumonia classification with competitive results. We have used Keras and Tensorflow 2.0 for this network.

## Dataset
We have used CELL pneumonia dataset v2.

Dataset link: https://data.mendeley.com/datasets/rscbjbr9sj/2
Last dataset is under Licence CC BY 4.0.

Original paper:
D.S. Kermany et al., “Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning,” Cell, vol. 172, no. 5, pp. 1122-1131.e9, 2018, doi: 10.1016/j.cell.2018.02.010.


Structure:

The dataset contains 5232 CXRAY images from children, including 3883 characterized as depicting pneumonia (2538 bacterial and 1345 viral) and 1349 labeled as normal, from a total of 5856 patients. These 5323 CXRAY images constitute the training data. In addition, the pneumonia dataset includes its own test set with 234 normal images and 390 pneumonia images (242 bacterial and 148 viral) from 624 patients.

Classes for the classification algorithm were: PNEUMONIA and NORMAL.
## Xception network

Is a fully convolutional neural network, presented by Francois Chollet in 2016.

Original paper:
F. Chollet, “Xception: Deep Learning with Depthwise Separable Convolutions,” 2016. Accessed: Dec. 04, 2019. [Online]. Available: https://arxiv.org/abs/1610.02357.

### Architecture

### Pretrained models
Pretrained models can be found in Keras repository: https://keras.io/api/applications/xception/

## Preprocessing technique

We preprocess all the images with the following steps:

1. Remove any possible black band from the edges of the image.

2. Resize the image to achieve that the smaller edge is (for this research) 299 pixels long.

3. Extract the central 299 x 299 region.

Original paper:
F. Pasa, V. Golkov, F. Pfeiffer, D. Cremers, and D. Pfeiffer, “Efficient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization,” Sci. Rep., vol. 9, no. 1, p. 6268, 2019, doi: 10.1038/s41598-019-42557-4.

## Class Imbalance
The pneumonia dataset presents an imbalance ratio of 2.87.
Our results where obtained by:
* Performing Random Undersampling to balance the training data. 
* Hold-out 80-20 for as validation method.
* Cost Sensitive learning with weights [5.0, 0.5] respectively.
