module ALU_32_Bit(output [31:0]Result, input [31:0]A, [31:0]B, [2:0]Opcode);
  wire [31:0]operationResults[7:0]; 
   
   assign operationResults[0] = A & B; 
   assign operationResults[1] = A | B;
   assign operationResults[2] = A + B;
   assign operationResults[4] = A & ~B;  
   assign operationResults[5] = A | ~B; 
   assign operationResults[6] = (A +  32'h00000001) + ~B;
   assign operationResults[7] = {31'b0000,(operationResults[6][31])};
   
   assign Result = operationResults[Opcode];
endmodule

