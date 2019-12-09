### tflite_rpi4
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To run with Raspberry Camera:

```console
docker run -it -d --restart unless-stopped --privileged --device /dev/gpiomem rio05docker/tflite_rpi3_picamera:rpi3_test_4
```

To run with Tensorflow Lite demo:

```console
docker run -it -d rio05docker/tflite_rpi3_picamera:rpi3_test_4.1 -v <image_path>:/home/scripts/samples --name tflite_image_classification python3.5 /home/scripts/pi_image_classifier_tflite_demo.py --image <image_path>
```
