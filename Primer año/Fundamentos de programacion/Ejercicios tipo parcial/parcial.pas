program tipo_parcial;

uses crt;

const
	n=5;

type
	t_obra = record
		apynom: string;
		obra_s: string;
		monto_cuota: real;
		integrantes: word;
	end;

	t_vector = array  [1..n] of t_obra;

var
	obra: t_obra;
	vec: t_vector;
	buscado: string;
	ac_monto:real;
	cont_integrantes,lim,pos:word;


procedure inicializar_reg (var obra: t_obra);
begin
	with obra do
	begin
		apynom:='';
		obra_s:='';
		monto_cuota:=0;
		integrantes:=0;
	end;
end;

procedure cargar_reg(var obra:t_obra);
begin
	with obra do
	begin
		write('Ingrese su apellido y nombre: ');
		readln(apynom);
		write('Ingrese su obra social: ');
		readln(obra_s);
		write('Ingrese el monto de cuota: ');
		readln(monto_cuota);
		write('Ingrese la cantidad de integrantes: ');
		readln(integrantes);
	end;
end;

procedure listar_reg(var obra:t_obra);
begin
	with obra do
	begin
		write('Apellido y nombre:');
		writeln(apynom);
		write('Obra social: ');
		writeln(obra_s);
		write('Monto de cuota: ');
		writeln(monto_cuota:2:0);
		write('Integrantes: ');
		writeln(integrantes);
	end;
end;

procedure inicializar_vec(var vec:t_vector);
var 
	i:word;
begin
	for i:= 1 to n do
	begin
		inicializar_reg(vec[i]);
	end;
end;

procedure cargar_vec(var vec:t_vector; var lim: word);
var 
	tecla:string;

begin
	readln(tecla);
	while (tecla = '1') and (lim < n) do
	begin
		inc(lim);
		cargar_reg(vec[lim]);
		textcolor(lightblue);
		writeln('1. Para cargar.');
		writeln('2. Para salir.');
		write('#Opcion: ');
		textcolor(white);
		readln(tecla);
	end;
end;

procedure burbuja_obra (var vec:t_vector; lim:word);

var 
	i,j:word;
	aux: t_obra;

begin
	for i:= 1 to lim-1 do
	begin
		for j:= 1 to lim-i do
		begin
			if (vec[j].obra_s + vec[j].apynom) > (vec[j+1].obra_s + vec[j+1].apynom) then
			begin
				aux:= vec[j];
				vec[j]:= vec[j+1];
				vec[j+1]:= aux;
			end;
		end;
	end;
end;

procedure listar_por_obra(var vec:t_vector; lim: word);
var 
	i:word;
begin
	for i:= 1 to lim do
	begin
		listar_reg(vec[i]);
	end;
end;

procedure bbin_osseg(var vec: t_vector; lim: word; var buscado: string; var pos:word);
var 
	pri, med, ult: word;

begin
	pri:=1;
	ult:=lim;
	pos:=0;
	while (pos = 0) and (pri <= ult) do
	begin
		med:= (pri+ult) div 2;
		if (vec[med].obra_s = buscado) then
		begin
			pos:= med;
		end;
		if (vec[med].obra_s > buscado) then
		begin
			ult:= med-1;
		end
			else
			begin
				pri:= med+1;
			end;
	end;
end;

procedure z (var vec:t_vector;lim:word;var ac_monto:real ;var pos: word);
begin
	while (vec[pos-1].obra_s = buscado) and (pos > 1) do
	begin
		pos:= pos-1;
	end;
	while (vec[pos].obra_s = buscado) and (pos <= lim) do
	begin
		if (vec[pos].apynom[1] = 'Z') and (buscado = 'Osseg') then
		begin
			listar_reg(vec[pos]);
			with obra do
			begin
				ac_monto:= ac_monto + monto_cuota;
			end;	
			inc(pos);
		end;
	end;
end;

procedure familias (var vec:t_vector;var cont_integrantes: word; lim:word);
var 
	i:word;

begin
	for i:= 1 to lim do
	begin
		if (vec[i].integrantes >= 6) then
		begin
			inc(cont_integrantes);
			if (vec[i].monto_cuota = 5000) then
			begin
				writeln('Familias con mas de 6 integrantes, que aportan mas de $5000');
				listar_reg(vec[i]);
			end;
		end;
	end;
end;

begin
	ac_monto:=0;
	inicializar_vec(vec);
	textcolor(lightblue);
	gotoxy(14,2);writeln('---------------------------');
	gotoxy(14,2);writeln('|');
	gotoxy(41,2);writeln('|');
	gotoxy(14,3);writeln('|');
	gotoxy(41,3);writeln('|');
	gotoxy(14,5);writeln('|');
	gotoxy(41,5);writeln('|');
	gotoxy(15,3); writeln('1. Para comenzar a cargar.');
	gotoxy(14,4);writeln('---------------------------');
	gotoxy(15,5);writeln('2. Para salir.');
	gotoxy(14,6);writeln('---------------------------');
	gotoxy(5,7);write('#Opcion: ');
	textcolor(white);
	cargar_vec(vec,lim);
	burbuja_obra(vec,lim);
	writeln('Listado ordenado por obra social: ');
	listar_por_obra(vec,lim);
	writeln('Ingrese la obra social a buscar: ');
	readln(buscado);
	bbin_osseg(vec,lim,buscado,pos);
	if (pos <> 0) and (vec[pos].apynom[1] = 'Z') then
	begin
		writeln('Afiliados cuyos apellidos comienzan con "Z" y su obra social es OSSEG');
		z (vec,lim,ac_monto,pos);
		writeln('Monto total aportado: ');
		writeln(ac_monto:2:0);
		readkey;
	end;
	familias (vec,cont_integrantes,lim);
	if (cont_integrantes <> 0) then
	begin
		writeln('Familias con mas de 6 integrantes: ', cont_integrantes);
	end;
readkey;
end.


