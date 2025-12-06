/*
* day1.sv: Given some input (rotation direction and amount of clicks), count the
* number of times the dial is left pointing at 0, to unlock the secret entrance
* to the North Pole. Part 2 of the challenge is to count the number of times
* 0 is passed in total. Note that the dial is initially pointing at 50.
*
* Author: Albert Luo (albertlu at cmu dot edu)
*/

typedef enum logic {
  LEFT,
  RIGHT
} rotDir_t;

module day1
  (input  logic        clock, reset,
   input  rotDir_t     direction,
   input  logic [31:0] clicks,
   output logic [31:0] password);

  localparam logic [7:0] MODULO = 8'd100;

  // Register to keep track of number the dial is pointing at, currently.
  logic [7:0] currNum_reg;

  // Clicks modulo 100.
  logic [7:0] clicksMod100;

  // The next numbers in either direction, given clicks.
  logic [8:0] rawRightRotNum;
  logic [7:0] rightRotNum;
  logic [8:0] rawLeftRotNum;
  logic [7:0] leftRotNum;

  // The next number the dial will point at.
  logic [7:0] nextNum;

  always_ff @(posedge clock, posedge reset) begin
    if (reset) begin
      currNum_reg <= 8'd50;
      password <= 32'd0;
    end
    else begin
      currNum_reg <= nextNum;
      password <= password + ((currNum_reg == 32'd0) ? 32'd1 : 32'd0);
    end
  end

  // Adder/subtracter to perform the rotation, which we mux out based on the
  // input direction.
  always_comb begin
    clicksMod100 = (clicks[7:0] > MODULO) ? (clicks[7:0] - MODULO) : clicks[7:0];

    // Raw rotation (non-circular).
    rawRightRotNum = currNum_reg + clicksMod100;
    rawLeftRotNum = currNum_reg - clicksMod100;

    // Perform modulo via subtraction.
    rightRotNum = (rawRightRotNum >= MODULO) ? (rawRightRotNum[7:0] - MODULO) :
                                               rawRightRotNum[7:0];

    // If top bit is set, then negative, so we convert it back to positive and
    // subtract it from the modulo.
    leftRotNum = (rawLeftRotNum[7]) ? (MODULO - (~(rawLeftRotNum) + 8'd1)) :
                                       rawLeftRotNum;

    // Select either left or right based on the direction given.
    nextNum = (direction == LEFT) ? leftRotNum[7:0] : rightRotNum;
  end
endmodule : day1
