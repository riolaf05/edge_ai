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

RUN pip3 install opencv-python

RUN apt-get install -y libqtgui4
#RUN modprobe bcm2835-v4l2
RUN apt-get install -y libqt4-test

RUN apt-get install -y libilmbase-dev
RUN apt-get install -y libopenexr-dev
RUN apt-get install -y libgstreamer1.0-dev