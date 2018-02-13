/*
 * File:   Main.c
 * Author: Michael Emperador
 *
 * Created on October 18, 2017, 9:11 PM
 */
// PIC16F1829 Configuration Bit Settings
// 'C' source line config statements
#include <xc.h>
#include <stdio.h>
#include <stdlib.h>

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.
// CONFIG1
#pragma config FOSC = INTOSC // Oscillator Selection (INTOSCoscillator: I/O function on CLKIN pin)
#pragma config WDTE = OFF // Watchdog Timer Enable (WDT disabled)
#pragma config PWRTE = OFF // Power-up Timer Enable (PWRT disabled)
#pragma config MCLRE = ON // MCLR Pin Function Select (MCLR/VPP pinfunction is MCLR)
#pragma config CP = OFF // Flash Program Memory Code Protection(Program memory code protection is disabled)
#pragma config CPD = OFF // Data Memory Code Protection (Datamemory code protection is disabled)
#pragma config BOREN = OFF // Brown-out Reset Enable (Brown-out Resetdisabled)
#pragma config CLKOUTEN = OFF // Clock Out Enable (CLKOUT function isdisabled. I/O or oscillator function on the CLKOUT pin)
#pragma config IESO = OFF // Internal/External Switchover(Internal/External Switchover mode is disabled)
#pragma config FCMEN = OFF // Fail-Safe Clock Monitor Enable (FailSafeClock Monitor is disabled)
// CONFIG2
#pragma config WRT = OFF // Flash Memory Self-Write Protection(Write protection off)
#pragma config PLLEN = OFF // PLL Enable (4x PLL disabled)
#pragma config STVREN = ON // Stack Overflow/Underflow Reset Enable(Stack Overflow or Underflow will cause a Reset)
#pragma config BORV = LO // Brown-out Reset Voltage Selection(Brown-out Reset Voltage (Vbor), low trip point selected.)
#pragma config LVP = OFF // Low-Voltage Programming Enable (Highvoltageon MCLR/VPP must be used for programming)

#define BAUD 9600
#define FOSC 4000000L
#define NINE_BITS 0
#define SPEED 0x4
#define _XTAL_FREQ 4000000.0 /*for 4mhz*/
#define RX_PIN TRISC5
#define TX_PIN TRISC4
#define DIVIDER ((int)(FOSC/(16UL * BAUD) -1)) // Should be 25 for9600/4MhZ

/* 
 * Primary Goal:
 * Create a self-sustaining pendulum. 
 * 
 * Secondary Goal:
 * To create different modes of use. 
 * 
 * Modules used:
 * A2D conversion
 * TMR0 
 * GPIO PINS
 * INTERRUPTS {INTCON,IOCBN}
 * EUSART
 * BJT terminal 
 * 
 * External Hardware used:
 * Photo-resistor 
 * Solenoid 
 * Relay
 * 
 * Output Pins:
 * RA5 - light for user feedback 
 * RB4 - powers external LED that indicates when solenoid should be fired. 
 * RB6 - powers bjt terminal 
 * 
 * Input Pins: 
 * RA0 - Analog input for photo-resistor set up. 
 * RA4 - calls while_game() function when grounded
 * RB5 - fires solenoid when RA4 is grounded, resets light_compare values when RA4 is high
 * RB7 - puts program in hold state
 *
 * EUSART pins:
 * RC5 - Rx pin
 * RC4 - Tx pin
 */

/*Prototypes*/
unsigned char ReadSensor(unsigned ch);
void configure_pins_modules(void);
unsigned int value_config(unsigned ch); 
void feedback_loop(int number_of_blinks, int delay_length); // Provides custom feedbacks to assist with debugging and user experience
void pinConfig(void);
void interrupt solenoid_limiter();
void while_function(unsigned int  current_a2d_value ,int control_compare);
void fire_solenoid();
void while_game(unsigned int  current_a2d_value ,int control_compare);

/*USART Prototypes*/
void setup_comms(void);
void putch(unsigned char);
unsigned char getch(void);
unsigned char getche(void);

// Global Variables
unsigned  int light_avg_value; // an average of ten light reads before startup 
unsigned int light_compare;
int solenoid_control = 0; 

void main(void) {
    configure_pins_modules();
    unsigned int  current_a2d_value ;
    int control_compare = 0; 
            ADCON1 = 0X10; 
     setup_comms(); // set up the USART - settings defined in usart.h
    
    while(1) {
	    if(!RA4) {
	        while_game(current_a2d_value,control_compare);
	    } 
	     while_function(current_a2d_value,control_compare);
	    if(!RB7){
	        while(!RB7) {
	            feedback_loop(1,10);
	        }
	    }
	}
    return;
}

/* 
 *@function() while_function(unsigned int, unsigned int) manual mode for solenoid relies on 
 * interrupt upon push of RB5 for activation of RB6.
 *@param current_a2d_value value from current a2d reading returned from value_config(0)
 *@param control_compare control variable that determines when default set value is enacted.
 */
void while_function(unsigned int  current_a2d_value ,int control_compare) {
    RA5 = 0; 
    
        light_compare = value_config(0);

    while(RB7 && RA4) {
        /* 
         * The following code will test whether the photo resistor value of 
         * un-obstructed light vs the value with the object obstructing. 
         * The a2d value should be less un-obstructed because of a 
         * higher resistance.
         */
        current_a2d_value = value_config(0);
        
        
        printf("current value is %d | base value is %d \n\r",
                current_a2d_value, light_compare);
        if( (light_compare - current_a2d_value) > 5  ) {
            
            current_a2d_value = value_config(0); 
            
            if(current_a2d_value < light_compare) {
                RB4 = 1; 
                if(solenoid_control > 6) {
                    RB6 = 1; // Activation of solenoid
                    solenoid_control = 0 ; 
                }
                __delay_ms(70);
                RB6 = 0;
                __delay_ms(15);
                RB4 = 0; 
            }
        }
    } 
    return;
}

/* @function() while_game(unsigned int, unsigned int) manual mode for solenoid relies on 
 * interrupt upon push of RB5 for activation of RB6.
 *@param current_a2d_value value from current a2d reading returned from value_config(0)
 *@param control_compare control variable that determines when default set value is enacted.
*/
void while_game(unsigned int  current_a2d_value ,int control_compare) {
    RA5 = 1; 
    printf("WELCOME TO GAME \n\r");
    while(RB7 && !RA4) {
        /* 
         * The following code will test whether the photo resistor value of 
         * un-obstructed light vs the value with the object obstructing. 
         * The a2d value should be less un-obstructed because of a 
         * higher resistance.
         */
        current_a2d_value = value_config(0);
        

        printf("current value is %d | base value is %d \n\r",
                current_a2d_value, light_compare);
        if( (light_compare - current_a2d_value) > 4  ) {
            
            current_a2d_value = value_config(0); 

            if(current_a2d_value < light_compare) {
                RB4 = 1; 
                RB4 = 0; 
            }
        }
    } 
        while_function(current_a2d_value , control_compare);
        RA5 = 0;
    return;
}

/*
 * @function startup_config() - takes in an array and populates it with values to be 
 * used as a baseline comparison.
 * @return Integer: Returns the average of the a2d values recorded.
 * @param startup_values[] - array passed in to be used as base a2d value to 
 * be compared with.
 */
unsigned int value_config(unsigned ch) {
    ADCON0 = 0x00; 
    ADCON0 = (ch << 2);
    unsigned int light_value;
    for(int i= 30; i >= 0; i--) {
        ADON = 1;
        for(int d = 0; d < 5; d++)
            ADGO = 1; 
        while(ADGO){continue;}
          light_value += ((ADRESH << 8) + (ADRESL));
    }  
    light_avg_value = light_value; 
    light_value = 0 ; 
    return light_avg_value / 2000  ; 
}

/* 
 *@function solenoid_limiter() Interrupt service routine that increments the 
 * solenoid_control varibale to control solenoid fireing frequency as well as 
 * control the function of RB5 button.
 */
void interrupt solenoid_limiter() {
        solenoid_control++; 
    TMR0IF = 0 ;
    if(!RB5 && RA4) { // setting up for multi-function
            light_compare = value_config(0);
            RB4 = 0; 
        while(!RB5) {
            continue;
        }
    }
    if(!RB5 && !RA4) {
        fire_solenoid();
    }
    return; 
}

/*
 *@function fire_solenoid() sets RB6 to high while button is pressed in game mode. 
 */
void fire_solenoid() {
    RB6 = 1; 
    while(!RB5){ 
        continue;
    }
    RB6 = 0;
    return;
}

/*
 * @funtion ReadSensor()
 * @param ch number of the channel in hex
 * @return returns unsigned value from a2d conversion 
 */
unsigned char ReadSensor(unsigned ch) {
    ADCON0 = 0x00; 
    ADCON0 = (ch << 2);
    ADON = 1;
    
    for(int i = 0; i < 5; i++)
        ADGO = 1; 
    while(ADGO){continue;}
    ADON = 0;
    return (ADRESH << 8) + (ADRESL);
}

/*
 * @function feedback_loop() - hosts feedback light routine.
 *           Minimum delay of 30 milliseconds.
 * @return void 
 * @param number_of_blinks integer determines how many times the light will blink. 
 * @param delay_length integer determines the multiplier of the base delay of 10 milliseconds. 
 */
void feedback_loop(int number_of_blinks, int delay_length) { 
    for(int i = 0; i <= number_of_blinks; i++) {
        RA5 = 1; 
        for(int d = delay_length; d >=0; d--) {
        __delay_ms(10); 
        }
        RA5 = 0;
        for(int d = delay_length; d >=0; d--) {
        __delay_ms(10); 
        }
    }
    return;
}


/*
 * @function configure_pins_modules() - configures pins and modules 
 * @return void 
 */
void configure_pins_modules(void) {
       // Initialization of Necessary Pins 
    TRISA = 0X11; //sets Ra5 as output and Ra0 as an input
    ANSELA = 0X01; // Ra0 as an analog input
    TRISB = 0XA0; // Sets RB5 and RB7 as input//0X20; // Sets RB5 as input
    ANSELB = 0X00;
    OSCCON = 0x6A; /* b6..4 = 1101 = 4MHz */
    TXCKSEL = 1; // both bits in APFCON0 MUST BE 1 for 1829 0 for 1825
    RXDTSEL = 1; /* makes RC4 & 5 TX & RX for USART (Allows ICSP)*/
    TRISC = 0x24; /* RC4, RC5, RC7 set as input */
    ANSELC =0x24; /* all ADC pins to digital I/O */
    //Interrupt config
    INTCON = 0XA0;
    OPTION_REG = 0X07; 
    IOCBN = 0X20;
    return;
}

/*
 *@function setup_comms() sets up pins and registers for USART
 */
void setup_comms(void) {
    RX_PIN = 1;
    TX_PIN = 1;
    SPBRG = DIVIDER;
    RCSTA = (NINE_BITS | 0x90);
    TXSTA = (SPEED | NINE_BITS | 0x20);
    TXEN = 1;
    SYNC = 0;
    SPEN = 1;
    BRGH = 1;
}


void putch(unsigned char byte) {
    /* output one byte */
    while(!TXIF) /* set when register is empty */
    continue;
    TXREG = byte;
}

unsigned char getch() {
    /* retrieve one byte */
    while(!RCIF) /* set when register is not empty */
    continue;
return RCREG;
}

unsigned char getche(void) {
    unsigned char c;
    putch(c = getch());
return c;
}