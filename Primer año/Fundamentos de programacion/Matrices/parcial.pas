Program parcial;

uses crt;

const
	n=5;
	m=5;

type
	t_dato = real;
	t_matriz = array [1..n,1..m] of t_dato;

var
	mat: t_matriz;
	ac_piso,max_piso: t_dato;
	piso:word;


procedure inicializar(var mat:t_matriz);
var 
	i,j:word;
begin
	for i:= 1 to n do
	begin
		for j:=1 to m do
			mat[i,j]:=0;
	end; 
end;

procedure cargar (var mat: t_matriz);
var 
	i,j:word;

begin
	for i:=1 to n do
	begin
		for j:= 1 to m do
		begin
			writeln('Ingrese el monto del dpto ',j,' piso ',i);
			readln(mat[i,j]);
		end;
	end;
end;	

procedure monto_piso(var mat:t_matriz;var ac_piso:t_dato;var max_piso:t_dato; var piso:word);
var 
	i,j:word;

begin
	for i:=1 to n do
	begin
		ac_piso:=0;
		for j:= 1 to m do
		begin
			ac_piso:= ac_piso + mat[i,j];
		end;
		writeln('Monto abonado por el piso ',i,': ',ac_piso:2:0);
		if max_piso < ac_piso then
		begin
			max_piso:= ac_piso;
			piso:=i;
		end;
	end;
	writeln('El piso con mayor monto es el ',piso,' con $',max_piso:2:0);
end;

begin
	inicializar(mat);
	cargar(mat);
	monto_piso(mat,ac_piso,max_piso,piso);
	readkey;
end.	