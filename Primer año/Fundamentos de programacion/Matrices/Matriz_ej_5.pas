Program ej_5;

uses crt,matriz;

const
	n = 150;
	m = 12;

type 
	t_dato = real;
	t_matriz = array [1..n, 1..m] of t_dato;

var
	mat: t_matriz;
	maxi,min,mont: t_dato;
	may,c,mes:integer;




procedure cargar_montos(var mat:t_matriz);
var
	i,j: Integer;
begin
	for j:=1 to m do
	begin
		for i:=1 to n do
		begin
			writeln('Ingrese el monto total facturado: ');
			read(mat[j,i]);
		end;
	end;
end;

procedure mostrar_monto (var mat:t_matriz; var mont:t_dato);
var
	i,j: Integer;

begin
	for j:=1 to m do
	begin
		for i:=1 to n do
		begin
			if (i = 142) and (j = 8) then
			mont:= mat[j,i];
		end;
	end;
end;

procedure maximo(var mat:t_matriz; maxi:t_dato; var may:integer);
var
	i,j: Integer;
begin
	maxi:=0;
	for j:= 1 to m do
	begin
		for i:= 1 to n do
		begin
			if maxi < mat[j,i] then
				maxi:= mat[j,i];
				may:=i;
		end;
	end;
end;

procedure minimo(var mat:t_matriz; min:t_dato; var c:integer; var mes:integer);
var
	i,j: Integer;

begin
	min:=mat[1,1];
	for j:=1 to m do
	begin
		for i:=1 to n do 
		begin
			if min > mat[j,i] then
			begin
				min:=mat[j,i];
				mes:=j;
				c:=i;
			end;
		end;
	end;
	
end;

begin
	inicializar(mat);
	cargar_montos(mat);
	mostrar_monto (mat, mont);
	writeln('El monto del cliente 142 es: ', mont);
	maximo(mat,maxi,may);
	writeln('El cliente N° ',maxi,' registró el mayor monto de facturación mensual.');
	minimo(mat,min,c,mes);
	writeln('En el mes ',mes ,' se registró la menor facturación mensual para el cliente N° ', c);

end.
