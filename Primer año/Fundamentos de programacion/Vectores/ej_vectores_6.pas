Program copii;

uses 
	crt;

const
	n = 5;

type
	t_dato = char;
	t_vector = array[1..n] of t_dato;

var
	vector: t_vector;
	vector_2: t_vector;
procedure inicializar(var vec:t_vector);

var
	lim:1..n;

begin
	for lim:= 1 to n do
	begin
	vec[lim]:= ' ';
	end;
end;

procedure cargar(var vec:t_vector);

var
	lim:1..n;
	aux:t_dato;

begin
	for lim:=1 to n do
	begin
	writeln('Ingrese el componente N° ', lim,' del vector:');
	readln(aux);
	vec[lim]:=aux;
	end;
end;

procedure mostrar(var vec:t_vector);
	var
		lim: 1..n;
begin

	write('Vector A: ( ');
	for lim := 1 to n do
	begin
		write(vec[lim]);
	end;
	writeln(' ) ');
end;

procedure copiar(var vec:t_vector; var vec_2:t_vector);
	var
		lim: 1..n;

begin
	for lim:=1 to n do
	vec_2[lim]:=vec[lim];
end;

procedure mostrar_2(var vec_2:t_vector);
	var
		lim: 1..n;
begin
	write('Vector B: ( ');
	for lim := 1 to n do
	begin
		write(vec_2[lim]);
	end;
	write(' ) ');
end;

begin
	inicializar(vector);
	cargar(vector);
	mostrar (vector);
	copiar(vector,vector_2);
	writeln('Presione enter para que se imprima en pantalla un vector igual al anterior.');
	readkey;
	mostrar_2(vector_2);
	readkey;
end.