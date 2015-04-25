import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
# Test comment
# Test comment 2
# Test comment 3
# Test comment 4
# Test comment 5
# 1x ground + 1x 5v source using orange/blue cable
enable_pin = 18		# no color

# First Stepper motor
coil_A_1_pin = 4	# yellow cable --> violet coil 
coil_A_2_pin = 17	# orange cable --> orange coil
coil_B_1_pin = 23	# orange cable --> blue coil
coil_B_2_pin = 24	# white/violet --> yellow coil

# Second Stepper motor
coil_C_1_pin = 22
coil_C_2_pin = 10
coil_D_1_pin = 18
coil_D_2_pin = 25
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(coil_C_1_pin, GPIO.OUT)
GPIO.setup(coil_C_2_pin, GPIO.OUT)
GPIO.setup(coil_D_1_pin, GPIO.OUT)
GPIO.setup(coil_D_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def forward(delay, steps, stpr): 
	for i in range(0, steps):
		setStep(1, 0, 1, 0,stpr)
		time.sleep(delay)
    		setStep(0, 1, 1, 0,stpr)
    		time.sleep(delay)
    		setStep(0, 1, 0, 1,stpr)
    		time.sleep(delay)
    		setStep(1, 0, 0, 1,stpr)
    		time.sleep(delay)
 
def backwards(delay, steps, stpr):  
  	for i in range(0, steps):
    		setStep(1, 0, 0, 1,stpr)
    		time.sleep(delay)
    		setStep(0, 1, 0, 1,stpr)
    		time.sleep(delay)
    		setStep(0, 1, 1, 0,stpr)
    		time.sleep(delay)
    		setStep(1, 0, 1, 0,stpr)
    		time.sleep(delay)
 
  
def setStep(w1, w2, w3, w4,stpr):
	if stpr == "A":
  		GPIO.output(coil_A_1_pin, w1)
  		GPIO.output(coil_A_2_pin, w2)
  		GPIO.output(coil_B_1_pin, w3)
  		GPIO.output(coil_B_2_pin, w4)
	if stpr == "B":
  		GPIO.output(coil_C_1_pin, w1)
  		GPIO.output(coil_C_2_pin, w2)
  		GPIO.output(coil_D_1_pin, w3)
  		GPIO.output(coil_D_2_pin, w4)
 
while True:
  	delay = raw_input("Delay between steps (milliseconds)?")
  	steps = raw_input("How many steps forward? ")
	stpr = raw_input("Which stepper motor do you want steer? ")
  	forward(int(delay) / 1000.0, int(steps), str(stpr))
  	steps = raw_input("How many steps backwards? ")
  	backwards(int(delay) / 1000.0, int(steps), str(stpr))