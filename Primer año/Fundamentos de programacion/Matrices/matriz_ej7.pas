Program suma;

uses crt,matriz;

const
	n = 5;
	m = 5;

type
	t_dato = Integer;
	t_matriz =	array[1..n,1..m] of t_dato;

var
	mat: t_matriz;
	ac_suma:t_dato;

procedure suma(var mat:t_matriz;var ac_suma:t_dato);
var
	i,j: t_dato;
begin
	ac_suma:=0;
	for i:= 1 to n Do
	begin
		for j := 1 to m Do
		begin
			if (i <> j) and (i>j) then
			ac_suma:=ac_suma+mat[i,j];

		end;
	end;
end;

begin
	inicializar_matriz(mat);
	cargar_matriz(mat);
	suma(mat, ac_suma);
	writeln('La suma de los elementos que estan por encima de la diagonal principal es: ', ac_suma);
end.