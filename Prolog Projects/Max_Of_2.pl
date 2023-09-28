max(X,X):-write('Larger number is '),write(X).
max(X,Y):-X>Y,write('Larger number is '),write(X).
max(X,Y):-X<Y,write('Larger number is '),write(Y).
