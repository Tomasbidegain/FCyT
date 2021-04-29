
unit unitclientes_tp;

interface

uses crt,registros,SubmenuCli,unitproyectos;

type 
	c_archivo = file of t_cliente;
var 
	cliente: c_archivo;
	lim,pos: word;

procedure abrir_cliente(var cliente: c_archivo);
procedure leer_cliente(var cliente:c_archivo; var reg_cliente: t_cliente; pos:word);
procedure escribir_cliente(var cliente:c_archivo; var reg_cliente: t_cliente);
procedure cerrar_cliente(var cliente:c_archivo);
procedure modificacion_cliente(var cliente:c_archivo);
procedure Alta_cliente(var cliente:c_archivo);
procedure bajas_clientes(var cliente: c_archivo);
procedure mostrar_clientes(var reg_cliente: t_cliente; var x:word; var y: word);
procedure mostrar_c(var reg_cliente: t_cliente; var cliente: c_archivo);
procedure ordenar(var cliente: c_archivo);
procedure p_contratados(var cliente:c_archivo);
procedure tabla_cliente(var x: word; var y:word);
procedure existe_cuit(var c_encontrado: boolean;var c: string; var cliente: c_archivo);
procedure tabla_contratados(var x:word; var y:word);
implementation

uses Validaciones;

procedure abrir_cliente(var cliente: c_archivo);
begin
	assign (cliente,'./Clientes.dat');
	{$I-} 
	reset (cliente);
	{$I-} 
	if IOResult <> 0 then
		rewrite(cliente);
end;

procedure leer_cliente(var cliente:c_archivo; var reg_cliente: t_cliente; pos:word);
begin
	seek(cliente,pos);
	read(cliente,reg_cliente);
end;

procedure escribir_cliente(var cliente:c_archivo; var reg_cliente: t_cliente);
begin
	seek(cliente,pos);
	write(cliente,reg_cliente);
end;

procedure cerrar_cliente(var cliente:c_archivo);
begin
	close (cliente);
end;

procedure existe_cuit(var c_encontrado: boolean;var c: string; var cliente: c_archivo);
begin
	c_encontrado := False;
    seek(cliente,0);
	while not eof (cliente) do
	begin
		read(cliente,reg_cliente);
        if (reg_cliente.cuit = c) then
           	c_encontrado := true;
    end;
end;

procedure tabla_contratados(var x:word; var y:word);
begin
	textcolor(red);
	gotoxy(x+15,4);write('------------------------------------------------------------------------------');
	gotoxy(x+15,6);write('------------------------------------------------------------------------------');
	gotoxy(x+15,y+8);write('------------------------------------------------------------------------------');
	gotoxy(x+15, 5);write('|');
	gotoxy(x+15, 5);write('|');
	gotoxy(x+43, 5);write('|');
	gotoxy(x+67, 5);write('|');
	gotoxy(x+92, 5);write('|');
	gotoxy(x+92, y+7);write('|');
	gotoxy(x+15, y+7);write('|');
	gotoxy(x+43, y+7);write('|');
	gotoxy(x+44, y+7);write('$ ');
	gotoxy(x+67, y+7);write('|');
	textcolor(white);
	gotoxy(x+16, 5);write('           Cuit            ');
	gotoxy(x+44, 5);write('    Costo invertido    ');
	gotoxy(x+68, 5);write('  Proyectos contratados ');
end;

procedure tabla_cliente(var x: word; var y:word);
begin
	x:=10;
	y:=5;
	textbackground(black);clrscr;
	textcolor(4);
	gotoxy(x+15,y-1);write('----------------------------------------------------------------------------------------------------------------');
	gotoxy(x+15,y+1);write('----------------------------------------------------------------------------------------------------------------');
	gotoxy(x+36,y+2);write('| ');
	gotoxy(x+50,y+2);write('|');
	gotoxy(x+64,y+2);write('|');
	gotoxy(x+96,y+2);write('|');
	gotoxy(x+126,y+2);write('|');
	gotoxy(x+15, y+2);write('|');
	gotoxy(x+15,y+3);write('----------------------------------------------------------------------------------------------------------------');
	textcolor(green);
	gotoxy(x+15,y);textcolor(red);write('|');textcolor(green);write('    Razon Social    ');textcolor(red);write('|');
	gotoxy(x+37,y);textcolor(green);write('    Cuit     ');textcolor(red);write('|');
	gotoxy(x+52,y);textcolor(green);write('  Telefono  ');textcolor(red);write('|');
	gotoxy(x+66,y);textcolor(green);write('          Domicilio           ');textcolor(red);write ('|');
	gotoxy(x+98,y);textcolor(green);write('            Email           ');textcolor(red);write('|');
end;

procedure Alta_cliente(var cliente: c_archivo); {CARGAMOS DATOS}
var
	valida,valido_e,valida_c,c_encontrado: boolean;
	cuit_aux: string;
	x,y: word;

begin
	valida_c := false;
	with reg_cliente do
	begin
		abrir_cliente(cliente);
		tabla_cliente(x,y);
		vigente:=true;
		textcolor(white);
		gotoxy(x+16,y+2);read(razon_social);
		razon_social[1] := upcase(razon_social[1]);
		gotoxy(x+37,y+2);readln(cuit_aux);
		validar_cuit(cuit_aux, valida_c);
		if (valida_c = false) then
		begin
			repeat
				gotoxy(x+37,y+2);write('             ');
				gotoxy(x+37,y+2);readln(cuit_aux);
				validar_cuit(cuit_aux, valida_c);
			until (valida_c = true);
		end
		else
		if (valida_c = true) then
		begin
			existe_cuit(c_encontrado, cuit_aux, cliente);
				if c_encontrado then
				begin
					repeat
   						gotoxy(x+37,y+2);write('             ');
						gotoxy(x+37,y+2);readln(cuit_aux);
						existe_cuit(c_encontrado, cuit_aux, cliente);
					until (c_encontrado = false);
          		end;
        end;
        reg_cliente.cuit := cuit_aux;
		gotoxy(x+52,y+2);readln(telefono);
		validar_telefono(telefono, valida);
		if (valida = false) then
		begin
			repeat
				gotoxy(x+52,y+2);write('           ');
				gotoxy(x+52,y+2);readln(telefono);
				validar_telefono(telefono, valida);
			until (valida = true);	
		end;
		gotoxy(x+66,y+2);readln(domicilio);
		upcase(domicilio[1]);
		gotoxy(x+98,y+2);readln(email);
		validar_email(email,valido_e,x,y);
	end;
		seek(cliente,fileSize(cliente));
		write(cliente,reg_cliente);
		cerrar_cliente(cliente);
end;

procedure modificacion_cliente(var cliente: c_archivo);
var
	cuit_buscado:string;
	encontrado,salida,valido_e,valida: boolean;
	opcion:char;
	x,y:word;
begin
	tabla_cliente(x,y);
	encontrado:=false;
	abrir_cliente(cliente); {Abro el archivo cliente}
	textcolor(red);
	gotoxy(25,1);writeln('Ingrese el cuit a buscar:');
	textcolor(white);
	gotoxy(25,2);readln(cuit_buscado); {leo el cuit a buscar}
	with reg_cliente do
	begin
		while not eof(cliente) and (encontrado = false) do
		begin
			read(cliente,reg_cliente);
			if (cuit_buscado = reg_cliente.cuit) and (vigente = true) then
			begin
				encontrado:=true;
			end;
		end;
			if (encontrado = true) then
			begin

				repeat
					salida:= false;
					tabla_cliente(x,y);
					textcolor(white);
					gotoxy(x+16,y+2);write(razon_social);
					gotoxy(x+37,y+2);write(cuit);
					gotoxy(x+52,y+2);write(telefono);
					gotoxy(x+66,y+2);write(domicilio);
					gotoxy(x+98,y+2);write(email);
					vigente := true;
					gotoxy(x+16,y+5);write('|  1. Razon social  |  2. Telefono  |  3. Domicilio  |  4. Email  |  5. Aceptar  |');
					gotoxy(x+16,y+7); write('# Opcion: ');
					opcion := readkey();
				    case opcion of
					 '1':begin
					 		gotoxy(x+16, y+2);write('                    ');
					 		gotoxy(x+16,y+2);readln(razon_social);
					 		upcase(reg_cliente.razon_social[1]);
					 		seek(cliente, filePos(cliente)-1);
							write(cliente,reg_cliente);
					  	end;
					 '2':begin
							gotoxy(x+52,y+2);write('            ');
							gotoxy(x+52,y+2);readln(telefono);
							validar_telefono(reg_cliente.telefono, valida);
							if (valida = false) then
							begin
								repeat
									gotoxy(x+52,y+2);write('            ');
									gotoxy(x+52,y+2);readln(reg_cliente.telefono);
									validar_telefono(reg_cliente.telefono, valida);
								until (valida = true);	
							end;
							seek(cliente, filePos(cliente)-1);
							write(cliente,reg_cliente);
						end;					 
					 '3':begin
						 	gotoxy(x+66,y+2);write('                              ');
					  		gotoxy(x+66,y+2);readln(domicilio);
							seek(cliente, filePos(cliente)-1);
							write(cliente,reg_cliente);
					  	end;
					 '4':begin
					 		gotoxy(x+98,y+2);write('                            ');
					  		gotoxy(x+98,y+2);readln(email);
							validar_email(reg_cliente.email,valido_e,x,y);
							seek(cliente, filePos(cliente)-1);
							write(cliente,reg_cliente);
					  	end;
					 '5':begin
					 		Salida:= true; 		
					  	end;
					 
					end;
			  	Until (Salida=true);
				clrscr;
			end
			else
			if not vigente then
			begin
				clrscr;
				textcolor(red);
				writeln('El cliente fue dado de baja.');
				readkey();
			end
			else
			begin
				clrscr;
				writeln;
				textcolor(red);
				writeln('EL cuit que acaba de ingresar es incorrecto.');
				readkey();
			end;
	end;
	cerrar_cliente(cliente);
	submenuClien();
end;

procedure bajas_clientes(var cliente: c_archivo);
var
	op:char;
	x,y:word;
 	cuit_buscado: string;
 	encontrado: boolean;
begin
	clrscr;
	abrir_cliente(cliente);
	textbackground(blue);clrscr;
	textcolor(black);
	tabla_cliente(x,y);
	textcolor(white);
	gotoxy(25,1);write('Ingrese el cuit : ');
	gotoxy(25,2);readln(cuit_buscado);
	encontrado:=false;
	with reg_cliente do
	begin
	    while not eof(cliente) and (encontrado = false)do
	    begin
	    	read(cliente,reg_cliente);
			if (cuit_buscado = reg_cliente.cuit) then
				encontrado:=true;
		end;
			if (encontrado = true) and (vigente) then
			begin
				tabla_cliente(x,y);
				textcolor(white);
				gotoxy(x+16,y+2);write(razon_social);
				gotoxy(x+37,y+2);write(cuit);
				gotoxy(x+52,y+2);write(telefono);
				gotoxy(x+66,y+2);write(domicilio);
				gotoxy(x+98,y+2);writeln(email);
			   	gotoxy(x+16,y+5);writeln('Esta seguro que quiere dar de baja el cliente?');
			   	gotoxy(x+16,y+6);writeln(' S/N');
				op := readkey;
				case upcase(op) of
					'S':begin
							vigente := false;
						end;
					'N': submenuClien();
				end;	
	   		end
	   		else 
	   		begin
	   			clrscr;
	   			textcolor(red);
	   			writeln('El cuit que ha ingresado no es correcto o el cliente fue dado de baja.');
	   			readkey();
	   		end;
	end;
	seek(cliente, filepos(cliente)-1);
	write(cliente,reg_cliente);
	close(cliente);
end;

procedure mostrar_clientes(var reg_cliente: t_cliente; var x:word; var y: word);
begin
		textcolor(red);
		gotoxy(x+15,4);write('----------------------------------------------------------------------------------------------------------------');
		gotoxy(x+15,6);write('----------------------------------------------------------------------------------------------------------------');
		gotoxy(x+36,y+7);write('| ');
		gotoxy(x+50,y+7);write('|');
		gotoxy(x+64,y+7);write('|');
		gotoxy(x+96,y+7);write('|');
		gotoxy(x+126,y+7);write('|');
		gotoxy(x+15, y+7);write('|');
		gotoxy(x+15,y+8);write('----------------------------------------------------------------------------------------------------------------');
		textcolor(green);
		gotoxy(x+15,5);textcolor(red);write('|');textcolor(green);write('    Razon Social    ');textcolor(red);write('|');
		gotoxy(x+37,5);textcolor(green);write('    Cuit     ');textcolor(red);write('|');
		gotoxy(x+52,5);textcolor(green);write('  Telefono  ');textcolor(red);write('|');
		gotoxy(x+66,5);textcolor(green);write('          Domicilio           ');textcolor(red);write ('|');
		gotoxy(x+98,5);textcolor(green);write('            Email           ');textcolor(red);write('|');
		textcolor(white);
		gotoxy(x+16,y+7);write(reg_cliente.razon_social);
		gotoxy(x+37,y+7);write(reg_cliente.cuit);
		gotoxy(x+52,y+7);write(reg_cliente.telefono);
		gotoxy(x+66,y+7);write(reg_cliente.domicilio);
		gotoxy(x+98,y+7);write(reg_cliente.email);
end;

procedure mostrar_c(var reg_cliente: t_cliente; var cliente: c_archivo);
var
	x,y:word;
	cont_enter:integer;
begin
	cont_enter:=0;
	abrir_cliente(cliente);
	clrscr;
	textbackground(black);clrscr;
	x:=10;
	y:=0;
	seek(cliente,0);
	while not eof (cliente) do
	begin
        read(cliente,reg_cliente);
       	if (reg_cliente.vigente = true) then
       	begin
       		mostrar_clientes(reg_cliente,x,y);
       		y:= y+2; 
       		cont_enter:= cont_enter + 1;
       		if (cont_enter = 15) then
       		begin
       			gotoxy(x+2,y+10);write('== Presione enter para seguir viendo los proyectos. ==');
       			readkey;
       			x:=10;
				y:=0;
				clrscr;
			end;
       	end;
    end;
    readkey;
    cerrar_cliente(cliente);
    submenuClien();
end;

procedure ordenar (var cliente: c_archivo);
	var
	reg1,reg2, aux : t_cliente;
    i, j: word;
begin
	abrir_cliente(cliente);
	i:=0;
	j:=0;
	for i := 0 to filesize(cliente)-1  do
	begin
		seek(cliente,i);
	 	read(cliente,reg1);
	 	for j := (filesize(cliente)-1) downto (i + 1) do
		begin
	    	seek(cliente,j);
	    	read(cliente,reg2);
	    	if (reg1.razon_social > reg2.razon_social) then
	    	begin
	       		aux := reg1;
	       		reg1 := reg2;
	       		reg2 := aux;
	       		seek(cliente,i);
	       		write(cliente,reg1);
	       		seek(cliente,j);
	       		write(cliente,reg2);
	    	end;
	 	end;
	end;
	cerrar_cliente(cliente);
end;

procedure p_contratados(var cliente:c_archivo);
var
	ac_costo:Real;
	cont_p,x,y: word;
	aux,valida_c :boolean;
	cuit_aux: string;
	cont_enter:integer;
begin
	cont_enter := 0;
	x:=10;
	y:=0;
	cont_p:=0;
	ac_costo:=0;
	aux:= false;
	abrir_proyecto(f_proyecto);
	seek (f_proyecto,0); 
	textcolor(10);
	gotoxy(x+1,4);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+1,6);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+38,y+7);write('|$ ');
	gotoxy(x+55,y+7);write('|');
	gotoxy(x+70,y+7);write('|');
	gotoxy(x+93,y+7);write('|');
	gotoxy(x+114,y+7);write('|');
	gotoxy(x+132,y+7);write('|');
	gotoxy(x+1,y+8);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x,5);write('|   ');textcolor(5);write('ID    ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(x,y+7);textcolor(10);write('| ');textcolor(white);write('0');textcolor(10);write('      |');
	gotoxy(x+11,5);textcolor(5);write('          Titulo           ');textcolor(10);write('|');
	gotoxy(x+39,5);write('     Costo      ');textcolor(10);write('|');
	gotoxy(x+57,5);write('    Cuit     ');textcolor(10);write('|');
	gotoxy(x+71,5);write('      Director        ');textcolor(10);write('|');
	gotoxy(x+94,5);write('  Fecha de entrega  ');textcolor(10);write('|');
	gotoxy(115+x,5);write('   Exporta(S/N)  ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(11,10);write('Ingrese el cuit del cliente para saber los proyectos que contrato: ');gotoxy(11,11);read(cuit_aux);
	validar_cuit(cuit_aux, valida_c);
	if (valida_c = false) then
	begin
		repeat
			gotoxy(25,2);writeln('              ');
			textcolor(white);
			gotoxy(25,2);readln(cuit_aux);
			validar_cuit(cuit_aux, valida_c);
		until (valida_c = true);
	end;
	clrscr;
 	seek (f_proyecto,0);
 	while not eof(f_proyecto) do
 	begin
 		read (f_proyecto,reg_proyecto);
 		if (cuit_aux = reg_proyecto.cuit) then
 		begin
 			cont_enter:= cont_enter + 1;
       		mostrar_proyectos_t(x,y);
 			inc(cont_p);
 			y:=y+2;
 			ac_costo := (ac_costo + reg_proyecto.costo);
 			aux:=true;
 			if (cont_enter = 15) then
       		begin
		       	gotoxy(x+2,y+10);write('== Presione enter para seguir viendo los proyectos. ==');
		       	readkey;
		       	x:=10;
				y:=0;
				clrscr;
		    end;
 		end;
 	end;
	if (aux = true) then
	begin
		writeln();
		writeln();
		writeln();
		gotoxy(11,y+8);writeln('Presione enter para ver el costo total invertido y la cantidad de proyectos que contrato.');
		readkey();
		clrscr;
		x:=10;
		y:=0;
		tabla_contratados(x,y);
		gotoxy (x+18,7);write(cuit_aux);
		gotoxy (x+46,7);write(ac_costo:2:0);
		gotoxy (x+69,7);write(cont_p);
		readkey();
	end
	else 
	if (aux = false) then
	begin
		textcolor(black);
		writeln('El cliente con el cuit ', cuit_aux,' no tiene proyectos contratados');
		readkey();
	end;
	cerrar_proyecto(f_proyecto);
end;
end.