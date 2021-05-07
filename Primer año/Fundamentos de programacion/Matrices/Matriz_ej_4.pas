Program pares;

uses crt,matriz;

const 
	n=3;
	m=2;

type
	t_dato = integer;
	t_matriz = array [1..n,1..m] of t_dato;

var
	mat: t_matriz;
	max_ij:t_dato;

procedure indices_pares(var mat:t_matriz; var max_ij:t_dato);
var 
	i,j:t_dato;

begin
	max_ij:=0;
	for i:= 1 to n do
	begin
		for j := 1 to m do
		begin
			if ((i+j) mod 2 = 0) then
			begin
			if (max_ij < mat[i,j]) then
			begin
				max_ij:=mat[i,j];
			end;

			end;
		end;		
	end;		
end;

begin
	inicializar_matriz(mat);
	cargar_matriz(mat);
	indices_pares(mat,max_ij);
	writeln('El mayor elemento, con la suma de sus subindices par, es: ', max_ij);
end.
