import os
import sys
import time

class Stepper_Motor:

  gpio_pins = (204,205,236,237)
  gpio_clockwise_cycle = (1,4,3,2)
  gpio_counterclockwise_cycle = (2,3,4,1)

  def __init__(self):
    self.init_pin()
    self.set_all(False)
    print 'GPIO Initialized'
    return

  def enable_pin_output(self,pin):
    # sudo sh -c 'echo 1 > /sys/class/gpio/export'
    enable_command = 'sudo sh -c \'echo ' + str(pin) + ' > /sys/class/gpio/export\'' 
    # sudo sh - c 'echo out > /sys/class/gpio/gpio1/direction'
    set_out_command = 'sudo sh -c \'echo out > /sys/class/gpio/gpio' + str(pin) + '/direction\''
    os.system(enable_command)
    os.system(set_out_command)
    return

  def set_pin(self,state,pin):
    # sudo sh -c 'echo 1 > /sys/class/gpio/1/value'
    # set_pin_command = 'sudo sh -c \'echo ' + str(state) + ' > /sys/class/gpio/gpio' + str(pin) + '/value\''
    set_pin_command = 'echo ' + str(state) + ' > /sys/class/gpio/gpio' + str(pin) + '/value'
    os.system(set_pin_command)

  def init_pin(self):
    # enable all pins
    for pin in self.gpio_pins:
      self.enable_pin_output(pin)

  def set_all(self,state):
    for pin in self.gpio_pins:
      self.set_pin(state and 1 or 0,pin);

  def run(self,speed,run_time):
    sleep_time = 0.0001
    start_time = time.time()
    while True:
      self.set_pin(1,204) 
      self.set_pin(0,205) 
      self.set_pin(0,236) 
      self.set_pin(0,237) 
      time.sleep(sleep_time)
      self.set_pin(0,204) 
      self.set_pin(0,205) 
      self.set_pin(0,236) 
      self.set_pin(1,237) 
      time.sleep(sleep_time)
      self.set_pin(0,204) 
      self.set_pin(0,205) 
      self.set_pin(1,236) 
      self.set_pin(0,237) 
      time.sleep(sleep_time)
      self.set_pin(0,204) 
      self.set_pin(1,205) 
      self.set_pin(0,236) 
      self.set_pin(0,237) 
      time.sleep(sleep_time)
    self.set_all(False)

stepper_motor = Stepper_Motor()
print 'Input speed and time:'
speed,run_time = map(float,raw_input().split())
stepper_motor.run(speed,run_time)
