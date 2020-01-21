### tflite_rpi4.2
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To build: 

```console
docker build -t rio05docker/tflite_rpi3_picamera:rpi3_test_4.2 .
docker push rio05docker/tflite_rpi3_picamera:rpi3_test_4.2
```

To run with Raspberry Camera:

```console
docker run -it --privileged --device=/dev/vchiq -p 8000:8000 --rm rio05docker/tflite_rpi:rpi3_test_4.2  python3.5 detect_picamera.py --model /tmp/detect.tflite --labels /tmp/coco_labels.txt
```

To run with Tensorflow Lite demo (on x86 with Quemu):

```console
docker run -it -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --privileged --device=/dev/vchiq -p 8000:8000 --rm rio05docker/tflite_rpi:rpi3_test_4.2  python3.5 detect_picamera.py --model /tmp/detect.tflite --labels /tmp/coco_labels.txt
```
