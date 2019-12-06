### tflite_rpi4
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To run:

```console
docker run -d --restart unless-stopped --privileged --device /dev/gpiomem rio05docker/tflite_rpi3_tpu:rpi3_test_4
```


