import numpy

INPUT_SIZE = (64, 64)


def pimg(image):
  image = image.resize(INPUT_SIZE)
  image = numpy.array(image, dtype=numpy.float32) / 255.0
  return numpy.expand_dims(image, axis=0)
