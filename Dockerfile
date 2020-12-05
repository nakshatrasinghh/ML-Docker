#@ Uses a base python3.7.5 slim image as the base OS kernel
FROM python:3.7.5-slim

#@ Copy source to the destination directory
COPY ./requirements.txt /requirements.txt

#@ Current directory
WORKDIR /

#@ Execute the python command
RUN pip3 install -r requirements.txt

#@ Copy all the files to working directory
COPY . /

#@ Command to use  
ENTRYPOINT [ "python3" ]

#@ Execute `train.py` file with ENTRYPOINT during runtime of image 
CMD [ "train.py" ]
