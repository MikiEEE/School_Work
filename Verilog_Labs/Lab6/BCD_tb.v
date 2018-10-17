
module BCDConverter_tb();
reg [11:0]BCD; 
wire [11:0]Binary;
 BCD_Converter Instance(BCD, Binary);
initial begin 
    BCD = 12'h721;
end 
endmodule