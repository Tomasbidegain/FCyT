Program NumReal;

uses crt;

const n=5;

type
	t_dato=real;
	t_vector=array[1..n] of t_dato;

var
	vector: t_vector;

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
	writeln('ingrese el primer componente del vector');
	read(aux);		
	vec[lim]:=aux;
	end;
end;

Procedure mostrar_vector(var vec:t_vector);

var lim:1..n;
	ac_suma:real;

begin
	for lim:=1 to n do
	begin
	ac_suma:=(ac_suma)+(vec[lim]);
	end;
	writeln('La suma de los componentes del vector es: ', ac_suma:2:0);
end;

begin
	inicializar(vector);

	cargar(vector);

	mostrar_vector(vector);
	
	readkey;
end.

