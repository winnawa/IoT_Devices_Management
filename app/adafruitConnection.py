import sys
from Adafruit_IO import MQTTClient

from app.socketConnection import socketio
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_aKfh23TyHDCoGJinXvAsTCi62LVp'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'namkhoapham'
mqttClient = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for DemoFeed changes...')
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('smart-home.temp')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    socketio.emit('new_temp', {'message': payload})

    # if payload > "30" and db.Fan.find({})[0]["status"] == "off":
    #     print('heat hight')
    #     requests.post('https://io.adafruit.com/api/v2/lnminhthu1505/feeds/smart-home.fan/data', data = {"value":"1"}, headers = {"X-AIO-Key": "aio_teLx19UtogwB52wolFfreAFt5UVd"})
        
    #     updateFan("on")

    #     socketio.emit('turn_fan_on', {'message': payload})

# Setup the callback functions defined above.
mqttClient.on_connect    = connected
mqttClient.on_disconnect = disconnected
mqttClient.on_message    = message

# Connect to the Adafruit IO server.
mqttClient.connect()

mqttClient.loop_background()
# Now send new values every 10 seconds.
print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
# while True:
#     value = random.randint(0, 100)
#     print('Publishing {0} to DemoFeed.'.format(value))
#     # client.publish('DemoFeed', value)
#     time.sleep(10)