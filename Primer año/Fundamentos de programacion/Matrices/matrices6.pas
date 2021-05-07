Program ej_6;

uses crt,matriz;

const
	n=10;
	m=5;

type
	t_dato = char;
	t_matriz = array [1..n,1..m] of t_dato;

var
	mat: t_matriz;
	promed, promed_max, promedmat, promedmax: real;
	cont_al,cont_m,acumax:integer;


procedure cargar_matriz_1(var mat:t_matriz);
var 
	i,j: integer;
begin
	for i:=1 to n do 
	begin
		for j := 1 to m do
		begin
			writeln('Ingrese la nota del alumno: ');
			readln(mat[i,j]);
				if (mat[i,j] = '') then
				begin
					mat[i,j] := '-';
				end;

		end;
	end;
end;

procedure promedio(var mat:t_matriz; var promed:real; cont_al: integer;var acumax:integer; var promedmax:real);
var
	i,j: Integer;
begin
	promed_max:=0;
	acumax:=0;
	for j:= 1 to m do
	begin
		cont_al:=0;
		for i:= 1 to n do
		begin
			if (mat[i,j] <> '') then
			begin
			cont_al:= cont_al+1;
			end;
		end;
		promed:=(cont_al/n);
		writeln('El promedio de alumnos de esta materia es: ', promed);
		acumax:= (acumax + cont_al)
		;
	end;
	promedmax:=(acumax/m);
	writeln('El promedio general de los alumnos es ', promedmax);
end;

procedure materias_cursadas(var mat:t_matriz; cont_m:integer; promedmat:real);
var 
	i,j: integer;
begin
	for i:=1 to n do 
	promedmat:=0;
	cont_m:=0;
	begin
		for j := 1 to m do
		begin
			if (mat[i,j] <> '') then
				cont_m:= cont_m+1;
		end;
		writeln('La cantidad de materias cursadas para el alumno ',i,' es: ',cont_m);
		promedmat:=(cont_m/m);
		writeln('El promedio de materias cursadas de el alumno ', i,' es: ',promedmat);
	end;
end;
begin
	inicializar(mat);
	cargar_matriz_1(mat);
	promedio(mat,promed,cont_al,acumax,promedmax);
	materias_cursadas(mat,cont_m,promedmat);


end.

