program Uader;
uses crt;
const 
	n=20;
type 
	t_empleado=record
		apyn:string;
		legajo:integer;
		facultad:string;
		sede:string;
		tareas:string;
		end;

		t_vector= array [1..n] of t_empleado;

var 
	r:t_empleado;
	v:t_vector;
	buscado:string;
	lim,buscado_leg,pos_,c_ex,c_ac,c_in:integer;

procedure inicializar_reg (var r:t_empleado);
begin 
	with r do 
	begin
		apyn:='';
		legajo:=0;
		facultad:='';
		sede:='';
		tareas:='';
	end;
end;

procedure cargar_reg (var r:t_empleado);
begin 
	with r do 
	begin
		writeln('apellido y nombre: ');
		readln(apyn);
		writeln('legajo: ');
		read (legajo);
		writeln('facultad: ');
		read (facultad);
		writeln('sede: ');
		read (sede);
		writeln('tareas que desarrolla: ');
		read(tareas);
	end;
end;

procedure listar_reg (var r:t_empleado);
begin 
	with r do 
	begin
		writeln ('apellido y nombre: ',apyn);
		writeln ('legajo: ',legajo);
		writeln ('facultad: ',facultad);
		writeln ('sede: ',sede);
		writeln ('tareas que desarrolla: ',tareas);
	end;
end;

procedure inicializar_v (var v:t_vector);
var i:integer;
begin	
	for i:= 1 to n do
	begin 
		inicializar_reg (v[i]);
	end;
end;

procedure cargar_v (var v:t_vector; lim:integer);
var  
	tecla:string;
begin
	lim:=1;
	read (tecla);
	while (tecla = ' ') and (lim<n) do
	begin
		cargar_reg (v[lim]);
		inc (lim);
		read (tecla);	
	end;
end;

procedure listar_v (var v:t_vector);
var i:integer;
begin	
	for i:= 1 to n do
	begin 
		listar_reg (v[i]);
	end;
end;

procedure burbuja_fac (var v:t_vector; lim:integer);
var i,j:integer;
	aux:t_empleado;

begin
	for i:= 1 to lim-1 do
	begin
		for j:=1 to lim-i do
		begin
			if (v[j].facultad > v[j+1].facultad) then
			begin
				aux:=v[j];
				v[j]:=v[j+1];
				v[j+1]:=aux;
			end;
		end;
	end;
end;

procedure burbuja_sede (var v:t_vector; lim:integer);
var i,j:integer;
	aux:t_empleado;

begin
	for i:= 1 to lim-1 do
	begin
		for j:=1 to lim-i do
		begin
			if (v[j].sede > v[j+1].sede) then
			begin
				aux:=v[j];
				v[j]:=v[j+1];
				v[j+1]:=aux;
			end;
		end;
	end;
end;

procedure burbuja_leg (var v:t_vector; lim:integer);
var i,j:integer;
	aux:t_empleado;

begin
	for i:= 1 to lim-1 do
	begin
		for j:=1 to lim-i do
		begin
			if (v[j].legajo > v[j+1].legajo) then
			begin
				aux:=v[j];
				v[j]:=v[j+1];
				v[j+1]:=aux;
			end;
		end;
	end;
end;

procedure BBin_sede (var v:t_vector; buscado:string; var pos_:integer; lim:integer);
var
	pri,med,ult:integer;
begin
	buscado:='concepcion del uruguay';
	pri:=1;
	ult:=lim;
	pos_:=0;
	while (pos_=0) and (pri<=ult) do
	begin
		med:=(pri+ult) div 2;
		if (v[med].sede=buscado) then
			pos_:=med-1
			else
			if (v[med].sede > buscado) then
				ult:=med-1
			else
				pri:=med+1;
	end;
end;

procedure BBin_leg (var v:t_vector; buscado_leg:integer; var pos_:integer; lim:integer);
var
	pri,med,ult:integer;
begin
	buscado_leg:=42903;
	pri:=1;
	ult:=lim;
	pos_:=0;
	while (pos_=0) and (pri<=ult) do
	begin
		med:=(pri+ult) div 2;
		if (v[med].legajo=buscado_leg) then
			pos_:=med
			else
			if (v[med].legajo > buscado_leg) then
				ult:=med-1
			else
				pri:=med+1;
	end;
end;

procedure izq_der (var v:t_vector; lim:integer; pos_:integer; buscado:string);
begin
	while (v[pos_-1].sede = buscado) and (pos_ > 1) do
	begin
		pos_:=pos_-1;
	end;
	while (v[pos_].sede = buscado) and (pos_ <= lim) do
	begin
	 	listar_reg (v[pos_]);
	 	inc (pos_);
	 end;
end;

procedure c_empleados (var v:t_vector; var c_ex,c_ac,c_in:integer; lim:integer);
var
	i:integer;	
begin
	for i:= 1 to lim do
	begin
		case v[i].tareas of
			'extension': inc (c_ex);
			'academica': inc (c_ac);
			'investigacion': inc (c_in);
		end;
	end;
end;

// CUERPO PRINCIPAL

begin
	inicializar_v (v);
	cargar_v (v,lim);
	burbuja_fac (v,lim);
	writeln ('empleados CdelU:');
	BBin_sede (v,buscado,pos_,lim);
	if (pos_ <> 0) then
	begin
		izq_der (v,lim,pos_,buscado);
	end;
	burbuja_leg (v,lim);
	BBin_leg (v,buscado_leg,pos_,lim);
	if (pos_ <> 0) then
		begin
			write ('Tareas del empleado 42903: ');
			with v[pos_] do
			begin
				write (tareas);
			end;
		end;
	c_empleados (v,c_ex,c_ac,c_in,lim);
	writeln ('cantidad de empleados que realizan c/actividad: ');
	writeln ('extension: ',c_ex);
	writeln ('academica: ',c_ac);
	writeln ('investigacion: ',c_in);
end.