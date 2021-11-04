# XPRESS/AMPL changelog

## 20110312
  xpress.c, README.1st, README.xpress:  update to version 7.1.

## 20110325
  xpress.c: omit the "debug" keyword unless compiled with -DRWA_DEBUG .

## 20110419
  xpress.c: fix a bug with quadratic constraints involving some
variables that only appear linearly.

## 20110825
  xpress.c: some bug fixes, e.g., in handling quadratic forms,
supplied by David Nielsen.

## 20110913
  xpress.c: add support for indicator constraints, i.e., logical
constraints of the form
	s.t. foo: b == c ==> constraint1 [else constraint2]
with b a binary variable, c = 0 or 1, and the constraints simple
inequality or equality constraints.  This requires linking with
version >= 20110913 of the AMPL/solver interface library.

## 20111010
 xpress.c: fix a bug in the update of 20110825.

## 20111220
 xpress.c: increase constraint.sstatus array length by one to fix
a possible fault.

## 20111223
 xpress.c: catch SIGINT (control-C) and return the best available
solution.  Quickly giving several control-C's may sometimes lead to
the new solve_result_num value 520 (and no returned solution).
 README.xpress: minor adjustments.

## 20120417
 xpress.c: updates for XPRESS 22.

## 20120605
 xpress.c: add keyword mipstartvalue with synonym mipstart to
control whether a starting guess for a MIP problem is passed
to XPRESS.  Hitherto a starting guess was ignored; now the
default is to use it, but specifying mipstartvalue=0 will cause
it not to be used.  Also arrange for "xpress -v" to report the
version of XPRESS being used.

## 20120731
 xpress.c: updates for XPRESS 23:  new keywords cpuplatform,
preduprow, presolvemaxgrow, symmetry.  The updated driver still
works with XPRESS 22.

## 20121006
  Add keyword "version", to report version details before solving
the problem.

## 20121011
  Updates to README.xpress, makefile.u, makefile.vc and addition
of shell scripts xpress.linux and xpress.macosx.

## 20130129
  Correct the description of "sos2" in the "-=" output.

## 20130312
  Add "network" keyword instructing xpress to identify and exploit
an embedded network.

## 20130419
  Update for version 7.5.  New keywords: baralg, barreg, treepresolve.

## 20130622
  Add keyword "lazy" for recognizing suffix .lazy, with nonzero values
indicating that linear constraints are "lazy" or "delayed" if the
problem has integer variables.
  Add keyword "objrep" controlling whether to replace
	minimize obj: v;
with
	minimize obj: f(x)
when variable v appears linearly in exactly one constraint of the form
	s.t. c: v >= f(x);
or
	s.t. c: v == f(x);
Default is no for the former, yes for the latter.  For more details,
invoke "xpress -=".  This requires use of version >= 20130622 of the
AMPL/solver interface library.

## 20140204
  Update for XPRESS 7.6.  New keywords barcores, miqcpalg, qccuts,
qcrootalg.  See the "xpress -=" output for details.  Tested with
libraries for which "xpress -v" says "AMPL/XPRESS 25.01.05 ...".

## 20140314
  Fix a glitch (possible fault) with objrep.

## 20140618
  When iis appears in $xpress_options and a linear problem is infeasible,
return an IIS in suffix .iis; if changing the bounds on just one
constraint or variable would remove the infeasibility, also return
suffix .iso with value 1 for each such constraint or variable.
  Change calls on Sprintf to simpler, safer calls on Bpf.  Should be
invisible.

## 20140624
  Update for XPRESS 7.7.  New keywords dualthreads, maxmemory,
prebndredcone, prebndredquad, prelindep, preobjcutdetect.  See the
"xpress -=" output for details.  Tested with libraries for which 
"xpress -v" says "AMPL/XPRESS 26.01.04 ...".

## 20141223
  New keyword "advance".  Specifying advance=0 in $xpress_options
has the same effect as "option send_statuses 0;" before "solve;"
in an AMPL session.
  Update for XPRESS 7.8.  New keywords
	algaftercrossover
	algafternetwork
	concurrentthreads
	crossovertol
	dualizeops
	feastol_target
	hdive_rounding
	lpref_itlim
	opttol_target
	precomponents
	refineops

## 20150417
  New keywords for MIP solution pool:
	pooldualred
	pooldupcol
	pooldups
	poolfeastol
	poolmiptol
	poolnbest
	poolstub
and updated description of "heurthreads".  For details, see the
"xpress -=" output or the updated README.xpress.

## 20150529
  New keyword "bestbound".  See the updated "xpress -=" output.

## 20150819
  Update for XPRESS 7.9.  New keywords
	maximpliedbound
	miprefiterlim
	miptoltarget

## 20161110
  Update for XPRESS 8.0.  New keywords
	barorderthreads
	conedecomp
	heurrootcutfreq
	maxmiptasks
	mipstop
	permuteseed
	prepermute

## 20170113
  Add keyword "barobjscale".

## 20170314
  Add keyword "param".  See the "xpress -=" output for details.

## 20170404
  Suppress call on XPRSgetlpsol() when LPSTATUS is 7 (XPRS_LP_UNSOLVED),
so the solve exit code will be 0 rather than 1.

## 20170428
  xpress.c: change erroneous want_deriv to want_derivs, which should
slightly reduce times to read problems involving quadratic expressions.

## 20170511
  Update for XPRESS 8.2.  New keywords
	archconsistent
	crossoveritlim
	crossoverops
	crossoverthreads
	miprampup
	preimplications
	sifting
	tunerdir
	tunerhistory
	tunermaxtime
	tunermethod
	tunermethodfile
	tunerpermute
	tunertarget
	tunerthreads

## 20170904
  Arrange for the solve_message to have the form "XPRESS xx.yy.zz"
rather than just "XPRESS.xx.yy".  With XPRESS 8.2 this is
"XPRESS.31.01.02" and with XPRESS 8.3 it is "XPRESS.31.01.09".

## 20171004
  xpress.c: fix a glitch in the ordering of #include directives.
The glitch had no effect on binaries generated by AMPL Optimization
because of the way license checking is done.

## 20171006
  xpress.c:  add keyword "writeprob"; see the "xpress -=" output for
details.
  README.xpress: update with current "xpress -=" output.

## 20180129
  xpress.c: update to XPRESS 8.4.  New keywords heurforcespecobj,
lpfolding, preanalyticcenter, and prebasisred, and some new possible
values (7,8,9) for tunertarget.  See the "xpress -= output".

## 20180530
  xpress.c: add keyword bargaptarget; see the -= output for details.

## 20180613
  xpress.c: adjust to allow solving problems with more than 2^31
nonzeros (on 64-bit systems).

## 20180808
  Update to XPRESS 8.5, which has some bug fixes and improvements.
New keywords:

	dualperturb
	presolvepasses
	primalperturb

Modified keyword (to be withdrawn):

	perturb

Withdrawn keyword:

	tempbounds

See the "xpress -=" output for more details.

## 20190220
  xpress.c, README.xpress:  Adjust "maxtime" description (in
"xpress -=" output and in README.xpress) to accord with XPRESS
documentation.  For n > 0, maxtime=n allows execution to run more than
n seconds if needed to obtain a first feasible solution, at least on
problems with integer variables.

## 20190308
  xpress.c: when available (starting with XPRESS 8.5), use attribute
XPRESSVERSION to obtain the "8.5.10" in the current "AMPL/XPRESS
8.5.10(33.01.12)" part of the solve_message and "xpress -v" output.
Previously this had to specified with a -D option when compiling
xpress.c.  Now changes to the XPRESS libraries in use should be
reflected in this string.

## 20190711
  xpress.c: update to XPRESS 8.6, which has bug fixes and
improvements.  New keywords: barkernel, elimfillin, mipkappafreq,
objscalefactor, preconvertsep.  See the "xpress -=" output.

## 20191230
  xpress.c:  update to XPRESS 8.8, which has bug fixes and
improvements.  New keywords:  globalfilemax, globalloginterval,
maxmemoryhard, mipdualreductions, resourcestrategy.  Expanded
description of refineops.  Keyword nodefilebias is now noted
as "deprecated and ignored".  See the "xpress -=" output.

## 20200905
  xpress.c: update to XPRESS 8.9, which has bug fixes and improvements.

## 20200914
  xpress.c: relinked to eliminate bogus output when an AMPL license is not found

## 20201005
[MacOS] Added support for older version of MacOS.
