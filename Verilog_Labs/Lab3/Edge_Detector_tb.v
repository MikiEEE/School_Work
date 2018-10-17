`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/18/2018 06:49:15 PM
// Design Name: 
// Module Name: edge_detector_tb
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


module edge_detector_tb();
//parameter number_Inidice = 0; 
reg clock;
reg edg; 
//reg [31:0] number; 
wire Falling, Rising;
edge_detector edg1(.signal(edg), .clock(clock),.risingEdge(Rising), .fallingEdge(Falling));

initial begin
    clock = 1'b0;
    edg = 1'b0; 
   // number = 32'hA19BFC79; 
end

always  begin
    #20 clock  =  !clock;   
end
always begin
     #100 edg = !edg;
 end
endmodule







