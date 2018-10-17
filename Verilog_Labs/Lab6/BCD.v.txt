module BCD_Converter(input [11:0]BCD, output [11:0]Binary);
assign Binary = (BCD[7:4]<<1) + (BCD[7:4]<<3) +  BCD[3:0] + (BCD[11:8]<<6) + (BCD[11:8]<<5) + (BCD[11:8]<<2);
endmodule