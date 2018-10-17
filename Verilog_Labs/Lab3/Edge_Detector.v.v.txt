`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/18/2018 06:30:46 PM
// Design Name: 
// Module Name: edge_detector
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module edge_detector(input signal, clock, output risingEdge, fallingEdge);
    wire first_secondD; 
    wire secondDOut; 
    wire thirdDOut; 
    wire clock, signal; 
    
    D_FF firstD(signal, clock,first_secondD);
    D_FF secondD(first_secondD, clock, secondDOut);
    D_FF thirdD(secondDOut, clock, thirdDOut);
    
    assign  risingEdge = !thirdDOut & (secondDOut ^ thirdDOut);
    assign  fallingEdge = thirdDOut & (secondDOut ^ thirdDOut); ;
endmodule



module D_FF(input d, clk, output Q);  
    reg subQ; 
    assign Q = subQ; 
    
    initial begin
        subQ = 0; 
    end
    
    always @ (posedge clk) 
    begin
        subQ <= d;
    end
endmodule






