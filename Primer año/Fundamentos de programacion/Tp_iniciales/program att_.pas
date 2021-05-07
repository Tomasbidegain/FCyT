program att;
uses crt;

const
	n=20;
	m=30;

type
	t_dato=integer;
	t_matriz= array [1..n,1..m] of t_dato;


var
	mat:t_matriz;

procedure inicializar_matriz(var mat:t_matriz);
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

begin
	inicializar_matriz(mat);
	cargar_matriz(mat);
end.