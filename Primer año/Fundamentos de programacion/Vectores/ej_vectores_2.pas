Program numeros_par;

uses crt;

const
	n=100

type
	t_dato: integer;
	t_vector: array [1..n] of t_dato;
var
	vector: t_dato;

procedure inicializacion(var vec:t_vector);
	var
		lim:1..n;

begin
	for lim := 1 to n do
	begin
		vec[lim]:=0;
	end;
end;

procedure cargar(var vec:t_vector);
	var
		lim: 1..n;
		aux:t_dato;

begin
	for lim:=1 to n do;
	begin
	writeln('Ingrese el componente N° ',lim 'del vector. ');
	read(aux);		
	vector[lim]:= aux
	end;
end;	

