### tflite_rpi4
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To run with Raspberry Camera:

```console
docker run -it -d --restart unless-stopped --privileged --device /dev/gpiomem rio05docker/tflite_rpi3_tpu:rpi3_test_4
```

To run with Tensorflow Lite demo:

```console
docker run -it -d rio05docker/tflite_rpi3_tpu:rpi3_test_4 /home/scripts/pi_image_classifier_tflite_demo.py --image <image_path>
```
