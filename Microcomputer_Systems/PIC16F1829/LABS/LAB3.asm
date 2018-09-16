ME: Michael Emperador
;LAB 3 BLINK WITH INTERRUPTS

; PIC16F1829 Configuration Bit Settings

; Assembly source line config statements

#include "p16f1829.inc"
#define mask (1 << 5)
;!!DEFINE MASK HERE!!
 
; CONFIG1
; __config 0xC9E4
 __CONFIG _CONFIG1, _FOSC_INTOSC & _WDTE_OFF & _PWRTE_OFF & _MCLRE_ON & _CP_OFF & _CPD_OFF & _BOREN_OFF & _CLKOUTEN_OFF & _IESO_OFF & _FCMEN_OFF
; CONFIG2
; __config 0xDEFF
 __CONFIG _CONFIG2, _WRT_OFF & _PLLEN_OFF & _STVREN_ON & _BORV_LO & _LVP_OFF


 
    list p=16F1829, R=DEC
    


    CBLOCK 0x30 ; Define GPR variable register locations
VarA
VarB
    ENDC
  ORG 0
    goto Start 
    ORG 4  
    banksel INTCON
    btfss INTCON , 2
    Reset 
    BCF INTCON, 2
    banksel LATA
    movlw (0<< 5)
    Banksel PORTB
    btfss PORTB , 5
    movlw  mask
    Banksel LATA
    xorwf LATA, f
    RETFIE
    
    
Start
;Clock Setup
    BANKSEL	OSCCON 	
    movlw   	0x6A   	 	
    movwf  	OSCCON
;Input Output Setup
    ;Configure all of TRISA to be output
    BANKSEL 	TRISA  	 	
    clrf    	TRISA
    ;Set all LATCH A outputs to 0
    BANKSEL	LATA
    clrf	LATA
    ;Configure Push Button as Input
    BANKSEL	TRISB
    bsf		TRISB, 5
    ;Configure Push Input as Digital
    BANKSEL	ANSELB
    bcf		ANSELB, 5
    ;Configure Option Registor for TMR0
    BANKSEL	OPTION_REG
    movlw	0x87
    movwf	OPTION_REG

    
    
    ;Interrupt Control Register Setup

Banksel	INTCON
    bcf INTCON, 2
    bsf	INTCON, 7
    bsf	INTCON, 5
   
end
