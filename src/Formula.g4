grammar Formula;

fragment LOWER          : [a-z];
fragment UPPER          : [A-Z];
fragment LETTER         : LOWER | UPPER;
fragment DIGIT          : [0-9];
fragment ANYCHAR        : LETTER | DIGIT | '_';

LOWER_NAME              : LOWER ANYCHAR*;
OP_AND                  : '&' | '&&' | 'v' | '.';
OP_OR                   : '|' | '^' | '+';
MODAL_OP                : 'Op';
NEG                     : '-' | '!' | '¬';

WS                      : [ \n\t\r]+ -> skip;

formula
    : LOWER_NAME              # atom
    | formula OP_AND formula  # conjunction
    | formula OP_OR formula   # disjunction
    | '(' formula ')'         # parens
    | '-(' formula ')'        # negation
    | '¬(' formula ')'        # negation
    | '!(' formula ')'        # negation
    | 'Op' formula '(' formula ')'       # modal_operator
    | 'Box(' formula ')'      # modal_operator
    | 'B(' formula ')'        # modal_operator
    ;


