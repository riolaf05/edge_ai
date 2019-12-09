import argparse
import io
import time
import numpy as np
import picamera

from PIL import Image
from tflite_runtime.interpreter import Interpreter

labels=load_labels("/home/scripts/models/labels_mobilenet_quant_v1_224.txt")
interpreter = Interpreter("/home/scripts/models/mobilenet_v1_1.0_224_quant.tflite")
interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']

def load_labels(path):
  with open(path, 'r') as f:
    return {i: line.strip() for i, line in enumerate(f.readlines())}

def classify_image(interpreter, image, top_k=1):
  """Returns a sorted array of classification results."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  # If the model is quantized (uint8 data), then dequantize the results
  if output_details['dtype'] == np.uint8:
    scale, zero_point = output_details['quantization']
    output = scale * (output - zero_point)
  
  ordered = np.argpartition(-output, top_k)
  return [(i, output[i]) for i in ordered[:top_k]]

def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def main():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  #parser.add_argument('--model', help='File path of .tflite file.', required=True)
  #parser.add_argument('--labels', help='File path of labels file.', required=True)
  parser.add_argument('--image', help='File path of image file to detect.', required=True)
  args = parser.parse_args()
  
  image = Image.open(args.image)
  image=image.convert('RGB').resize((width, height), Image.ANTIALIAS)

  results = classify_image(interpreter, image)
  print("The image contains:", labels[results[0][0]])

if __name__ == "__main__":
    main()