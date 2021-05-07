Program empresas;
uses crt;

const
	n = 9;


type
	t_cadena = string;
	t_empresa = record
		apynom: string;
		cuidad: string;
		Clien_esp: string;
		monto_t: real;
		total_deuda:real;
	end;

	t_vector = array [1..n] of t_empresa;

var
	empre: t_empresa;
	vec: t_vector;
	buscado: t_cadena;
	lim,pos:word;
	cont_colon,cont_esp:integer;
	ac_deudas, porcentaje:real;

procedure inicializar_reg (var empre:t_empresa);
begin
    with empre do 
    begin
       	apynom:='';
        cuidad:='';
        Clien_esp:='';
        monto_t:=0;
        total_deuda:=0;
    end;
end;

procedure cargar_reg(var empre: t_empresa);
begin
	with empre do
	begin
		textcolor(lightred);
		write('Ingrese su apellido y nombre: ');
		textcolor(white);
		readln(apynom);
		textcolor(lightred);
		write('Ingrese la cuidad en la que vive:');
		textcolor(white);
		readln(cuidad);
		textcolor(lightred);
		write('Ingrese si es cliente especial o no:');
		textcolor(white);
		readln(Clien_esp);
		textcolor(lightred);
		write('Ingrese el monto total de compra acumulada en 2018: ');
		textcolor(white);
		readln(monto_t);
		textcolor(lightred);
		write('Ingrese el total de deudas: ');
		textcolor(white);
		readln(total_deuda);
	end;
end;
procedure inicializar_vec(var vec:t_vector);
var
	i: word;
begin
	for i:= 1 to n do
	inicializar_reg(vec[i]);
end;

procedure cargar_vec(var vec:t_vector; lim:word);
var
	tecla: char;
begin
	readln(tecla);
	clrscr;
	while (tecla <> '2') and (lim <= n) do
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

procedure listar_reg(var empre:t_empresa);
begin
	with empre do
	begin
		writeln(apynom);
        writeln(cuidad);
        writeln(Clien_esp);
        writeln(monto_t);
      	writeln(total_deuda);
    end;
end;

procedure listar_vec(var vec:t_vector);
var
	i: word;
begin
	for i:= 1 to n do
	begin
		listar_reg(vec[i]);
	end;
end;

procedure verifica(var vec:t_vector; lim:word);
var
	i,j: word;
	aux: t_empresa;

begin
	for i:= 1 to lim-1 do
	begin
		for j:= 1 to lim-i do
		begin
			if (vec[j].apynom) > (vec[j+1].apynom) then
			begin
				aux:= vec[j];
				vec[j]:= vec[j+1];
				vec[j+1]:= aux;
			end;
		end;
	end;
end;	

procedure bbin_verifica(var vec:t_vector; buscado:string; var pos:word; lim:word);
var
	pri,med,ult: word;
begin
	pri:=1;
	ult:=lim;
	pos:=0;
	while (pos<=ult) and (pos=0) do
	begin
		med:=(pri+ult) div 2;
		if (vec[med].apynom = buscado) then
		begin
			pos:=med;
		end
		else 
		if (vec[med].apynom > buscado) then
		begin
			pos:=med-1;
		end
		else
		begin
			pos:=med+1;
		end;
	end;
end;
procedure burbuja (var vec:t_vector; lim:word);

var
   i, j: word;
   aux: t_empresa;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].cuidad > vec[j+1].cuidad) then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure busqueda_bin (var vec:t_vector; buscado:string; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].cuidad = buscado) then
              pos:=med
           else
               begin
                    if (vec[med].cuidad > buscado) then
                       ult:=med-1
                    else
                        pri:=med+1;
               end;
      end;
end;

procedure derecha_izq(var vec:t_vector; buscado:string; var pos:word; lim:word;var cont_colon:integer);
begin
	cont_colon:=1;
	while (vec[pos-1].cuidad = buscado) and (pos > 1) do
	begin
		pos:= pos-1;
	end;	

	while (vec[pos].cuidad = buscado) and (pos <= lim) do
	begin
		listar_reg(vec[pos]);
		inc (pos);
		inc(cont_colon)
	end;
end;

procedure burbuja_clientes_especiales(var vec:t_vector; lim: word);
var
	i,j:word;
	aux: t_empresa;

begin
	for i:= 1 to lim-1 do
	begin
		for j:=1 to lim-i do
		begin
			if (vec[j].Clien_esp) > (vec[j+1].Clien_esp) then
			begin
				aux:= vec[j];
				vec[j]:= vec[j+1];
				vec[j+1]:= aux;
			end;
		end;
	end;
end;

procedure bbin_clientes_especiales(var vec:t_vector; buscado:string; var pos: word; lim:word);
var
	pri,med,ult:word;

begin
	pri:=1;
	ult:=lim;
	pos:=0;
	while (pos=0) and (pos <= lim) do
	begin
		med:=(pri+ult) div 2;
		if (vec[med].Clien_esp = buscado) then
		begin
			pos:=med;
		end
		else
			if (vec[med].Clien_esp > buscado) then
			begin
				ult:= med-1;
			end
			else
			begin
				pri:=med+1;
			end;
	end;
end;

procedure der_izq(var vec:t_vector; buscado:string; var pos:word; lim:word; var cont_esp:integer;var ac_deudas:real);
begin
	ac_deudas:=0;
	while (vec[pos-1].Clien_esp = buscado) and (pos > 1) do
	begin
		pos:= pos-1;
	end;
	while (vec[pos].Clien_esp = buscado) and (pos <= lim) do
	begin
		with vec[pos] do
		begin
			inc(cont_esp);
			ac_deudas:=ac_deudas+total_deuda;
			inc(pos);
		end;
	end;
end;

procedure bur_buscar_cliente(var vec:t_vector; lim:word);
var
	i,j:integer;
	aux:t_empresa;

begin
	for i:= 1 to lim-1 do
	begin
		for j:= 1  to lim-i do
		begin
			if (vec[j].apynom > vec[j+1].apynom) then
			begin
				aux:= vec[j];
				vec[j]:= vec[j+1];
				vec[j+1]:= aux;
			end;
		end;
	end;
end;

procedure bbin_cliente(var vec:t_vector;buscado:string; var pos:word; lim:word);
var
	pri,med,ult: word;

begin
	pri:=1;
	ult:=lim;
	pos:=0;
	while (pos=0) and (pos <= lim) do
	med:=(pri+ult) div 2;
	begin
		if (vec[med].apynom = buscado) then
		begin
			pos:=med;
		end
		else
			if (vec[med].apynom > buscado) then
			begin
				ult:=med-1
			end
			else
				pri:= med+1;
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
	lim:=0;
	cargar_vec(vec,lim);
	verifica(vec,lim);
	writeln('Para cargar un nuevo cliente debe verificar que no exista en el sistema.');
	writeln('Ingrese el cliente a buscar: ');
	readln(buscado);
	bbin_verifica(vec,buscado,pos, lim);
	if (pos <> 0) then
	begin
		cargar_reg(empre);
	end
	else
	begin
		writeln('El cliente ya existe.');
	end;
	burbuja(vec,lim);
	writeln('Ingrese una cuidad para saber los clientes que le corresponden a dicha cuidad: ');
	readln(buscado);
	busqueda_bin (vec, buscado, pos, lim);
	if (pos <> 0) then
	begin
		derecha_izq (vec,buscado,pos,lim,cont_colon);
		writeln('La cantidad de empleados en la cuidad ',buscado,' es de ', cont_colon);
	end
	else 
	begin
		writeln('No existe clientes de la cuidad ',buscado);
	end;
	burbuja_clientes_especiales(vec,lim);
	buscado:='Si';
	bbin_clientes_especiales(vec, buscado, pos, lim);
	if (pos <> 0 ) then
	begin
		 der_izq(vec,buscado,pos,lim,cont_esp,ac_deudas);
		 writeln('Cantidad de clientes especiales: ',cont_esp);
		 writeln('Total de deudas de los clientes especiales: ', ac_deudas:2:0);
		 porcentaje:= (cont_esp / ac_deudas) * 100;
		 writeln('Porcentaje de deudas: ', porcentaje);
	end;
	bur_buscar_cliente(vec,lim);
	writeln('Ingrese un cliente a buscar: ');
	readln(buscado);
	bbin_cliente(vec,buscado,pos,lim);
	if (pos <> 0 ) then
	begin
		with vec[pos] do
		begin
			writeln(buscado,' existe en el sistema.');
			writeln('Compras de ',buscado,' en 2018: ', monto_t:2:0);
		end;
	end
	else
		writeln(buscado,' no existe.');
	readkey;
end.