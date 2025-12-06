/*
* modulo.sv: A module for computing modulo N.
*
* Author: Albert Luo (albertlu at cmu dot edu)
*/

typedef enum logic [1:0] {
  MOD_WAIT,
  MOD_COMP,
  MOD_DONE
} modState_t;

module moduloN
  #(parameter int WIDTH = 8,
              int MOD_WIDTH = 8)
  (input  logic [WIDTH - 1:0]     moduloIn,
   input  logic [MOD_WIDTH - 1:0] mod,
   input  logic                   clock, reset, start,
   output logic [WIDTH - 1:0]     modulo);

endmodule : moduloN

module modFSM
  (input  logic clock, reset, start,
   input  logic compDone);

  modState_t currState, nextState;

  always_ff @(posedge clock, posedge reset) begin
    if (reset)
      currState <= MOD_WAIT;
    else
      currState <= nextState;
  end

  always_comb begin
    unique case (currState)
      MOD_WAIT: nextState = (start) ? MOD_COMP : MOD_WAIT;
      MOD_COMP: nextState = (compDone) ? MOD_DONE : MOD_COMP;
      MOD_DONE: nextState = MOD_DONE;
    endcase
  end
endmodule : modFSM
