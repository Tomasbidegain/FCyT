Program facultades;

uses crt;

const
	n=4;

type
	t_empleados = record
		legajo: string;
		sede: string;
		tareas: string;
		facultad: string;
		apynom:string;
	end;

	t_vector = array [1..n] of t_empleados;

var
	empleado: t_empleados;
	vec: t_vector;
	cont_ex,cont_ac,cont_in: integer;
	lim,pos : word;
	buscado:string;

procedure inicializar_reg (var empleado:t_empleados);
begin
    with empleado do 
    begin
        legajo:='';
       	sede:='';
        tareas:='';
        facultad:='';
        apynom:='';
    end;
end;

procedure cargar_reg (var empleado:t_empleados);

begin
	with empleado do 
	begin
		textcolor(lightred);
		write('Numero de legajo: ');
		textcolor(white);
		readln(legajo);
		textcolor(lightred);
		write('Ingrese la sede: ');
		textcolor(white);
		readln(sede);
		textcolor(lightred);
		write('Ingrese las tareas que desarrolla: ');
		textcolor(white);
		readln(tareas);
		textcolor(lightred);
		write('Ingrese la facultad: ');
		textcolor(white);
		readln(facultad);
		textcolor(lightred);
		write('Ingrese apellido y nombre: ');
		textcolor(white);
		readln(apynom);
	end;
end;

procedure inicializar_vec(var vec:t_vector; var lim:word);
var
	i: word;
begin
	lim:=0;
	for i:= 1 to n do
		inicializar_reg(vec[i]);
end;

procedure cargar_vec(var vec:t_vector; var lim:word);
var 
	tecla:integer;
begin
	readln(tecla);
	clrscr;
	while (tecla <> 2) and (lim < n) do
	begin
		inc(lim);
		cargar_reg (vec[lim]);
		clrscr;
		textcolor(lightblue);
		writeln('1. Para cargar:');
		writeln('2. Para dejar de cargar.');
		write('#Opcion: ');
		textcolor(white);
		readln(tecla);
		clrscr;
	end;
end;

procedure burbuja (var vec:t_vector; lim:word);
var
   i, j: word;
   aux: t_empleados;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].facultad+vec[j].apynom > (vec[j+1].facultad+vec[j].apynom))then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure listar_reg(var empleado:t_empleados);
begin
	with empleado do
	begin
		writeln(legajo);
        writeln(sede);
        writeln(tareas);
        writeln(facultad);
        writeln(apynom);
    end;
end;

procedure listar_empleados_vec(var vec:t_vector; lim:word);
var
	i: word;
begin
	for i:= 1 to lim do
	begin
		listar_reg(vec[i]);
	end;
end;

procedure burbuja_sede (var vec:t_vector; lim:word);
var
   i, j: word;
   aux: t_empleados;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].sede > (vec[j+1].sede))then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure busqueda_bin_sede (var vec:t_vector; buscado:string; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].sede + vec[med].facultad = buscado) then
              pos:=med
           else
               begin
                    if (vec[med].sede + vec[med].facultad > buscado) then
                       ult:=med-1
                    else
                        pri:=med+1;
               end;
      end;
end;

procedure dere_izq(var vec: t_vector; pos:word; buscado:string;lim:word);

begin
	while (vec[pos-1].sede = buscado) and (pos > 1) do
	begin
		pos:= pos-1;
	end;

	while (vec[pos].sede = buscado) and (pos <= lim) do
	begin
		with vec[pos] do
		begin
			listar_reg(vec[pos]);
			inc(pos);
		end;
	end;
end;

procedure burbuja_legajo (var vec:t_vector; lim:word);
var
   i, j: word;
   aux: t_empleados;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].legajo > (vec[j+1].legajo))then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure bbin_legajo (var vec:t_vector; var buscado: string; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].legajo = buscado) then
              pos:=med
           else
               begin
                    if (vec[med].legajo > buscado) then
                       ult:=med-1
                    else
                        pri:=med+1;
               end;
      end;
end;

procedure cantidad_de_actividades(var vec:t_vector; var cont_ex:integer; var cont_ac:integer; var cont_in:integer;lim:word);
var 
	i:word;

begin
	for i := 1 to lim do
	begin
		if (vec[i].tareas = 'Extension') then
		begin
			inc (cont_ex);
		end
			else
			if (vec[i].tareas = 'Academica') then
			begin
				inc (cont_ac);
			end
				else
				if (vec[i].tareas = 'Investigacion') then
				begin
					inc (cont_in);
				end;
	end;
end;

//CUERPO PRINCIPAL
begin
	inicializar_vec (vec,lim);
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
	gotoxy(14,4);writeln('---------------------------');
	write('#Opcion: ');
	textcolor(white);
	cargar_vec (vec,lim);
	clrscr;
	burbuja (vec,lim);
	textcolor(lightred);
	writeln('Listado ordenado de empleados por facultad: ');
	textcolor(white);
	listar_empleados_vec(vec,lim);
	write('Ingrese sede a buscar: ');
	readln(buscado);
	busqueda_bin_sede (vec, buscado, pos, lim);
	if (pos <> 0) then
	begin
		writeln('Empleados que trabajan en la sede' , buscado , ': ');
		dere_izq (vec,pos,buscado,lim);
	end;
	writeln('Buscar N° legajo: ');
	readln(buscado);
	burbuja_legajo(vec,lim);
	bbin_legajo (vec, buscado, pos, lim);
	if (pos <> 0) then
	begin
		writeln('Tareas desarrolladas por el cliente cuyo legajo es: ', buscado);
		with vec[pos] do
			writeln(tareas);
	end
	else
	begin
	writeln('El empleado con el legajo 42903 no existe');
	end;
	cantidad_de_actividades(vec,cont_ex,cont_ac,cont_in,lim);
	textcolor(yellow); writeln('Cantidad de empleados por actividades:');
	textcolor (blue); write('Extension: ');
	textcolor (white);writeln(cont_ex);
	textcolor (red);write('Academicas: ');
	textcolor (white);writeln(cont_ac);
	textcolor (green);write('Investigacion: '); 
	textcolor (white);writeln (cont_in);
	readkey;
end.
