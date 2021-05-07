unit matrices;

interface

uses crt;

const 
	n=100;
	m=100;

type
	t_dato: real;
	t_matriz: array [1..n,1..m] of t_dato;

procedure inicializar_matriz (var m:t_matriz);
procedure cargar_matriz(var m:t_matriz);
procedure listar_matriz(var m:t_matriz);

implementation 

procedure inicializar_matriz (var m:t_matriz);
	var
		i,j: 1..100;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
				m[i,j]:=0;	
			end;
		end;	
end;

procedure cargar_matriz(var m:t_matriz);
	var
		i,j: 1..100;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
				read(m[i,j]);
			end;
		end;			
end;

procedure listar_matriz(var m:t_matriz);
	var
		i,j: 1..100;

begin
	for i:=1 to n do

	begin
		for j:= 1 to m do
		begin
			writeln(m[i,j]);
		end;
	end;

end;
end.