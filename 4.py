import time
import math

def delayed_sqrt(number, delay_ms):
    # Convert milliseconds to seconds
    delay_seconds = delay_ms / 1000.0
    time.sleep(delay_seconds)  # Introduce a delay
    result = math.sqrt(number)  # Calculate the square root
    return result

# Example usage
number = 25100
delay_ms = 2123

sqrt_result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")
