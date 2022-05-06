// Code your testbench here
// or browse Examples

module full_adder_tb;
  reg x,y,ci;
  wire w1,w2,w3;
  
  full_adder fal(x,y,ci,co,s);
  
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1);
    
    x=0;y=0;ci=0;
    #10 x=0;y=0;ci=1;
    #10 x=0;y=1;ci=0;
    #10 x=0;y=1;ci=1;
    #10 x=1;y=0;ci=0;
    #10 x=1;y=0;ci=1;
    #10 x=1;y=1;ci=0;
    #10 x=1;y=1;ci=1;
    
  end
  initial #80 $finish;
endmodule

// Code your design here


module half_adder(x,y,c,s);
  input x,y;
  output c,s;
  
  xor xor1(s,x,y);
  and and1(c,x,y);
endmodule

module full_adder(x,y,ci,co,s);
  input x,y,ci;
  output co,s;
  wire w1,w2,w3;
  half_adder ha1(x,y,w1,w2);
  half_adder ha2(w2,ci,w3,s);
  or or1(co,w1,w3);
  
endmodule
