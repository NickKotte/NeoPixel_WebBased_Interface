import time
from neopixel import *



class led:
	
	def __init__(self):
		# LED strip configuration:
		self.LED_COUNT      = 300     # Number of LED pixels.
		self.LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
		#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
		self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
		self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
		self.LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
		self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
		self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
		
		self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
		self.strip.begin()

	def showSolidColor(self, color, ms):
		for i in range(self.LED_COUNT):
			self.strip.setPixelColor(i, color)
			self.strip.show()
			time.sleep(ms/1000.0)
