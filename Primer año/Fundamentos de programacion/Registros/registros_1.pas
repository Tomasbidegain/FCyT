Program discos;

uses crt;

const
	n = 5;
type
	t_disco = record
		titulo:string [50];
		autor:string [50];
		anio:integer;
		duracion:real;
	end;

	t_vector = array[1..n] of t_disco;

var
	dis: t_vector;
	disco: t_disco;

procedure inicializar_reg(var d: t_disco);

begin
	with d Do
	begin
		titulo:='';
		autor:='';
		anio:=0;
		duracion:=0;
	end;
end;

procedure cargar_reg(var d: t_disco);

begin
	with d Do
	begin
		readln(titulo);
		readln(autor);
		readln(anio);
		readln(duracion);
	end;
end;

procedure listar_reg(var d: t_disco);

begin
	with d Do
	begin
		writeln(titulo);
		writeln(autor);
		writeln(anio);
		writeln(duracion);
	end;
end;

procedure inicializar(var dis:t_vector);
var
	i: Integer;
begin
	for i:= 1 to n Do
	begin
		inicializar_reg(dis[i]);
	end;
end;

procedure cargar(var dis:t_vector);
var
	i: Integer;
begin
	for i := 1 to n Do
	begin
		cargar_reg(dis[i]);		
	end;	
end;

procedure listar(var dis:t_vector);
var
	i: Integer;

begin
	for i:= 1 to n Do
	begin
		listar_reg(dis[i]);
	end;
end;

	
begin
	inicializar_reg(disco);
	cargar_reg(disco);
	listar_reg(disco);
	inicializar(dis);
	cargar(dis);
	listar(dis);
end.

