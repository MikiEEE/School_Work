module RegisterFile32w5_tb();

reg [4:0] writeAddress1; 
reg [4:0] readDataAddress1; 
reg clock; 
reg writeEnable1; 
reg [31:0] data1; 
wire [31:0] readData1; 
integer i; 
//module RegisterFile32w5( input writeEnable, clk, [31:0] data, [4:0] writeAddress, [4:0] readDataAddress,output [31:0]readData, );
RegisterFile32w5 emoryBlock( writeEnable1, clock, data1,writeAddress1,readDataAddress1,readData1 );
initial begin 
    clock = 1'b0; 
    writeEnable1 = 1'b1; 
    writeAddress1 = 5'b0; 
    readDataAddress1 = 5'b0;
    data1 = 32'b0;
    for(i = 0; i < 32; i = i + 1) begin 
        clock = 1'b1; 
        data1 = i;
        #5;
        clock = 1'b0; 
        writeEnable1 = writeAddress1 + 1'b1; 
        #5;
    end
end 
endmodule