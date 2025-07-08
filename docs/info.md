## How it works
The chip generates a PRBS31 signal using a Fibonacci LFSR and analyzes it with the same structure. The output of the PRBS is taken off the chip and read back in to be analyzed.  
The PRBS generator is based on a 31-bit linear shift register with the feedback coming from registers 30 and 27.
Everything will be documented here:https://docs.google.com/document/d/1nhcHBQsxXUUo1_4WGjxFoWHzpVBCy18a5GQimM9eUtQ/edit?usp=sharing
co-lab code: https://colab.research.google.com/drive/1uSGfoFdt0cDL9Ya7yrQQEXQ4FVlEGef5?usp=drive_link
## How to test
Input Clock and reset (Low high, then low)
Take the output out of port io_out[0] and feed it back into the chip (after transmitting it if you like.) iio_out[1] will be zero after 31 clock cycles  if the data is correct.
You can also capture the data and check it against the code at the end of the co-lab code listed above.
## External hardware
ADALM2000
