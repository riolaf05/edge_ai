### tflite_rpi3
Based on Debian Buster for ARMv7, it contains:

* Miniconda3
* Tensorflow Lite
* Jupyter

To run:

```console
docker run -it --network=host -v /home/pi/Codice/notebooks/:/root/notebooks --env="DISPLAY" --restart=unless-stopped -d --name tflite_jupyter rio05docker/tflite_rpi:rpi3_test_3
```


