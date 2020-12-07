# Mobile Classification- Docker 

A docker image for scoring a simple DTC model on training and testing sets using [Mobile price classification](https://www.kaggle.com/iabhishekofficial/mobile-price-classification) dataset. This is very simple image which prints out model scores on training and testing sets, scores can vary as `random seed` parameter is not a constant.

![](imgs/cmd.png)

## Dataset

For this project, I have used the [Mobile price classification](https://www.kaggle.com/iabhishekofficial/mobile-price-classification) dataset from kaggle. This is a simple and clean practice dataset for classification modelling. It consists of 2000 rows and 21 columns. The model will be based on “features” like _battery power, bluetooth and n_cores etc_. You can also use feature engineering to create new features. But we won't be dealing with feature engineering in this project. *On the side note, I used the [Rainbow CSV extension](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) for VS-code to make .csv files look more attractive 😅*. The dataset can be viewed [here](https://github.com/nakshatrasinghh/Mobile-Classification-Docker/blob/main/mobile.csv).

![](imgs/dataset.png)

## Training script

⚠️ All the necessary [packages](https://github.com/nakshatrasinghh/Mobile-Classification-Docker/blob/main/requirements.txt) must be installed using pip in order to train the model. ⚠️ Decision Tree Classifier was used to train the model. Training and testing scores of dtc model were printed out. Detailed code of the training script with comments [here](https://github.com/nakshatrasinghh/Mobile-Classification-Docker/blob/main/train.py).

![](imgs/train.png)

## Dockerfile

To create docker images and run them in containers, you need to have a [dockerfile](https://github.com/nakshatrasinghh/Mobile-Classification-Docker/blob/main/Dockerfile) which includes all the commands to be executed sequential for the application to run in the base OS kernel (in this case, Ubuntu). Firstly, we'll use a basic linux OS kernel with [python 3.7.5-slim edition](https://hub.docker.com/_/python) (keeps the image size small and very portable across different computers). 

⚠️***This image does not contain the common packages contained in the default tag and only contains the minimal packages needed to run python. Unless you are working in an environment where only the python image will be deployed and you have space constraints, it's highly recommend using the default image of this repository.*** ⚠️

![](imgs/docker.png)

Secondly, we copy the requirements.txt file in the root director, move to the root directory and pip install all the requirements. Finally, we execute python3 command along with the file we need to execute for tha application to run.  

