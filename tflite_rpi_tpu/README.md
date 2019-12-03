### tflite_rpi3
Based on Debian Buster for ARMv7, it contains:

* Tensorflow Lite
* RPi.GPIO libraries
* Flask
* Coral Edge TPU drivers

To run:

```console
docker run -d --restart unless-stopped --privileged --device /dev/gpiomem  -p 5002:5002 -v /dev/bus/usb:/dev/bus/usb rio05docker/tflite_rpi3_tpu:rpi3_test_1
```


