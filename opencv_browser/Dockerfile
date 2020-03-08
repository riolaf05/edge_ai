FROM rio05docker/tflite_rpi:pose_detection_tpu_test

RUN mkdir /home/scripts/browser/
COPY stream_test.py /home/scripts/browser/
WORKDIR /home/scripts/browser/

RUN pip3 install -r requirements.txt

CMD ["python3", "stream_test.py"]
