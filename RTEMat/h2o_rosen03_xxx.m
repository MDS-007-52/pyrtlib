% C************************************
% C The interface of the following original function is changed to match
% C the interface of the ETL routine.    Yong Han, 1999.
% 
% C      FUNCTION ABH2O(T,P,RHO,F)
% C  Copyright (c) 2002 Massachusetts Institute of Technology
% C
% C  NAME- ABH2O    LANGUAGE- FORTRAN 77
% C
% C PURPOSE- COMPUTE ABSORPTION COEF IN ATMOSPHERE DUE TO WATER VAPOR
% C 
% C      IMPLICIT NONE
% C  CALLING SEQUENCE PARAMETERS-
% C    SPECIFICATIONS
% C      REAL T,P,RHO,F,ABH2O
% C      NAME    UNITS    I/O  DESCRIPTON            VALID RANGE
% C      T       KELVIN    I   TEMPERATURE
% C      P       MILLIBAR  I   PRESSURE              .1 TO 1000
% C      RHO     G/M**3    I   WATER VAPOR DENSITY
% C      F       GHZ       I   FREQUENCY             0 TO 800
% C      ABH2O   NEPERS/KM O   ABSORPTION COEFFICIENT
% C
% C   REFERENCES-
% C   P.W. ROSENKRANZ, RADIO SCIENCE V.33, PP.919-928 (1998); V.34, P.1025 (1999).
% C
% C   LINE INTENSITIES SELECTION THRESHOLD=
% C     HALF OF CONTINUUM ABSORPTION AT 1000 MB.
% C   WIDTHS MEASURED AT 22,183,380 GHZ, OTHERS CALCULATED.
% C     A.BAUER ET AL.ASA WORKSHOP (SEPT. 1989) (380GHz).
% c     M. TRETYAKOV et al., J. MOLEC. SPEC. (2003)
% C
% C   REVISION HISTORY-
% C    DATE- OCT.6, 1988  P.W.ROSENKRANZ - EQS AS PUBL. IN 1993.
% C          OCT.4, 1995  PWR- USE CLOUGH'S DEFINITION OF LOCAL LINE
% C                   CONTRIBUTION,  HITRAN INTENSITIES, ADD 7 LINES.
% C          OCT. 24, 95  PWR -ADD 1 LINE.
% C          JULY 7, 97   PWR -SEPARATE COEFF. FOR SELF-BROADENING, 
% C                       REVISED CONTINUUM.
% C        Aug. 28, 2002  PWR - CORRECTED LINE INTENSITIES
% C        Mar. 2, 2003   PWR - LINE SHIFT
% C
% C*************************************
% CYH **** add the following lines ******************************

%      subroutine H2O_xxx(pdrykpa,vx,ekpa,frq,npp,ncpp)
function [npp,ncpp] = h20_rosen03_xxx(pdrykpa,vx,ekpa,frq);

%CYH ***********************************************************

%C   LOCAL VARIABLES:
%       INTEGER NLINES,I,J
%       PARAMETER (NLINES=15)
%       REAL DF(2),S1(NLINES),B2(NLINES),W3(NLINES),FL(NLINES),X(NLINES),
%      & WS(NLINES),XS(NLINES),SR(NLINES)
%       REAL PVAP,PDA,DEN,TI,TI2,SUM,WIDTH,WSQ,S,BASE,RES,CON,SHIFT
%C     LINE FREQUENCIES:
      FL = [ 22.2351, 183.3101, 321.2256, 325.1529, 380.1974, 439.1508,...
            443.0183, 448.0011, 470.8890, 474.6891, 488.4911, 556.9360,...
            620.7008, 752.0332, 916.1712];
%C     LINE INTENSITIES AT 300K:
      S1 = [.1314E-13, .2279E-11, .8058E-13, .2701E-11, .2444E-10,...
            .2185E-11, .4637E-12, .2568E-10, .8392E-12, .3272E-11, .6676E-12,...
            .1535E-08, .1711E-10, .1014E-08, .4238E-10];
%C     T COEFF. OF INTENSITIES:
      B2 = [2.144, .668, 6.179, 1.541, 1.048, 3.595, 5.048, 1.405,...
            3.597, 2.379, 2.852, .159, 2.391, .396, 1.441];
%C     AIR-BROADENED WIDTH PARAMETERS AT 300K:
      W3 = [.00281, .00287, .0023, .00278, .00287, .0021, .00186,...
            .00263, .00215, .00236, .0026, .00321, .00244, .00306, .00267];
%C     T-EXPONENT OF AIR-BROADENING:
      X = [.69, .64, .67, .68, .54, .63, .60, .66, .66, .65, .69, .69,...
           .71, .68, .70];
%C     SELF-BROADENED WIDTH PARAMETERS AT 300K:
      WS = [.01349, .01491, .0108, .0135, .01541, .0090, .00788,...
            .01275, .00983, .01095, .01313, .01320, .01140, .01253, .01275];
%C     T-EXPONENT OF SELF-BROADENING:
      XS = [.61, .85, .54, .74, .89, .52, .50, .67, .65, .64, .72,...
            1.0, .68, .84, .78];
%C     RATIO OF SHIFT TO WIDTH
      SR = [0., -.017, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.];
%C
%CYH *** add the follwong lines *******************

      db2np = log(10.) * 0.1;
      rvap = 0.01 * 8.314510 / 18.01528;
      factor = .182 * frq;
      T = 300./vx;
      P = (pdrykpa+ekpa)*10.;
      RHO = ekpa*10./(rvap*T);
      F = frq;

%CYH ***********************************************

      if RHO <= 0.
        ABH2O = 0.;
        npp = 0;
        ncpp = 0;
        return
      end
      PVAP = RHO * T / 217;
      PDA = P - PVAP;
      DEN = 3.335E16 * RHO; %! const includes isotopic abundance
      TI = 300./T;
      TI2 = TI^2.5;

%C      CONTINUUM TERMS
      CON = (5.43E-10*PDA*TI^3 + 1.8E-8*PVAP*TI^7.5) * PVAP * F*F;
%C
%C      ADD RESONANCES
      NLINES = length(FL);
      SUM = 0.;
      for I = 1:NLINES
          WIDTH = W3(I)*PDA*TI^X(I) + WS(I)*PVAP*TI^XS(I);
          SHIFT = SR(I)*WIDTH; % ! unknown temperature dependence
          WSQ = WIDTH*WIDTH;
          S = S1(I)*TI2*exp(B2(I)*(1.-TI));
          DF(1) = F - FL(I) - SHIFT;
          DF(2) = F + FL(I) + SHIFT;
%C  USE CLOUGH'S DEFINITION OF LOCAL LINE CONTRIBUTION
          BASE = WIDTH/(562500. + WSQ);
%C  DO FOR POSITIVE AND NEGATIVE RESONANCES
          RES = 0.;
          for J = 1:2
              if abs(DF(J)) <= 750. 
                  RES = RES + WIDTH/(DF(J)^2+WSQ) - BASE;
              end
          end
          SUM = SUM + S*RES*(F./FL(I))^2;

%CYH **************************************************************
%C     separate the following original equ. into line and continuum
%C        terms, and change the units from np/km to ppm

%C      ABH2O = .3183E-4*DEN*SUM + CON

      npp = (.3183E-4 * DEN * SUM / db2np) / factor;
      ncpp = (CON / db2np) / factor;

%CYH *************************************************************
      end
      
return
end