program ej_3;
uses crt;
const
	n=4;
	m=3;

type
	t_dato=integer;
	t_matriz= array [1..n,1..m] of t_dato;

var
	mat:t_matriz;
	suma, max:t_dato;

procedure inicializar_matriz(var mat:t_matriz);
	var
		i,j: integer;

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
		i,j: integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			write('ingrese un valor');
			read(mat[i,j]);
			end;
		end;			
end;

procedure suma_columna(var mat:t_matriz; suma:t_dato);
	var
	i,j: integer;

begin
	for j:= 1 to m do
		begin
			suma:=0;
			for i := 1 to n do
			begin
			 	suma:=(suma+mat[j,i]);   
			end;
		write('la sumatoria de esta columna es ', suma);	
		end;
end;

procedure mayor_columna(var mat:t_matriz; max:t_dato);
var
	i,j: integer;

begin
	for j := 1 to m do
		begin
			for i := 1 to n do
				begin
					if (mat[j,i]>max) then 
					max:=mat[j,i];
				end;
		write('el mayor valor de esta columna es ', max);		
		end;
end;

begin
inicializar_matriz(mat);
cargar_matriz(mat);
suma_columna(mat, suma);
mayor_columna(mat, max);
readkey;
end.