FROM rio05docker/tflite_rpi:rpi3_test_4.2

RUN apt-get update && apt-get install -y curl zip

RUN mkdir /home/scripts/object_detections/tpu_inference

WORKDIR /home/scripts/object_detections/tpu_inference

COPY detect_picamera.py /home/scripts/object_detections/tpu_inference

#Installing the Edge TPU runtime (see:https://coral.ai/docs/accelerator/get-started/)
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN apt-get update && apt-get install -y libedgetpu1-std

ENTRYPOINT /bin/sh -c /home/scripts/object_detections/download.sh && /bin/bash



