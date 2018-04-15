import time
import RPi.GPIO as GPIO
import subprocess
import os

GPIO.setmode(GPIO.BCM)

class StepperMotor:
	def __init__(self, in1, in2, in3, in4):
		self.p1 = in1
		self.p2 = in2
		self.p3 = in3
		self.p4 = in4
		self.delay = 0.004
		GPIO.setup(in1, GPIO.OUT)
		GPIO.setup(in2, GPIO.OUT)
		GPIO.setup(in3, GPIO.OUT)
		GPIO.setup(in4, GPIO.OUT)
	def stepForward(self):
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
	def stepBackward(self):
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
	def goBackwards(self, steps=1):
		for i in range(steps):
			self.stepForward()
		self.off()
	def goForward(self, steps=1):
		for i in range(steps):
			self.stepBackward()
		self.off()
	def off(self):
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)


os.system('python3 /home/pi/pywu/pywu/pywu.py fetch bbd2a2857e76b82b pws:IMADRID321')
p = subprocess.Popen("python3 /home/pi/pywu/pywu/pywu.py current temp_c", stdout=subprocess.PIPE, shell=True)
output_p = p.communicate()[0]
temp = int(output_p)

q = subprocess.Popen("cat /home/pi/.pos", stdout=subprocess.PIPE, shell=True)
output_q = q.communicate()[0]
pos = int(output_q)

pos_requerida = -13.0*(temp-25)/3.
pos_requerida = int(pos_requerida)
pos_requerida = max(0, min(130, pos_requerida))

mov = pos_requerida - pos



motor = StepperMotor(5,6,13,26)
# Avanza 100 pasos a la derecha
# motor.goForward(10)
# Retrocede 150 pasos
# motor.goBackwards(10)
# Limpiamos puertos

if mov < 0:
    motor.goBackwards(-mov)
elif mov > 0:
    motor.goForward(mov)
else:
    pass

with open("/home/pi/.pos", "w") as archivo:
    archivo.write("{}".format(pos_requerida))

GPIO.cleanup()
