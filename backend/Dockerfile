# base image  
FROM python:3.8   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# install dependencies  


# copy whole project to your docker home directory. 
COPY . $DockerHOME  
RUN pip install --upgrade pip  
COPY requirements.txt .
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 0.0.0.0:0.0.0.0