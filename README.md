# Python Cryptographie

## Table of contents

* [Installation](##Installation)
* [Usage](##Usage)
  * [Encrypt](###Encrypt)
  * [Decrypt](###Decrypt)
* [Technic](##Technic)
* [Competition](##Competition)

## Installation

This program can be run on any version of Python 3.

As Libarys you have to install:
* ``` os ```
* ``` shutil ```
* ``` opencv ```
* ``` PySimpleGUI ```
* ``` pillow ```
* ``` bitarray ```
* ``` random ```
* ``` csv ```
* ``` math ```

To use the programm you have to run the ```GenerateNumbers.csv``` file, to generate the numbers and key table. This file the must be shared with all users you want to send messages to.

## Usage

### Encrypt

First select an image (Only ```.png```) by pressing the ```Choose Image``` button on the left side. Then enter your text to the textfield below. Then press the ```Convert``` button. Then you can save the image by clicking the ```Save``` button. Also copy the ```key```and send it with the image.

### Decrypt

First enter the ```key``` send with the image to the textfield at the top right. Then click the ```Choose Image``` button and select your image. Now click the ```Convert``` button and the message appears in the textfield.

## Technic

### Encrypting

First every letter of the message gets converted to a number. Then every number gets charged with the key. All results get converted to binary. Then at every chrominance in every pixel in the image the last bit gets replaced by one bit of the message.

### Decrypting

First at every chrominance in every pixel in the image the last bit gets read and added together to a string. Then the strings get split into numbers which get charged with the key. The new numbers get back converted to letters.

## Competition

This program was original developed for the "Data security" competition of [Explore Science](http://explore-science.info) 2022 in Mannheim.

With this project, we earned the 1. place.