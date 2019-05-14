# Docker image to use GPIO

In order to make use of additional hardware and add-on boards you will need to access the GPIO pins. 
These require an additional flag at runtime of `--privileged` to allow the container to write to the special area of memory managing GPIO.

The standard RPi.GPIO library will work through Docker including the libraries from several hardware manufactures.

In directory `gpio-base` there is the Docker base image


### Build the base image

`docker build -t gpio-base .`

### Build blinking image

Script `app.py` is used to blink an LED connected to GPIO pin 18.

![schema](https://blog.alexellis.io/content/images/2016/08/Screen-Shot-2016-08-20-at-09-40-46-1.png "schema")

Just use ADD to transfer the script into a new image depriving from `gpio-base` and build main `Dockerfile`

`docker build -t blink .`

`docker run -ti --privileged blink`

For more on interacting with GPIO head over to the Raspberry Pi Foundation's [Getting Started](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/)  with Physical Computing worksheet.
