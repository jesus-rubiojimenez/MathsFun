function [C] = nCkLog(n,k)
% Given the integers n and k, with k in [n, 0), 
%
%   nCkLog(n,k)
%
% returns the natural logarithm of the binomial coefficient C(n, k), i.e., log[C(n, k)].
%
% Dr Jesús Rubio
% University of Exeter
% J.Rubio-Jimenez@exeter.ac.uk
% Created: June 2020
% Last modified: Jan 2022

aux=0;
for x=k+1:n
    aux=aux+log(x)-log(x-k);
end

C=aux;
end
