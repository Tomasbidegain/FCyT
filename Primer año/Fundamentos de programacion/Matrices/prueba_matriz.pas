Program asd;

uses crt;

const
	n = 2;
	m = 3;

Type
	t_dato= integer;
	t_matriz=array [1..n,1..m] of t_dato;

var
	mat: t_matriz;
	ac_su: t_dato;
	ac_ar: t_dato;


procedure inicializar_matriz (var mat:t_matriz);
	var
		i,j:Integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			mat[i,j]:=0;	
			end;
		end;	
end;

procedure cargar_matriz(var mat:t_matriz);
	var
		i,j: Integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			write('Ingrese un elemento');
			read(mat[i,j]);
			end;
		end;			
end;

procedure acumulador(var mat:t_matriz; ac_su:t_dato; ac_ar: t_dato);
var
	i,j: integer;

begin
	ac_su:=0;
	for i:= 1 to n do
	begin
		ac_ar:=0;
		for j := 1 to m do
			begin
				ac_ar:= ac_ar + mat[i,j];
			end;
		writeln('La cantidad de articulos vendidos es de: ', ac_ar);
		ac_su:= ac_ar;
		writeln('La cantidad de articulos vendidos por la sucursal ',i, ' es de: ', ac_ar);
	end;
end;
begin
	inicializar_matriz (mat);
	cargar_matriz(mat);
	acumulador(mat,ac_su,ac_ar);
end.


