unit matriz;

Interface

const 
	n=11;
	m=14;

type
	t_dato= string;
	t_matriz= array [1..n,1..m] of t_dato;


procedure inicializar_matriz (var mat:t_matriz);
procedure cargar_matriz(var mat:t_matriz);
procedure listar_matriz(var mat:t_matriz);

Implementation 

uses Crt;

var
	mat: t_matriz;

procedure inicializar_matriz (var mat:t_matriz);
	var
		i,j:integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			mat[i,j]:='';	
			end;
		end;	
end;

procedure cargar_matriz(var mat:t_matriz);
	var
		i,j: integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			writeln('Ingrese un elemento');
			read(mat[i,j]);
			end;
		end;			
end;

procedure listar_matriz(var mat:t_matriz);
	var
		i,j: integer;

begin
	for i:=1 to n do
	begin
		for j:= 1 to m do
		begin
			writeln(mat[i,j]);
		end;
	end;

end;

end.