Program ej_2;

uses crt;matriz;

const
	n = 20;
	m = 30;

Type
	t_dato: integer;
	t_matriz: array [1..n,1..m] of t_dato;

var
	mat: t_matriz;
	ac_su: t_dato;
	ac_ar: t_dato;


procedure acumulador(var mat:t_matriz; ac_su:t_dato; ac_ar: t_dato);
var
	i,j: t_dato;

begin
	ac_su:=0;
	for i:= 1 to n do
	begin
		ac_ar:=0;
		for j := 1 to m do
			begin
				ac_ar:= ac_su + mat[i,j];
				writeln('La cantidad de articulos vendidos es de: ', ac_su;);
			end;

		ac_su:= ac_ar;
		writeln('La cantidad de articulos vendidos por la sucursal ',i, ' es de: ', ac_ar;);
	end;
end;

begin
	inicializar_matriz (mat);
	cargar_matriz(mat);
	acumulador(mat,ac_su,ac_ar);
end.

