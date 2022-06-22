from random import randint
import csv
import ImageConvertor
import math

class Verschluessler():
  keys = []
  numbers = []
  def __init__(self):
    with open("NumbersForKeys.csv") as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei, delimiter=";")
        for row in csv_reader_object:
            self.keys.append(row["Key"])
            self.numbers.append(row["Number"])
  def readImage(self, imageToRead):
    ImageConvertor.seek(in_file = imageToRead)
  def writeImage(self, imageToPass):
    ImageConvertor.hide(in_file = imageToPass)
  def verschluesseln(self, string, key):
    i = 0
    result = ""
    while i < len(string):
      e = 0
      if str(string[i]) != "\n":
        while str(string[i]) != self.keys[e]:
          e = e + 1
        a = int(self.numbers[e])
        b = key
        c = str(math.sqrt(((a * a) + (b * b))))
        result = result + str(c) + " "
      if str(string[i]) == "\n":
        result = result + "\n" + " "
      i = i + 1
    return result
  def entschluesseln(self, string, key):
    numbers = string.split(" ")
    numbers = numbers[0:len(numbers) - 1]
    result = ""
    for elements in numbers:
      if elements != "\n":
        a = math.ceil(math.sqrt(((float(elements) * float(elements)) - (key * key))))
        e = 0
        while True:
          if int(a) == int(self.numbers[e]):
            break
          if int(a + 1) == int(self.numbers[e]):
            break
          if int(a - 1) == int(self.numbers[e]):
            break
          e = e + 1
        result += str(self.keys[e])
      if elements == "\n":
        result += "\n"
    return result
  def generateKey(self):
    return randint(100, 999)
