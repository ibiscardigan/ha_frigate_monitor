'''
Stand alone python app for displaying the state of a frigate instance in
regards to its up/down state and its primary secondary state with other
frigate instances
'''

import time
from periphery import GPIO

# Define GPIO chip and pins
GPIO_CHIP = "/dev/gpiochip1"
GREEN_PIN_1 = 63  # Physical Pin 29
RED_PIN_1 = 64  # Physical Pin 31
GREEN_PIN_2 = 65  # Physical Pin 33
RED_PIN_2 = 67  # Physical Pin 37

# Initialize GPIOs
try:
    print(f"Setting up GPIO {GREEN_PIN_1} to always be ON...")
    always_on_led = GPIO(GPIO_CHIP, GREEN_PIN_1, "out")
    always_on_led.write(True)  # Keep this LED ON

    print(f"Setting up GPIO {RED_PIN_1} to blink every 10 seconds...")
    blinking_led = GPIO(GPIO_CHIP, RED_PIN_1, "out")

    while True:
        # Blink the second LED
        print(f"Turning ON GPIO {RED_PIN_1}")
        blinking_led.write(True)
        time.sleep(0.25)  # ON for 1 second

        print(f"Turning OFF GPIO {RED_PIN_1}")
        blinking_led.write(False)
        time.sleep(9.75)  # OFF for 9 seconds

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    always_on_led.write(False)  # Turn off before exit
    blinking_led.write(False)
    always_on_led.close()
    blinking_led.close()
    print("GPIO cleanup complete.")

except Exception as e:  # pylint: disable=broad-exception-caught
    print(f"Error: {e}")
