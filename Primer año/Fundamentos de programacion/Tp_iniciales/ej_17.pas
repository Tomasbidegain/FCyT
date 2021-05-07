Program Meses;
Var mes:1..12;
begin

writeln('Para saber cuantos días tiene el mes ,ingrese el numero del mes');
readln(mes);

if (mes<=1) and (mes>=12) then
begin
	writeln('mes inválido');
end
else if (mes=2) then
begin
	writeln('tiene 28 días');
end
else if (mes=4)and(mes=6)and(mes=9)and(mes=11) then
begin
	writeln('tiene 30 días');
end
else
	writeln('Tiene 31 días')
end.