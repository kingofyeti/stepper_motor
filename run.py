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
    set_pin_command = 'sudo sh -c \'echo ' + str(state) + ' > /sys/class/gpio/gpio' + str(pin) + '/value\''
    os.system(set_pin_command)

  def init_pin(self):
    # enable all pins
    for pin in gpio_pins:
      self.enable_pin_output(pin)

  def set_all(self,state):
    for pin in gpio_pins:
      set_pin(state and 1 or 0,pin);

  def run(self,speed,run_time):
    sleep_time = (float) 1/ speed
    start_time = time.time()
    while (time.time()-start_time ) < run_time:
      for i,pin in enumerate(gpio_pins):
        state = (i+1) == gpio_clockwise_cycle and 1 or 0 
        self.set_pin(state,pin) 
      time.sleep(sleep_time)
    self.set_all(False)

stepper_motor = Stepper_motor()
stepper_motor.run(100,50)
