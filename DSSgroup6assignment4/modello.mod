set FATTORIA;
set SILOS;

param costoTrasporto;
param days;

param Dist{SILOS, FATTORIA};

param d{FATTORIA};
param q_t{SILOS};

param m{SILOS};
param cf{SILOS};

param C{i in SILOS, j in FATTORIA}:= costoTrasporto*2*Dist[i,j]*d[j] + m[i]*d[j];
param f{i in SILOS}:= cf[i]/days;

var x{SILOS, FATTORIA}, >=0 ;
var y{SILOS}, binary ;

minimize obj_funct: sum{i in SILOS, j in FATTORIA} C[i,j]*x[i,j] + sum{i in SILOS} f[i]*y[i];
s.t. constraint1{j in FATTORIA}: sum{i in SILOS} x[i,j] = 1;
s.t. constraint2{i in SILOS}: sum{j in FATTORIA} d[j]*x[i,j] <= q_t[i]*y[i];


