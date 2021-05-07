Program Calculadora;
var n1, n2:Integer;
	op: Char;

begin
	
writeln('Ingrese el primer numero');

readln(n1);

writeln('ingrese el operador');

readln(op);

writeln('ingrese el segundo numero');

readln(n2);

begin

if (op='+')then

	writeln(n1+n2)

else
	if (op='-')then

	writeln(n1-n2)

else 
	if(op='*')then

	writeln(n1*n2)

else
	if(op='/')then
	writeln(n1/n2)
end;
readln()
end.




