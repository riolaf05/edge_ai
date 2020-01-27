### tflite_rpi4.3
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To build: 

```console
docker build -t rio05docker/tflite_rpi:rpi3_test_4.3 .
docker push rio05docker/tflite_rpi:rpi3_test_4.3
```

To run with Raspberry Camera:

```console
docker run -it --privileged --device=/dev/vchiq -p 8000:8000 --rm rio05docker/tflite_rpi:rpi3_test_4.3  python3.5 detect_picamera.py --model /tmp/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite --labels /tmp/coco_labels.txt
```

