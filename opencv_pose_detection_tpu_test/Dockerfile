FROM raspbian/stretch

RUN apt-get update
RUN apt-get install -y build-essential cmake pkg-config
RUN apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get install -y libxvidcore-dev libx264-dev
RUN apt-get install -y libgtk2.0-dev libgtk-3-dev
RUN apt-get install -y libatlas-base-dev gfortran
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y curl zip

RUN pip3 install opencv-python
#RUN pip3 install picamera
RUN pip3 install numpy
RUN pip3 install Pillow

RUN apt-get install -y libqtgui4
#RUN modprobe bcm2835-v4l2
RUN apt-get install -y libqt4-test

RUN apt-get install -y libilmbase-dev
RUN apt-get install -y libopenexr-dev
RUN apt-get install -y libgstreamer1.0-dev

RUN mkdir /home/scripts/
RUN mkdir /home/scripts/object_detections
WORKDIR /home/scripts/

#Install Tensorflow Edge CPU libraries
RUN apt-get install -y apt-transport-https
RUN apt-get install -y git
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list \
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y libedgetpu1-std \
&& apt-get install -y python3-edgetpu

RUN pip3 install Flask

RUN mkdir /home/scripts/pose_detection
COPY project-posenet /home/scripts/pose_detection
#COPY 


