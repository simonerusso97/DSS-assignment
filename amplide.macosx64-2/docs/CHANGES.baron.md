# BARON/AMPL Changelog
All notable changes to this project will be documented in this file.
## 20201005
### Fixed
- [MacOS] Added support for older version of MacOS
## 20200921
### Changed
- [Linux] update to correctly find version 36 of xpress library.
## 20200905
### Changed
- Update to Baron 20.04.14
### Fixed
- Fixed a bug with iisfind, where the infeasible subset was not returned due to changes in how Baron passes the information back to AMPL
- Fixed a problem with rpath of the OSX shared library.
### Added
- Added value `Both` for  the iis suffix, to identify variables and inequality constraints whose lower or upper bounds are in the IIS.

## 20200820
Minor tweaks to -= output.

## 20191216
### Changed
- Update to Baron 19.12.07, which has performance improvements on large-scale problems and mised-integer QPs.

## 20190908
### Fixed
- Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190713
### Changed
- Update to Baron 19.7.13 to fix a fault seen in the MS Windows binary.

## 20190711
### Changed
- Update to Baron 19.7.9, which has various improvements and bug fixes.

## 20190322
### Changed
- Update to Baron 19.3.22, which has various improvements and a new keyword, firstloc. See the updated README.baron or "baron -=" output. The 32-bit binaries remain at version 18.5.8 and do not have the new keyword.

## 20190320
### Fixed
- Fix a bug with unary minus applied to a sum or difference. The resulting nonlinear evaluations were wrong.
### Added
- New keywords deltaa, deltar, deltat, deltaterm and associated new solve_result_num = 150. See the updated README.baron or "baron -=" output.

## 20190116
### Fixed
- Fix a glitch with "maxtime=1000". Other maxtime values were unaffected.

## 20181116
### Changed
- Update to Baron 18.11.12, which has a more robust treatment of cutting planes and better optimality-based range reductions.
- Ignore HEARTBEAT lines in the ampl.lic file.

## 20180928
### Added
- Add keywords iisfind, iisint, iisorder related to finding an irreducible infeasible set of constraints and variable bounds for infeasible problems. Baron often reports that the sets it finds may not be irreducible. See the "baron -=" output for more details. New solve_result_num values:
```
201 → infeasible, IIS found
202 → infeasible, IS found, possibly not irreducible
203 → infeasible, IIS sought but not found
```

## 20180925
### Fixed
- Recreate the MacOSX64 bundle so libbaron-osx64.dylib knows to look in the directory containing baron for libiomp5.dylib. This does not matter for some systems.

## 20180823
### Changed
- Update to Baron 18.8.23, which has some bug fixes and improvements and is only available for 64-bit versions of Linux, MacOSX, and MS Windows. No further updates to 32-bit binaries are expected.

## 20180813
### Fixed
- Fix some trouble with numsol=n for n >= 2: only one solution file was produced, likely not for the best solution found.

## 20180508
### Changed
- Update to Baron 18.5.8, which has various improvements and bug fixes.

## 20180307
### Changed
- Arrange for lpsolver=cplex and lpsolver=xpress to work with more recent versions of cplex and xpress, respectively. For MS Windows, currently cplex1280.dll, cplex1271.dll, cplex1270.dll and cplex1263.dll are explicitly recognized. Copying another cplex*.dll to cplex.dll may work if not too old. For example, cplex124.dll is too old.

## 20171013
### Changed
- Update to Baron 17.10.13 to fix a glitch -- undesired output -- under MS Windows.

## 20171011
### Changed
- Update to Baron 17.10.10, which has some bug fixes.

## 20170812
### Changed
- Update to Baron 17.8.7, which has bug fixes, performance improvements, and another builtin local nonlinear solver (FilterSQP). New keyword "nlpsol"; see the "baron -=" output for details. 
### Deprecated 
- Keyword "filter" is now deprecated (replaced by suitable nlpsol assignments).

## 20170628
### Changed
- Update to Baron 17.6.24, which has bug fixes and performance improvements.

## 20170511
### Added
- New keyword "version" (no value) causes version, platform, and license to be reported.

## 20170401
### Changed
- Update to Baron 17.4.1, which has some bug fixes and performance improvements.

## 20170321
### Changed
- Update libbaron-osx64.dylib (MacOSX only) to look in the directory containing baron (as well as standard places) for libiomp5.dylib.

## 20170121
### Changed
- Update so lpsolver=cplex and lpsolver=xpress work with current versions of cplex and xpress. This was already true for MacOSX (version 20170116).

## 20170116
### Fixed
- Fix a glitch with multiple objectives: the objective used was not transmitted (via the .sol file) to the AMPL session.
- In the binary for 32-bit MS Windows, fix trouble with "lpsolver=xpress".

## 20170112
### Changed
- Update to Baron 17.1.2, which has some bug fixes and performance improvements. 
### Fixed
- Specifying "lpsolver=xpress" (when permitted by licensing) now works except for 32-bit MS Windows.

## 20161207
### Changed
- Update to Baron 16.12.7, which has some bug fixes and performance improvements.

## 20161001
### Fixed
- Fix a bug that sometimes caused baron to go into an infinite loop after solving a problem with defined variables.

## 20160927
### Fixed
- Fix a bug with temporary or time-limited cplex or xpress licenses in conjunction with lpsolver=cplex or lpsolver=xpress. The bug led to a "license not found" message.

## 20160921
### Added
- Add "No value is expected." to the description of objbound in the "baron -=" output.

## 20160920
### Fixed
- Fix glitches with keyword lpsolver. If given a bad value, the error message involved some erroneous text. If lpsolver appeared in $baron_options and other settings followed, lpsolver was incorrectly diagnosed as having an incorrect value.
### Added
- New keyword "objbound" requests return of suffixes .obj_lb and .obj_ub on the problem and objective for Baron's final lower and upper bounds on the objective value.

## 20160729
### Changed
- Update to BARON 16.7.29, which has various bug fixes and improvements. No changes to $baron_options.

## 20160531
### Changed
- Relink MacOSX version so libbaron-osx64.dylib will look for libiomp5.dylib in the directory containing "baron".

## 20160407
### Changed
- Update to BARON 16.4.4, which has some bug fixes and improvements. Dual variable values are now returned.

## 20160316
### Changed
- Update to BARON 16.3.16, which has various bug fixes and improvements. No changes to $baron_options.

## 20160129
### Fixed
- Adjust to work when one uses "option presolve 0" (a bad idea) and the problem has some empty constraints.

## 20160122
### Changed
- Linux 64-bit binary relinked so as not to require GLIBC 2.14.

## 20151205
### Fixed
- Fix a bug affecting "baron ... lpsolver=..." that could cause some licenses not to be returned.
### Changed
- Update to CPLEX 12.6.3, which affects "lpsolver=cplex".

## 20151125
### Changed
- For Linux binaries, add the directory containing the binary to the library search rules.

## 20151120
### Added
- Update driver to deal with complementarity constraints.

## 20150929
### Fixed
- Update to BARON 15.9.22, to fix a fault that was possible under some conditions.
### Added
- New keyword "lpsolver" to specify the choice of LP solver, which matters mainly when there are integer variables: possible values are cbc (default), cplex, or xpress. The last two must be suitably licensed to be used.

## 20150911
### Fixed
- Fix a bug that sometimes affected keyword lsolver under MS Windows.

## 20150826
### Changed
- Update to version 15.8.26, which has many bug fixes and small performance improvements.

## 20150729
### Fixed
- Add possible solve_result_num value 100 for "numerical difficulties but possibly optimal".
- Adjust MacOSX version so __ZNKSt5ctypeIcE13_M_widen_initEv is not required. It is missing in the C++ run-time libraries on some MacOSX systems.

## 20150630
### Fixed
- Fix some possible trouble with a single-use license.

## 20150605
### Changed
- Update to BARON 15.6.5, which has various bug fixes.

## 20150529
### Fixed
- Fix a typo in the baron.doc* bundles and add an "INSTALLING" section. 
- Relink the 64-bit Linux version to not require GLIBC 2.14.

## 20150424
### Fixed
- Fix a rarely seen licensing glitch.

## 20150416
### Added
- Add keywords maxiter and maxtime; expand description of optfile in the "baron -=" output. Recognize comment lines in optfile (starting with #).

## 20150319
### Changed
- Improved handling of keyword "numsol"; values > 1 now imply keepsol.