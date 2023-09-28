max(P,P,P):-('Largest number is '),write(P).
max(P,Q,R):-P>Q,P>R,write('Largest number is '),write(P).
max(P,Q,R):-P<Q,Q>R,write('Largest number is '),write(Q).
max(P,Q,R):-R>Q,P<R,write('Largest number is '),write(R).
