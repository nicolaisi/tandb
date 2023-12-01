### 01.12.2023

- nucleo-l053r8 has 8k RAM and initial loading of FreeRTOS using CMSISv2 used up all the RAM, with one task created.
- Maybe this MCU with only 8k RAM should be done in bare-metal approach!! super-loop approach!!
- I don't think we can go crazy with the test, it surely will be slower...
- Maybe use mutex in super-loop
- Next step is to either continue super-loop development, or use a larger board and proceed with RTOS approach!! 
