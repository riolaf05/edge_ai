### tflite_rpi4
Based on Raspbian Stretch, it contains:

* Python 3.6.9
* Tensorflow Lite
* Picamera module

To run with Raspberry Camera:

```console
docker run -it -d --restart unless-stopped --privileged --device /dev/gpiomem rio05docker/tflite_rpi3_picamera:rpi3_test_4
```

To run with Tensorflow Lite demo (on x86 with Quemu):

```console
docker run -it -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static -v <host_path>:/home/scripts/samples --name tflite_image_classification rio05docker/tflite_rpi:rpi3_test_4.1 python3.5 /home/scripts/pi_image_classifier_tflite_demo.py --image samples/<image_name>.jpg
```

on ARM (i.e. RaspberryPi):

```console
docker run -it -v <host_path>:/home/scripts/samples --name tflite_image_classification rio05docker/tflite_rpi:rpi3_test_4.1 python3.5 /home/scripts/pi_image_classifier_tflite_demo.py --image samples/<image_name>.jpg
```