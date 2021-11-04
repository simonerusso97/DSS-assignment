var XB;
var XC;
maximize Profit: 25 * XB + 30 * XC;
subject to Time: (1/200) * XB + (1/400) * XC;
subject to B_limit: 0 <= XB <= 4000;
subject to C_limit: 0 <= XC <= 6000;