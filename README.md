# Histopathological_Cancer_Detector

Multiple models are created to learn and identify Histopathological cancer images.
Specifically Colon cancer cells are identified in all three models. 
For more details on how it works do refer the [documentation](./Documentations).
_________________________________________________________________________________
#### This README file is written by 

Aashik Sharif B  
121003003  
B.Tech CSE  
SASTRA Deemed to be University  
_________________________________________________________________________________
# To Run


[cancer_tissue](./images/cancer_tissue.tif)  

I assume that you have installed reqired **python packages**. This notebooks were run in kaggle.  
There are three models that are applied for an given datasets.  
There are two different datasets. Dataset in Link 1 is applied for model 1 & 2.  
Dataset in Link 2 is applied for model 3. 

The public datasets was obtained and forked into kaggle notebook from the following link which was available for competition:  
##### 1) https://www.kaggle.com/c/histopathologic-cancer-detection
##### 2) https://www.kaggle.com/andrewmvd/lung-and-colon-cancer-histopathological-images


##There are total of **3 Models** that are made for this mini-project.
### 1) [Model 1 - Xception and Nasnet Mobile Architecture](./Models/model1.ipynb)

Here, Xception and NASNetMobile architecture with Avg-pooling layeris concatenated. Click the header or this [link](./Models/model1.ipynb) to open the notebook.  
The maximum accuracy we gained from the model is **97.4%** for training data and **96%** for testing data. The model architecture is as follows below. 

![model 1 architecture](./images/model1.png)
 
### 2) [Model 2 - Inception V3 architecture](./Models/model2.ipynb)  
    
Since the previous model has overfitted, the model and parameters instructed in base paper is followed in new model. Here, InceptionV3 architecture with max-pooling layeris used.
It is clearly evident here that the model is neither overfitting nor underfitting. Model 1 is actually overfitting and model 2 can be alternative for it.  
Click the header or this [link](./Models/model2.ipynb) to open the notebook.  The model architecture is as follows below. 

The outputs generated in this notebook are also stored in this [link](.\Model 2 outputs)
![model 1 architecture](./images/model2.png)
   
### 3) [Model 3 - NASNet Mobile architecture](./Models/model3.ipynb)  

 Here, only NASNetMobile architecture with max-pooling layer and average-pooling layeris used.  
 Due to poor augmentation of data here, the **accuracy of model didnâ€™t go more than 54%** and had **high loss  rate**. Hence this model is not further used.   
 The model architecture is as follows below. 

![model 1 architecture](./images/model3.png)
 
 Click the header or this [link](./Models/model3.ipynb) to open the notebook.  

_________________________________________________________________________________
## GUI Application

Using python flask package an Interactive webpage is also used to upload the image and find weather the Histopathological image is cancer positive or not. i.e Adenocarcinoma or adenoma.  
To run this GUI application simply clone this repository in your system and run **app.py** in a proper GUI application such as VS Code.(Assuming you have python and its required packages installed).
This GUI Application is based on model 2 that was trained. To try model 1 or model 3 generate and save its h5 file and change its name in **output.py**.
The following screenshots are how the GUI application  works on.   
[image1](./images/app1.png)  
[image1](./images/app2.png)  
[image1](./images/app3.png)  
_________________________________________________________________________________

For futher queries or doubts:  
* mailto: ashiktcy.s@gmail.com  
* LinkedIn: [AashikSharif](https://www.linkedin.com/in/aashik-sharif-b-44ba40b5/)

_________________________________________________________________________________


version https://git-lfs.github.com/spec/v1
oid sha256:5a6e28a9e47885176f9efced0a869cea638536f74d07814608a9d4fd7b416e0d
size 4062
