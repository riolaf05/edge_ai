FROM rio05docker/tflite_rpi:rpi3_test_4.1

RUN apt-get update && apt-get install -y curl zip

RUN mkdir /home/scripts/object_detections

WORKDIR /home/scripts/object_detections

COPY download.sh /home/scripts/object_detections
RUN chmod +x /home/scripts/object_detections/download.sh
COPY detect_picamera.py /home/scripts/object_detections
COPY annotation.py /home/scripts/object_detections

ENTRYPOINT ["/bin/bash/" "home/scripts/object_detections/download.sh"]

