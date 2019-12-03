### tflite_rpi3
Based on Debian Buster for ARMv7, it contains:

* Miniconda3
* Tensorflow Lite
* Jupyter

To run:

```console
docker run -it -p 8888:8888 -v <local_notebook_folder>:/root/notebooks --env="DISPLAY" --rm rio05docker/tflite_rpi:rpi3_test_3
```


