Program vector_5;

const

	n=10;

type

	t_dato=real;
	t_vector=array [1..n] of t_dato; 

var
	vector:t_vector;
	positivos, negativos, ceros: boolean;


Procedure inicializar (var vec:t_vector);
var

	lim:1..n;

begin
	for lim:= 1 to n do
	begin
		vec[lim]:=0;
	end;
end;

Procedure cargar (var vec:t_vector);
var

	lim:1..n;
	aux:t_dato;

begin
	for lim:=1 to n do
	begin
	writeln('Ingrese el componente N° ', lim, ' del vector.');
	read(aux);		
	vec[lim]:= aux
	end;
end;	

Procedure positivo (var vec:t_vector; var posi:boolean);
	var
		lim:1..n;

begin
	posi:=false;

	for lim := 1 to n do
	begin
		if (vec[lim] > 0) then
		begin
			posi:=true
		end;
	end;
end;

Procedure negativo (var vec:t_vector; var negat:boolean);
	var
		lim:1..n;

begin
	negat:=false;

	for lim := 1 to n do
	begin
		if (vec[lim] < 0) then
		begin
			negat:=true
		end;
	end;
end;

Procedure cero (var vec:t_vector; var cer:boolean);
	var
		lim:1..n;

begin
	cer:=false;

	for lim := 1 to n do
	begin
		if (vec[lim] = 0) then
		begin
			cer:=true
		end;
	end;
end;

begin
	inicializar(vector);
	cargar(vector);
	positivo(vector,positivos);
	if (positivos = true) then
	writeln('El vector contiene componentes positivos.');
	negativo(vector,negativos);
	if (negativos = true) then
	writeln('El vector contiene componentes negativos.');
	cero(vector, ceros);
	if (ceros = true) then
	writeln('El vector contiene ceros como componentes');

end.