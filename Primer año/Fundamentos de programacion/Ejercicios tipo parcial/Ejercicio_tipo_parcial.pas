program cobradores;

uses crt;

const
	n = 5;

type
	t_cob = record
		cod_cobrador : integer;
		barrio: string;
		apynom_socio: string;
		cuota: real;
	end;

	t_vector = array[1..n] of t_cob;

var
	cob: t_cob;
	vec: t_vector;
	lim: integer;
	buscado:string;
	ac_cuota:real;
	pos:word;

procedure inicializar_reg(var cob: t_cob);

begin
	with cob Do
	begin
		cod_cobrador :=0;
		barrio:='';
		apynom_socio:='';
		cuota:=0;
	end;
end;

procedure cargar_reg(var cob: t_cob);

begin
	with cob do
	begin
		textcolor(lightred);
		write('Ingrese el codigo de cobrador:');
		textcolor(white);
		readln(cod_cobrador);
		textcolor(lightred);
		write('Ingrese el barrio:');
		textcolor(white);
		readln(barrio);
		textcolor(lightred);
		write('Ingrese el apellido y nombre del socio:');
		textcolor(white);
		readln(apynom_socio);
		textcolor(lightred);
		write('Ingrese la cuota: ');
		textcolor(white);
		readln(cuota);
	end;
end;

procedure listar_reg(var cob:t_cob);
begin
	with cob do
	begin
		textcolor(lightred);
		writeln('Codigo del cobrador: ');
		textcolor(white);
		writeln(cod_cobrador);
		textcolor(lightred);
		write('Barrio: ');
		textcolor(white);
		writeln(barrio);
		textcolor(lightred);
		write('Apellido y nombre: ');
		textcolor(white);
		writeln(apynom_socio);
		textcolor(lightred);
		write('Cuota: ');
		textcolor(white);
		writeln(cuota:2:0);
	end;
end;
procedure inicializar_vec(var vec: t_vector);

var
	i: integer;
begin
	for i:= 1 to n do
	begin
		inicializar_reg(vec[i]);
	end;
end;

procedure cargar_vec(var vec: t_vector; var lim:integer);
var
	tecla: string;

begin
	readln(tecla);
	clrscr;
	lim:=0;
	while (lim < n) and (tecla <> '2') do
	begin
		inc (lim);	
		cargar_reg(vec[lim]);
		clrscr;
		textcolor(lightblue);
		writeln('1. Para cargar:');
		writeln('2. Para dejar de cargar.');
		write('#Opcion: ');
		textcolor(white);
		read(tecla);
		clrscr;
	end;	
end;

procedure listar_vec(var vec:t_vector);
var
	i:word;
begin
	for i:= 1 to lim do 
	begin
		listar_reg(vec[i]);
	end;
end;

procedure burbuja_barrio_cliente (var cob:t_cob; var vec:t_vector; lim:integer);
var
   i, j: word;
   aux: t_cob;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].barrio + vec[j].apynom_socio) > (vec[j+1].barrio + vec[j+1].apynom_socio) then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure listar_barrio_y_cliente(var cob:t_cob; lim:word);
var
	i: Integer;

begin
	for i:= 1 to lim do
	begin
		listar_reg(vec[i]);
	end;
end;

procedure burbuja_barrio_puerto (var cob:t_cob; var vec:t_vector; lim:integer);
var
   i, j: word;
   aux:t_cob;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].barrio) > (vec[j+1].barrio) then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure busqueda_bin_puerto(var vec:t_vector;var buscado:string; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].barrio = buscado) then
              pos:=med
           else
               begin
                    if (vec[med].barrio > buscado) then
                       ult:=med-1
                    else
                        pri:=med+1
               end;
      end;
end;

procedure dere_izq(var vec: t_vector;var ac_cuota:real; pos:word; var buscado:string;lim:word);

begin
	ac_cuota:=0;
	while (vec[pos-1].barrio = buscado) and (pos > 1) do
	begin
		pos:= pos-1;
	end;

	while (vec[pos].barrio = buscado) and (pos <= lim) do
	begin
		with cob (vec[pos]) do
		begin
			ac_cuota:=ac_cuota + cuota;
			inc(pos);
		end;
	end;
end;

procedure clientes_al(var vec:t_vector; lim:word; buscado:string);
var
	i:integer;
	aux: string;

begin
	for i:= 1 to lim do
	begin
		aux:=copy(vec[i].apynom_socio,1,2);
		if (aux = buscado) then
		begin
			writeln('Listado de los clientes que empiecen con "', buscado,'".');
			listar_reg(vec[i]);
		end
		else 
			writeln('No hay apellido que comiencen con "', buscado,'".');
	end;
end;

procedure burbuja_cobrador(var cob:t_cob; var vec:t_vector; lim:integer);
var
   i, j: word;
   aux: t_cob;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].cod_cobrador) > (vec[j+1].cod_cobrador) then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure listado_cobrador(var vec:t_vector;var cob:t_cob;lim:word);
var
	i: word;
begin
	for i:= 1 to lim do
	begin
		with cob do
		begin
			writeln(cod_cobrador);
			writeln(cuota:2:0);
		end;
	end;
end;

begin
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
burbuja_barrio_cliente (cob,vec,lim);
textcolor(lightred);
writeln('Listado ordenado por barrio y cliente: ');
textcolor(white);
listar_barrio_y_cliente(cob, lim);
burbuja_barrio_puerto (cob,vec,lim);
write('Ingrese el barrio a buscar: ');
readln();
readln(buscado);
busqueda_bin_puerto(vec,buscado,pos,lim);
if (pos <> 0) then
begin
	dere_izq(vec,ac_cuota,pos,buscado,lim);
	textcolor(lightred);
	writeln('Total recaudado en el barrio ',buscado,' es: ', ac_cuota:2:0);
	textcolor(white);
end;
write('Ingrese las primeras 2 letras de un apellido: ');
readln(buscado);
clientes_al(vec, lim, buscado);
burbuja_cobrador(cob,vec,lim);
writeln('Listado ordenado por codigo de cobrador,con el monto a cobrar: ');
listado_cobrador(vec,cob,lim);
readkey;
end.
