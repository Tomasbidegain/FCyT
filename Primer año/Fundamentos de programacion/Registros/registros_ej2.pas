Program auto;

uses crt;

const
	n=5;

type
	t_autos = record
		marca:string [50];
		modelo:integer;
		anio:integer;
		color:string[20];
		can_puertas:integer;
		precio:real;
	end;
	t_vector = array[1..n] of t_autos;

var
	au: t_vector;
	aut: t_autos;

procedure inicializar_reg(var a: t_autos);

begin
	with a Do
	begin
		marca:='';
		modelo:=0;
		anio:=0;
		color:='';
		can_puertas:=0;
		precio:=0;
	end;
end;

procedure cargar_reg(var a: t_autos);

begin
	with a Do
	begin
		writeln('Ingrese la marca del auto.');
		readln(marca);
		writeln('Ingrese el modelo.');
		readln(modelo);
		writeln('Ingrese el año del auto.');
		readln(anio);
		writeln('Ingrese el color del auto.');
		readln(color);
		writeln('Ingrese la cantidad de puertas.');
		readln(can_puertas);
		writeln('Ingrese el precio.');
		readln(precio);
	end;
end;

procedure listar_reg(var a: t_autos);

begin
	with a Do
	begin
		writeln(marca);
		writeln(modelo);
		writeln(anio);
		writeln(color);
		writeln(can_puertas);
		writeln(precio);
	end;
end;


procedure inicializar(var au:t_vector);
var
	i: Integer;
begin
	for i:= 1 to n Do
	begin
		inicializar_reg(au[i]);
	end;
end;

procedure cargar(var au:t_vector);
var
	i: Integer;
begin
	for i := 1 to n Do
	begin
		cargar_reg(au[i]);		
	end;	
end;

procedure listar(var au:t_vector);
var
	i: Integer;

begin
	for i:= 1 to n Do
	begin
		listar_reg(au[i]);
	end;
end;


begin
	inicializar_reg(aut);
	cargar_reg(aut);
	listar_reg(aut);
	inicializar(au);
	cargar(au);
	listar(au);

end.
