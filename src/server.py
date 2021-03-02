import RPi.GPIO as gpio


from flask import Flask
app =Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world!'

@app.route('/turn_on_lights')
def turn_on_lights():
    gpio.output(17, gpio.HIGH) 
    return 'on'

@app.route('/turn_off_lights')
def turn_off_lights():
    gpio.output(17, gpio.LOW) 
    return 'off'

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

app.run('0.0.0.0')
