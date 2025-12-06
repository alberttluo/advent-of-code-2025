/*
* day1_test.sv: A testbench for the day1 module.
*
* Author: Albert Luo (albertlu at cmu dot edu)
*/

module day1_test();
  logic clock, reset;
  rotDir_t direction;
  logic [31:0] clicks;
  logic [31:0] password;

  day1 DUT(.*);

  initial begin
    clock = 0;
    reset = 1;
    #20;
    reset = 0;
    forever #10 clock = ~clock;
  end

  int inputFD;
  byte inputDir;
  logic [31:0] inputClicks;

  initial begin
    $monitor("direction: %s   clicks: %d   password: %d\n",
                     direction.name, clicks, password);

    `ifdef SMALL_TEST
    inputFD = $fopen("../../inputs/day1_smallinput.txt", "r");
    `else
    inputFD = $fopen("../../inputs/day1_input.txt", "r");
    `endif

    if (inputFD == 0) begin
      $fatal("Failed to open input file.");
    end

    while ($fscanf(inputFD, "%c%d\n", inputDir, inputClicks) == 2) begin
      direction <= (inputDir == "L") ? LEFT : RIGHT;
      clicks <= inputClicks;
      @(posedge clock);
    end

    $display("Final password is %d.", password);

    $fclose(inputFD);
    $finish;
  end
endmodule : day1_test
