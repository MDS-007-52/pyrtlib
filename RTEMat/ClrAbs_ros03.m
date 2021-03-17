%   Computes profiles of water vapor and dry air absorption for
%   a given set of frequencies.  Subroutines H2O_xxx and O2_xxx
%   contain the absorption model of Leibe and Layton [1987: 
%   Millimeter-wave properties of the atmosphere: laboratory studies 
%   and propagation modeling. NTIA Report 87-224, 74pp.] with oxygen 
%   interference coefficients from Rosenkranz [1988: Interference 
%   coefficients for overlapping oxygen lines in air.  
%   J. Quant. Spectrosc. Radiat. Transfer, 39, 287-97.]
%
%     inputs passed as arguments: 
%          p      = pressure profile (mb)
%          tk     = temperature profile (K)
%          !!!e      = vapor pressure profile (mb)
%          rho    = water vapor density (g/m3)
%          frq    = frequency (GHz)
%       absmdl    = Absorption model for WV (default 'ROS98')
%       absmdl.wvres = wv resonant absorption
%       absmdl.wvcnt = wv continuuum absorption
%     outputs: 
%          awet   = water vapor absorption profile (np/km)
%          adry   = dry air absorption profile (np/km)
%     subroutines:  
%          H2O_xxx = computes water vapor absorption
%          O2_xxx  = computes oxygen (dry air) absorption
%          (H2O and O2 both call subroutine Shape.)

function [awet,adry] = ClrAbs_ros03(p,tk,e,frq);

nl = length(p);
awet = zeros(size(p));
adry = zeros(size(p));
factor = .182 * frq;
db2np = log (10.) * 0.1;

for i = 1:nl
  
%c  Compute inverse temperature parameter; convert wet and dry p to kpa.
    v = 300. / tk(i);
    ekpa = e(i) / 10.;
    pdrykpa = p(i) / 10. - ekpa;
  
%c  Compute H2O and O2 absorption (dB/km) and convert to np/km. 
    [npp,ncpp] = h2o_rosen03_xxx(pdrykpa,v,ekpa,frq);
    awet(i) = (factor * (npp + ncpp)) * db2np;
    [npp,ncpp] = o2n2_rosen03_xxx(pdrykpa,v,ekpa,frq);
    adry(i) = (factor * (npp + ncpp)) * db2np;
    
end




return