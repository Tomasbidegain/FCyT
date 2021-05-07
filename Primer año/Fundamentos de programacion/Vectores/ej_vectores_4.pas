Program generar_vector;

uses crt;

const n=100;

type

	t_dato=integer;
	t_vector=array[1..n] of t_dato;

var
	vector:t_vector;

Procedure inicializacion (var vec:t_vector);
	var
		lim:1..n;

begin
	for lim:= 1 to n do
 	begin
 		vec[lim]:=0;
 	end;
end;

procedure cargar (var vec:t_vector);
	var
		lim:1..n;
begin
	for lim := 1 to n do
	begin
		if ((lim mod 2)<>0) then
		begin
			vec[lim]:=1;
		end
		else 
		begin
		if ((lim mod 2)=0) then
			vec[lim]:=0;
		end;
	end;
end;

procedure mostrar(var vec:t_vector);
	var
		lim:1..n;

begin
	for lim:= 1 to n do
	 write(vec[lim]);
end;
begin
	inicializacion(vector);
	cargar(vector);
	mostrar(vector);
end.