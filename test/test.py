# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

prbs_size=31 #size of the lsfr
#fill two list with 0's
PRBSN=[0]*prbs_size
PRBSO=[0]*prbs_size
#will not work if all the FFs are set to zero.
#set highest register to 1
PRBSO[prbs_size-1]=1
#set number of clock cycles to test. 
n_clock=10000
#set output lists to 1
out=[1]*(n_clock) #list containing the number 1 n_clock number of times. 
# Run throughthe simulation to create the idealized output 
for i in range(n_clock):
  #input the feedback
  PRBSN[0]=PRBSO[27]^PRBSO[30]
  #shift the vlaues
  for j in range(prbs_size-1):
    count=prbs_size-j-1
    PRBSN[count]=PRBSO[count-1]
  #update the array
  for j in range(len(PRBSN)):
    PRBSO[j]=PRBSN[j]
#take the output from the right most FF
out[i]=PRBSN[prbs_size-1]
#start the test
@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    #set the clock period to the 10us(100khhz)
    clock = Clock(dut.clk, 10, units="us")
    #start the clock
cocotb.start_soon(clock.start())
#run through reset sequence. start low,high, low. test start when reset goes low. 
dut._log.info("Reset")
#set inputs for enable, ui_in and uio_in
dut.ena.value=1
dut.ui_in.value=0
dut.uio_in.value=0
#set reset to 0
dut.rst_n.value=0
#wait 5 clock cycles
await ClockCycles(dut.clk, 5)
#set reset to 1
dut.rst_n.value=1
#test begin here
dut._log.info("Test project behavior")
#Compare output to theory for each clock cycle 
for i in range(0,n_clock):
    #wait one clock cycle to see output values 
    await ClockCycles(dut.clk, 1)
#The following assertion is a example of how to check output values.
#test (assert) that we are getting the expected output. 
assert dut.uo_out[0].value == out[i]


