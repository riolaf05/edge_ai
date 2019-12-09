#!/bin/bash

# Get TF Lite model and labels
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip

unzip mobilenet_v1_1.0_224_quant_and_labels.zip -d /home/scripts/models

rm mobilenet_v1_1.0_224_quant_and_labels.zip

# Get version compiled for Edge TPU
wget https://dl.google.com/coral/canned_models/mobilenet_v1_1.0_224_quant_edgetpu.tflite \
-O /home/scripts/models/mobilenet_v1_1.0_224_quant_edgetpu.tflite

echo -e "Downloaded files are in /home/scripts/models"
