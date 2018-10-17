module RegisterFile32w5( input writeEnable,  clk, [31:0] data, [4:0] writeAddress, [4:0] readDataAddress, output [31:0]readData );
    reg [31:0]emory[31:0]; 
    integer i; 
    
    assign readData = emory[readDataAddress];
    initial begin
        for(i = 0; i < 32; i = i + 1) begin 
            emory[i] = 32'b0; 
        end 
    end 
    
    always @(posedge clk) begin 
        if(writeEnable) begin
            emory[writeAddress] <= data; 
        end
    end 
 
     
endmodule