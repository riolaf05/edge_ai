#See: https://cxlabs.sap.com/2019/10/07/containerizing-a-tensorflow-lite-edge-tpu-ml-application-with-hardware-access-on-raspbian/
FROM debian:buster

RUN apt update
#mainly required for the installation of the Edge TPU dependencies.
#zlib1g-dev libjpeg-dev is the C Bindings for Python that will be compiled during installation time in ARM-based Raspberry Pi
RUN apt install curl gnupg ca-certificates zlib1g-dev libjpeg-dev -y 

RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN apt update
#This is used to support the Coral Edge TPU (via USB Accelerator)
RUN apt install libedgetpu1-std python3 python3-pip python3-edgetpu  -y 

RUN curl https://dl.google.com/coral/python/tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl > tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl
RUN pip3 install tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3"]
#put Flask api server with AI model here
CMD [""] 