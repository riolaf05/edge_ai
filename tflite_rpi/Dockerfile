FROM arm32v7/python:3.5-buster 

RUN mkdir /root/scripts

WORKDIR /root/scripts

RUN wget 'https://dl.google.com/coral/python/tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl'

RUN pip3 install tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl

RUN pip3 install numpy

RUN mkdir /root/scripts/models

COPY models/rss_model.h5 /root/scripts/models