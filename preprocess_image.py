import numpy


async def pimg(image):
  image = image.resize((64, 64))
  image = numpy.array(image)
  image = image / 255.0
  image = numpy.expand_dims(image, axis=0)
  return image
