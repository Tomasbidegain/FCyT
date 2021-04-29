unit unitproyectos;

interface 

uses crt,registros,sysutils,Validaciones,unit_menu_principal;

type 
	//archivo
	fichero_proyec = file of t_proyec;

var
	lim,pos: word;
	f_proyecto: fichero_proyec;
	id_buscado:word;
	cont_id:integer;
	carga:boolean;

//interfaz de procedimientos
procedure abrir_proyecto(var f_proyecto:fichero_proyec);
procedure leer_proyecto(var f_proyecto:fichero_proyec);
procedure escribir_proyecto(var f_proyecto:fichero_proyec; var reg_proyecto: t_proyec);
procedure cerrar_proyecto(var f_proyecto:fichero_proyec);
procedure s_n(var carga:boolean);
procedure Alta_Proyecto(var f_proyecto:fichero_proyec);
procedure modificacion_proyectos(var f_proyecto:fichero_proyec; var id_buscado:word);
procedure bajas(var f_proyecto: fichero_proyec);
procedure ordenar_titulo(var f_proyecto:fichero_proyec);
procedure mostrar_proyectos_t(var x:word; var y:word);
procedure rango_de_fechas(var f_proyecto:fichero_proyec);
procedure mostrar_p(var f_proyecto:fichero_proyec);
procedure validacion(var d_i:integer; var m_i: integer ;var a_i: integer ;var d_f: integer;var m_f: integer; var a_f:integer );
procedure tabla (var x:word; var y:word);
implementation

uses 
	submenuPro,SubmenuConsultas,unitclientes_tp;
//implementacion de procedimientos
procedure abrir_proyecto(var f_proyecto: fichero_proyec);
begin
	assign (f_proyecto, 'Proyectos.dat'); {Asigna el alias del archivo y guarda el archivo con extension .dat}
	{$I-} //Desabilita los mensajes de error
	reset(f_proyecto); {Apertura del archivo en modo de lectura y escritura}
	{$I+}
	if IOResult <> 0 then {Si IOResult es diferente de 0 quiere decir que hubo un error en la apertura}
		rewrite(f_proyecto); {Crea el archivo si no existe}
end;

procedure leer_proyecto(var f_proyecto:fichero_proyec);
begin
	seek(f_proyecto,pos);{Nos permite posicionar el puntero en la posicion deseada}
	read(f_proyecto,reg_proyecto);{Para leer datos de un archivo}
end;

procedure escribir_proyecto(var f_proyecto:fichero_proyec; var reg_proyecto: t_proyec);
begin
	seek(f_proyecto,fileSize(f_proyecto)); {Se posiciona al final del archivo}
	write(f_proyecto,reg_proyecto)	{Guarda el registro en el archivo en la ultima posicion}
end;

procedure cerrar_proyecto(var f_proyecto:fichero_proyec);
begin
	close (f_proyecto); {Cierra el archivo}
end;
  
procedure s_n(var carga:boolean);
var
	op : string;
begin
	op:='';
	read(op);
	case upcase(op) of
		'S': carga:=true;
		'N': carga:=false;
	end;
end;

procedure tabla(var x: word; var y:word);
begin
	x:=10;
	y:=5;
	textbackground(black);clrscr;
	textcolor(10);
	gotoxy(x+1,y-1);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+1,y+1);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+38,y+2);write('|');textcolor(5);write('$ ');
	textcolor(10);
	gotoxy(x+55,y+2);write('|');
	gotoxy(x+70,y+2);write('|');
	gotoxy(x+93,y+2);write('|');
	gotoxy(x+114,y+2);write('|');
	gotoxy(x+132,y+2);write('|');
	gotoxy(x+1,y+3);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x,y);textcolor(10);write('|   ');textcolor(5);write('ID    ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(x,y+2);textcolor(10);write('| ');textcolor(white);write(reg_proyecto.id_proyecto);textcolor(10);write('      |');
	gotoxy(x+11,y);textcolor(5);write('          Titulo           ');textcolor(10);write('|');
	gotoxy(x+39,y);textcolor(5);write('     Costo      ');textcolor(10);write('|');
	gotoxy(x+57,y);textcolor(5);write('    Cuit     ');textcolor(10);write('|');
	gotoxy(x+71,y);textcolor(5);write('      Director        ');textcolor(10);write('|');
	gotoxy(x+94,y);textcolor(5);write('  Fecha de entrega  ');textcolor(10);write('|');
	gotoxy(115+x,y);textcolor(5);write('   Exporta(S/N)  ');textcolor(10);write('|');
end;

procedure Alta_Proyecto(var f_proyecto:fichero_proyec); {CARGAMOS DATOS}
var
	exportacion,op:char;
	bisiesto, valida_c:boolean;
	aux: LongInt;
    cont_id: Longint;
    reg_aux:t_proyec;
    x,y:word;
begin
	x:=10;
	y:=5;
	abrir_proyecto(f_proyecto); {Se abre el proyecto}
	with reg_proyecto do
	begin
		id_proyecto:=0;
		aux := 0;
        Seek(f_proyecto,0);  {Posicionamos el puntero en la posicion 0}
        while not EOF(f_proyecto) do {Mientras no sea el final del archivo}
        begin
            Read(f_proyecto, reg_aux);
            if (reg_aux.id_proyecto > aux) then    {Generamos el ID}
            	aux := (reg_aux.id_proyecto);
        end;
        cont_id := aux + 1;
        id_proyecto:= cont_id; 
		tabla(x,y);
		textcolor(white);
		gotoxy(x+11,y+2);readln(titulo);
		titulo_mayus(reg_proyecto);
		gotoxy(x+41,y+2);readln(costo);
		gotoxy(x+56,y+2);readln(cuit);
		validar_cuit(cuit, valida_c);
		if not valida_c then
		begin
			repeat
				gotoxy(x+56,y+2);write('             ');
				gotoxy(x+56,y+2);readln(cuit);
				validar_cuit(cuit, valida_c);
			until (valida_c = true);
			end;
		vigente:= true;
		gotoxy(x+72,y+2);readln(director);
		textcolor(5);
		gotoxy(x+97,y+2);write('/');
		textcolor(white);
		gotoxy(x+95,y+2);readln(dia);
		gotoxy(x+98,y+2);readln(mes);
		textcolor(5);
		gotoxy(x+100,y+2);write('/');
		textcolor(white);
		gotoxy(x+101,y+2);readln(anio);
		if (dia > 31) or (dia < 01) then
		begin
			repeat
				gotoxy(x+95,y+2);write('  ');
				gotoxy(x+95,y+2);readln(dia);                                                //  Validamos el dia
			until (dia <= 31) and (dia >= 01);
		end;
		if (dia = 31) then
		begin
			if (mes = 04) or (mes = 06) or (mes = 09) or (mes = 11) then
			begin
				repeat
					gotoxy(x+95,y+2);write('  ');
					gotoxy(x+95,y+2);readln(dia);
				until (dia <= 30);
			end;
		end;
		if (((anio mod 4) = 0) and ((anio mod 100) <> 0)) or ((anio mod 400) = 0) then     
      		bisiesto:=TRUE {Es ano bisiesto}
   		else                                                                                 //Validamos si es año bisieso o no
      		bisiesto:=FALSE; {No es ano bisiesto}
      	if (mes < 01) or (mes > 12) then
		begin
				repeat
					gotoxy(x+98,y+2);write('  ');
					gotoxy(x+98,y+2);readln(mes);											// Validamos el mes
				until (mes >= 01) and (mes <= 12);
		end;
		if (bisiesto = false) and (mes = 02) and (dia > 28) then
		begin
			repeat
				gotoxy(x+95,y+2);write('  ');
				gotoxy(x+95,y+2);readln(dia);												//Validamos el dia segun el mes de febrero y el año
			until (dia <= 28);
		end;
		if (bisiesto = true) and (mes = 02) and (dia > 29) then
		begin
			repeat
				gotoxy(x+95,y+2);write('  ');
				gotoxy(x+95,y+2);readln(dia);
			until (dia <= 29);
		end;
		gotoxy(x+115,y+2);exportacion := readkey;
		if (exportacion <> 's') or (exportacion <> 'S') or (exportacion <> 'n') or (exportacion <> 'N') then
		begin
			repeat
				gotoxy(x+115,y+2);writeln('  ');
				gotoxy(x+115,y+2);readln(exportacion);
			until (exportacion = 'S') or (exportacion = 's') or (exportacion = 'N') or (exportacion = 'n');
		end;
		case upcase(exportacion) of
			'S' : reg_proyecto.exporta:= true;
			'N' : reg_proyecto.exporta:= false;
		end;
		gotoxy(x,y+4);writeln('Quiere cargar el proyecto en el sistema? S/N');
		op:=readkey();
		case upcase(op) of
		
			'S':begin
			 		seek(f_proyecto,fileSize(f_proyecto));
		  			escribir_proyecto(f_proyecto,reg_proyecto);
		  			clrscr;
		  			writeln('Su proyecto se cargo correctamente.');
		  			cerrar_proyecto(f_proyecto);
		  			menu_principal();
		  			readkey();
				end;

			'N':begin
					cerrar_proyecto(f_proyecto);
		  			menu_principal();
				end;
		end;
	end;		
end;


procedure modificacion_proyectos(var f_proyecto:fichero_proyec; var id_buscado:word);
var
	salida,valida_c,bisiesto,encontrado:boolean;
	exportacion,opcion:char;
	x,y:word;
begin
	encontrado:=false;
	abrir_proyecto(f_proyecto); {Abrimos el archivo proyecto}
	x:=10;
	y:=5;
	textbackground(black);clrscr;
	textcolor(10);
	gotoxy(x+1,y-1);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+1,y+1);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+38,y+2);write('|');textcolor(5);write('$ ');
	textcolor(10);
	gotoxy(x+55,y+2);write('|');
	gotoxy(x+70,y+2);write('|');
	gotoxy(x+93,y+2);write('|');
	gotoxy(x+114,y+2);write('|');
	gotoxy(x+132,y+2);write('|');
	gotoxy(x+1,y+3);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x,y);textcolor(10);write('|   ');textcolor(5);write('ID   ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(x,y+2);textcolor(10);write('| ');textcolor(white);write('0');textcolor(10);write('      |');
	gotoxy(x+11,y);textcolor(5);write('          Titulo           ');textcolor(10);write('|');
	gotoxy(x+39,y);textcolor(5);write('     Costo      ');textcolor(10);write('|');
	gotoxy(x+57,y);textcolor(5);write('    Cuit     ');textcolor(10);write('|');
	gotoxy(x+71,y);textcolor(5);write('      Director        ');textcolor(10);write('|');
	gotoxy(x+94,y);textcolor(5);write('  Fecha de entrega  ');textcolor(10);write('|');
	gotoxy(115+x,y);textcolor(5);write('   Exporta(S/N)  ');textcolor(10);write('|');
	textcolor(10);
	gotoxy(x+4,1);writeln('Ingrese el ID a buscar:');
	textcolor(white);
	gotoxy(x+4,2);read(id_buscado); {leemos el id a buscar}
	while not eof(f_proyecto) and (encontrado = false) do
	begin
		read(f_proyecto,reg_proyecto);
		if (id_buscado = reg_proyecto.id_proyecto) and (reg_proyecto.vigente = true) then
		begin
			encontrado:=true;
		end;
	end;
		if (encontrado = true) then
		begin

			repeat
				salida:= false;
				textbackground(11);clrscr;
				x:=10;
				y:=5;
				seek(f_proyecto,filePos(f_proyecto));
				textbackground(black);clrscr;
				textcolor(10);
				gotoxy(x+1,y-1);write('-----------------------------------------------------------------------------------------------------------------------------------');
				gotoxy(x+1,y+1);write('-----------------------------------------------------------------------------------------------------------------------------------');
				gotoxy(x+38,y+2);write('|');textcolor(5);write('$ ');
				textcolor(10);
				gotoxy(x+55,y+2);write('|');
				gotoxy(x+70,y+2);write('|');
				gotoxy(x+93,y+2);write('|');
				gotoxy(x+114,y+2);write('|');
				gotoxy(x+132,y+2);write('|');
				gotoxy(x+1,y+3);write('-----------------------------------------------------------------------------------------------------------------------------------');
				gotoxy(x,y);textcolor(10);write('|   ');textcolor(5);write('ID    ');textcolor(10);write('|');
				textcolor(white);
				gotoxy(x,y+2);textcolor(10);write('| ');textcolor(white);write(reg_proyecto.id_proyecto);textcolor(10);write('      |');
				gotoxy(x+11,y);textcolor(5);write('          Titulo           ');textcolor(10);write('|');
				gotoxy(x+39,y);textcolor(5);write('     Costo      ');textcolor(10);write('|');
				gotoxy(x+57,y);textcolor(5);write('    Cuit     ');textcolor(10);write('|');
				gotoxy(x+71,y);textcolor(5);write('      Director        ');textcolor(10);write('|');
				gotoxy(x+94,y);textcolor(5);write('  Fecha de entrega  ');textcolor(10);write('|');
				gotoxy(115+x,y);textcolor(5);write('   Exporta(S/N)  ');textcolor(10);write('|');
				textcolor(white);
				gotoxy(x+11,y+2);write(reg_proyecto.titulo);
				gotoxy(x+41,y+2);write(reg_proyecto.costo:2:0);
				gotoxy(x+56,y+2);write(reg_proyecto.cuit);
				gotoxy(x+72,y+2);write(reg_proyecto.director);
				textcolor(11);
				gotoxy(x+97,y+2);write('/');
				textcolor(white);
				gotoxy(x+95,y+2);write(reg_proyecto.dia);
				gotoxy(x+98,y+2);write(reg_proyecto.mes);
				textcolor(11);
				gotoxy(x+100,y+2);write('/');
				textcolor(white);
				gotoxy(x+101,y+2);write(reg_proyecto.anio);
				gotoxy(x+118,y+2);write(reg_proyecto.exporta);
				textcolor(white);
				gotoxy(x+4,y+5); write('|  1. Titulo  |  2. Costo  |  3. Cuit  |  4. Director  |  5. Fecha entrega  |  6. Exporta S/N  |  7. Volver  |');
				textcolor(5);
				gotoxy(x+4,y+7);write('# Opcion: ');
				gotoxy(x+4,y+8);textcolor(white); opcion:=readkey();
			    case opcion of
				 '1':begin
				 		textcolor(white);
						gotoxy(x+11,y+2);write('                           ');readln;
						gotoxy(x+11,y+2);read(reg_proyecto.titulo);
						titulo_mayus(reg_proyecto);
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
				  	end;
				 '2':begin
				 		textcolor(white);
				 		gotoxy(x+41,y+2);write('              ');
				 		gotoxy(x+41,y+2);read(reg_proyecto.costo);
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
					end;					 
				 '3':begin
				 		textcolor(white);
				  		gotoxy(x+56,y+2);write('             ');readln;
				  		gotoxy(x+56,y+2);read(reg_proyecto.cuit);
						validar_cuit(reg_proyecto.cuit, valida_c);
						if not valida_c then
						begin
							repeat
								gotoxy(x+56,y+2);write('             ');readln;
				  				gotoxy(x+56,y+2);read(reg_proyecto.cuit);
								validar_cuit(reg_proyecto.cuit, valida_c);
							until (valida_c = true);
						end;
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
				  	end;
				 '4':begin
				 		textcolor(white);
				 		gotoxy(x+72,y+2);write('                     ');readln;
						gotoxy(x+72,y+2);read(reg_proyecto.director);
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
				  	end;
				 '5':begin
				 		textcolor(11);
						gotoxy(x+97,y+2);write('/');
						textcolor(white);
						gotoxy(x+95,y+2);read(reg_proyecto.dia);
						gotoxy(x+98,y+2);read(reg_proyecto.mes);;
						textcolor(11);
						gotoxy(x+100,y+2);write('/');
						textcolor(white);
						gotoxy(x+101,y+2);read(reg_proyecto.anio);
						if (reg_proyecto.dia > 31) or (reg_proyecto.dia < 01) then
						begin
							repeat
								gotoxy(x+95,y+2);write('  ');
								gotoxy(x+95,y+2);readln(reg_proyecto.dia);
							until (reg_proyecto.dia <= 31) and (reg_proyecto.dia >= 01);
						end;
						if (reg_proyecto.dia = 31) and (reg_proyecto.mes = 04) or (reg_proyecto.mes = 06) or (reg_proyecto.mes = 09) or (reg_proyecto.mes = 11) then
						begin
							repeat
								gotoxy(x+95,y+2);write('  ');
								gotoxy(x+95,y+2);readln(reg_proyecto.dia);
							until (reg_proyecto.dia <= 30);
						end;
						if (((reg_proyecto.anio mod 4) = 0) and ((reg_proyecto.anio mod 100) <> 0)) or ((reg_proyecto.anio mod 400) = 0) then
				      		bisiesto:=TRUE {Es ano bisiesto}
				   		else
				      		bisiesto:=FALSE; {No es ano bisiesto}
				      	if (reg_proyecto.mes < 01) or (reg_proyecto.mes > 12) then
						begin
								repeat
									gotoxy(x+98,y+2);write('  ');
									gotoxy(x+98,y+2);readln(reg_proyecto.mes);
								until (reg_proyecto.mes >= 01) and (reg_proyecto.mes <= 12);
						end;
						if (bisiesto = false) and (reg_proyecto.mes = 02) and (reg_proyecto.dia > 28) then
						begin
							repeat
								gotoxy(x+95,y+2);write('  ');
								gotoxy(x+95,y+2);readln(reg_proyecto.dia);
							until (reg_proyecto.dia <= 28);
						end;
						if (bisiesto = true) and (reg_proyecto.mes = 02) and (reg_proyecto.dia > 29) then
						begin
							repeat
								gotoxy(x+95,y+2);write('  ');
								gotoxy(x+95,y+2);readln(reg_proyecto.dia);
							until (reg_proyecto.dia <= 29);
						end;
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
				  	end;
				 '6':begin
				  		repeat
				 		gotoxy(x+115,y+2);writeln('                  ');readln;
				  		gotoxy(x+118,y+2);read(exportacion);
						case exportacion of
							's': reg_proyecto.exporta:= true;
							'n': reg_proyecto.exporta:= false;
							'S': reg_proyecto.exporta:= true;
							'N': reg_proyecto.exporta:= false;
						end;
						until (exportacion = 's') or (exportacion = 'n') or (exportacion = 'N') or (exportacion = 'S');
						seek(f_proyecto, filePos(f_proyecto)-1);
						write(f_proyecto,reg_proyecto);
					end;
				'7':begin
				  		Salida:= true;
				  	end;
				end;
				 
		  	Until (Salida=true);
			clrscr;
		end
		else
		if not reg_proyecto.vigente then
		begin
			clrscr;
			textcolor(red);
			writeln('El proyecto fue dado de baja.');
			readkey();
		end
		else 
		begin
			writeln;
			clrscr;
			textcolor(red);
			writeln('No existe el ID que acaba de ingresar!');
			readkey();
		end;
	cerrar_proyecto(f_proyecto);
	submenuProy();
end;

procedure bajas(var f_proyecto: fichero_proyec);
var
	x,y:word;
	encontrado: boolean;
	id_buscado: word;
	op: char;
begin
	encontrado:=false;
	abrir_proyecto(f_proyecto); {Abrimos el archivo proyecto}
	textcolor(11);
	tabla(x,y);
	gotoxy(10,1);writeln ('Ingrese el ID del proyecto a dar de baja.');
	textcolor(white);
	gotoxy(10,2);read(id_buscado); {leemos el id a buscar}
	seek(f_proyecto,0);
	while not eof(f_proyecto) and (encontrado = false) do
	begin
		read(f_proyecto,reg_proyecto);
		if (id_buscado = reg_proyecto.id_proyecto) and (reg_proyecto.vigente = true) then
		begin
			encontrado:=true;
		end;
	end;
		if (encontrado = true) then
		begin
			tabla(x,y);
			gotoxy(10, y+2);write('| ');
			textcolor(white);
			gotoxy(x+11,y+2);write(reg_proyecto.titulo);
			gotoxy(x+41,y+2);write(reg_proyecto.costo:2:0);
			gotoxy(x+56,y+2);write(reg_proyecto.cuit);
			gotoxy(x+72,y+2);write(reg_proyecto.director);
			textcolor(10);
			gotoxy(x+97,y+2);write('/');
			textcolor(white);
			gotoxy(x+95,y+2);write(reg_proyecto.dia);
			gotoxy(x+98,y+2);write(reg_proyecto.mes);
			textcolor(10);
			gotoxy(x+100,y+2);write('/');
			textcolor(white);
			gotoxy(x+101,y+2);write(reg_proyecto.anio);
			gotoxy(x+118,y+2);write(reg_proyecto.exporta);
			gotoxy(x,y+5);write('Esta seguro que quiere dar de baja este proyecto? S/N');
			gotoxy(x,y+5); op := readkey;
			case upcase(op) of
				'S' : reg_proyecto.vigente := false;
				'N' : submenuProy;	
			end;
		end
		else
		begin
			textcolor(red);
			clrscr;
			writeln('No existe el ID que ingreso.');
			readkey();
		end;
	seek(f_proyecto, filepos(f_proyecto)-1);
	write(f_proyecto,reg_proyecto);
	close(f_proyecto);
end;

procedure mostrar_proyectos_t(var x:word ; var y: word);
var 
	aux_dia: string;
	aux_mes: string;
	aux_anio: string;
begin
	textcolor(10);
	gotoxy(x+1,4);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+1,6);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x+38,y+7);write('|');textcolor(5);write('$ ');
	textcolor(10);
	gotoxy(x+55,y+7);write('|');
	gotoxy(x+70,y+7);write('|');
	gotoxy(x+93,y+7);write('|');
	gotoxy(x+114,y+7);write('|');
	gotoxy(x+132,y+7);write('|');
	gotoxy(x+1,y+8);write('-----------------------------------------------------------------------------------------------------------------------------------');
	gotoxy(x,5);textcolor(10);write('|   ');textcolor(5);write('ID   ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(x,y+7);textcolor(10);write('| ');textcolor(white);write(reg_proyecto.id_proyecto);textcolor(10);write('      |');
	gotoxy(x+11,5);textcolor(5);write('          Titulo           ');textcolor(10);write('|');
	gotoxy(x+39,5);textcolor(5);write('     Costo      ');textcolor(10);write('|');
	gotoxy(x+57,5);textcolor(5);write('    Cuit     ');textcolor(10);write('|');
	gotoxy(x+71,5);textcolor(5);write('      Director        ');textcolor(10);write('|');
	gotoxy(x+94,5);textcolor(5);write('  Fecha de entrega  ');textcolor(10);write('|');
	gotoxy(115+x,5);textcolor(5);write('   Exporta(S/N)  ');textcolor(10);write('|');
	textcolor(white);
	gotoxy(x+11,y+7);write(reg_proyecto.titulo);
	gotoxy(x+41,y+7);write(reg_proyecto.costo:2:0);
	gotoxy(x+56,y+7);write(reg_proyecto.cuit);
	gotoxy(x+72,y+7);write(reg_proyecto.director);
	textcolor(11);
	aux_dia:= inttostr(reg_proyecto.dia);
	aux_mes:= inttostr(reg_proyecto.mes);
	aux_anio:=inttostr(reg_proyecto.anio);
	textcolor(white);
	if (length(aux_dia) = 1) then
	begin
		gotoxy(x+95,y+7);write('0',reg_proyecto.dia);
	end
	else
		gotoxy(x+95,y+7);write(reg_proyecto.dia);
	if (length(aux_mes) = 1) then
	begin
		gotoxy(x+98,y+7);write('0',reg_proyecto.mes);
	end
	else
		gotoxy(x+98,y+7);write(reg_proyecto.mes);
	textcolor(5);
	gotoxy(x+97,y+7);write('/');
	gotoxy(x+100,y+7);write('/');
	textcolor(white);
	if (length(aux_anio) = 2) then
	begin
		gotoxy(x+101,y+7);write('20',reg_proyecto.anio);
	end
	else
		gotoxy(x+101,y+7);write(reg_proyecto.anio);
	gotoxy(x+115,y+7);write(reg_proyecto.exporta);
end;

procedure mostrar_p(var f_proyecto:fichero_proyec);
var
	x,y : word;
	cont_enter: integer;
begin
	cont_enter := 0;
	abrir_proyecto(f_proyecto);
	x:=10;
	y:=0;
	seek(f_proyecto,0);
	while not eof (f_proyecto) do
	begin
		read(f_proyecto,reg_proyecto);
       	if reg_proyecto.vigente then
       	begin
       		mostrar_proyectos_t(x,y);
       		y:= y + 2;
       		cont_enter:= cont_enter + 1;
       		if (cont_enter = 16) then
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
    cerrar_proyecto(f_proyecto);
    Submenu_Consultas;
end;

procedure ordenar_titulo(var f_proyecto:fichero_proyec);
var
	reg1,reg2 : t_proyec;
    i, j, lim: word;
begin
	abrir_proyecto(f_proyecto);
	i:=0;
	j:=0;
	lim:= filesize(f_proyecto)-1;
	for i := 1 to lim - 1  do
	begin
	 	for j := 0 to lim - i  do
		begin
			seek(f_proyecto,j);
		 	read(f_proyecto,reg1);
	    	seek(f_proyecto,j+1);
	    	read(f_proyecto,reg2);
	    	if (reg1.titulo > reg2.titulo) then
	    	begin
	       		seek (f_proyecto,j+1);
          		write(f_proyecto,reg1);
          		seek (f_proyecto,j);
          		write(f_proyecto,reg2);
	    	end;
	 	end;
	end;
	cerrar_proyecto(f_proyecto);
end;

procedure validacion(var d_i:integer; var m_i: integer ;var a_i: integer ;var d_f: integer;var m_f: integer; var a_f:integer );
var
	bisiesto_i,bisiesto_f:boolean;
	aux_dia,aux_mes,aux_fecha_inicial,aux_fecha_final: String;
begin
		textbackground(black);clrscr;
		d_i:=0; m_i:=0; a_i:=0; d_f:=0; m_f:=0; a_f:=0;
		textcolor(10);
		gotoxy(30,9);writeln('--------------------------------------------------');
		gotoxy(30,10);writeln('|');
		gotoxy(80,10);writeln('|');
		textcolor(5);
		gotoxy(31,10);writeln('Ingrese la fecha inicial ( DD / MM / AAAA ): ');
		textcolor(10);
		gotoxy(30,11);writeln('--------------------------------------------------');
		gotoxy(30,12);writeln('|');
		gotoxy(80,12);writeln('|');
		textcolor(10);
		gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);read(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);read(a_i);
		clrscr;
		textcolor(10);
		gotoxy(30,9);writeln('--------------------------------------------------');
		gotoxy(30,10);writeln('|');
		gotoxy(80,10);writeln('|');
		gotoxy(31,10);textcolor(5);write('Fecha inicial: ');textcolor(white);write(d_i);textcolor(5);write('/');textcolor(white);write(m_i);textcolor(5);write('/');textcolor(white);write(a_i);
		textcolor(10);
		gotoxy(30,11);writeln('--------------------------------------------------');
		gotoxy(30,12);writeln('|');
		gotoxy(80,12);writeln('|');
		textcolor(5);
		gotoxy(31,12);writeln('Ingrese la fecha final (DD / MM / AAAA): ');
		textcolor(10);
		gotoxy(30,13);writeln('--------------------------------------------------');
		gotoxy(30,14);writeln('|');
		gotoxy(80,14);writeln('|');
		textcolor(10);
		gotoxy(31,14);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,14);write('/');textcolor(white);read(m_f);textcolor(5);gotoxy(37,14);write('/');textcolor(white);read(a_f);
		aux_fecha_inicial:='';
		aux_dia:='';
		aux_mes:='';
		aux_dia:= inttostr(d_i);
		aux_mes:= inttostr(m_i);
		aux_fecha_inicial:=inttostr(a_i);
		if length(aux_mes) < 2 then
			aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_mes    
		else
			aux_fecha_inicial:= aux_fecha_inicial + aux_mes;
		if length (aux_dia) < 2 then
			aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_dia
		else 
			aux_fecha_inicial := aux_fecha_inicial + aux_dia;     //Acumulamos la fecha inicial

		aux_dia:='';
		aux_mes:='';
		aux_fecha_final:='';
		aux_dia:= inttostr (d_f);
		aux_mes:= inttostr(m_f);
		aux_fecha_final:=inttostr(a_f);

		if length(aux_mes) < 2 then
			aux_fecha_final:= aux_fecha_final + '0' + aux_mes
		else
			aux_fecha_final:= aux_fecha_final + aux_mes;
		if length (aux_dia) < 2 then
			aux_fecha_final:= aux_fecha_final + '0' + aux_dia
		else 
			aux_fecha_final := aux_fecha_final + aux_dia;       //Acumulamos la fecha final

		if (aux_fecha_inicial > aux_fecha_final) then
		begin
			repeat
				textbackground(black);clrscr;
				d_i:=0; m_i:=0; a_i:=0; d_f:=0; m_f:=0; a_f:=0;
				textcolor(4);
				gotoxy(30,8);writeln('La fecha inicial es mayor que la final!');
				textcolor(10);
				gotoxy(30,9);writeln('--------------------------------------------------');
				gotoxy(30,10);writeln('|');
				gotoxy(80,10);writeln('|');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese la fecha inicial ( DD / MM / AAAA ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(10);
				gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);read(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);read(a_i);
				clrscr;
				textcolor(10);
				gotoxy(30,9);writeln('--------------------------------------------------');
				gotoxy(30,10);writeln('|');
				gotoxy(80,10);writeln('|');
				gotoxy(31,10);textcolor(5);write('Fecha inicial: ');textcolor(white);write(d_i);textcolor(5);write('/');textcolor(white);write(m_i);textcolor(5);write('/');textcolor(white);write(a_i);
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);writeln('Ingrese la fecha final (DD / MM / AAAA): ');
				textcolor(10);
				gotoxy(30,13);writeln('--------------------------------------------------');
				gotoxy(30,14);writeln('|');
				gotoxy(80,14);writeln('|');
				textcolor(10);
				gotoxy(31,14);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,14);write('/');textcolor(white);read(m_f);textcolor(5);gotoxy(37,14);write('/');textcolor(white);read(a_f);
				aux_fecha_inicial:='';
				aux_dia:='';
				aux_mes:='';
				aux_dia:= inttostr(d_i);
				aux_mes:= inttostr(m_i);
				aux_fecha_inicial:=inttostr(a_i);
				if length(aux_mes) < 2 then
					aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_mes    
				else
					aux_fecha_inicial:= aux_fecha_inicial + aux_mes;
				if length (aux_dia) < 2 then
					aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_dia
				else 
					aux_fecha_inicial := aux_fecha_inicial + aux_dia;     //Acumulamos la fecha inicial

				aux_dia:='';
				aux_mes:='';
				aux_fecha_final:='';
				aux_dia:= inttostr (d_f);
				aux_mes:= inttostr(m_f);
				aux_fecha_final:=inttostr(a_f);

				if length(aux_mes) < 2 then
					aux_fecha_final:= aux_fecha_final + '0' + aux_mes
				else
					aux_fecha_final:= aux_fecha_final + aux_mes;
				if length (aux_dia) < 2 then
					aux_fecha_final:= aux_fecha_final + '0' + aux_dia
				else 
					aux_fecha_final := aux_fecha_final + aux_dia;       //Acumulamos la fecha final
			until(aux_fecha_inicial < aux_fecha_final);	
		end;
		clrscr;
		textcolor(10);
		gotoxy(30,9);writeln('--------------------------------------------------');
		gotoxy(30,10);writeln('|');
		gotoxy(80,10);writeln('|');
		gotoxy(31,10);textcolor(5);write('Fecha inicial: ');textcolor(white);write(d_i);textcolor(5);write('/');textcolor(white);write(m_i);textcolor(5);write('/');textcolor(white);write(a_i);
		textcolor(10);
		gotoxy(30,11);writeln('--------------------------------------------------');
		gotoxy(30,12);writeln('|');
		gotoxy(80,12);writeln('|');
		gotoxy(31,12);textcolor(5);write('Fecha final: ');textcolor(white);write(d_f);textcolor(5);write('/');textcolor(white);write(m_f);textcolor(5);write('/');textcolor(white);write(a_f);
		textcolor(10);
		gotoxy(30,13);writeln('--------------------------------------------------');
		if (d_i > 31) or (d_i < 01) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El dia que ingreso es incorrecto!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_i);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_i <= 31) and (d_i >= 01);
		end;
		if (d_i = 31) and (m_i = 04) or (m_i = 06) or (m_i = 09) or (m_i = 11) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El dia que ingreso es incorrecto!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD  ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_i);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_i <= 30);
		end;
		bisiesto_i:=false;
		if (((a_i mod 4) = 0) and ((a_i mod 100) <> 0)) or ((a_i mod 400) = 0) then
      		bisiesto_i:=true {Es ano bisiesto}
   		else
      		bisiesto_i:=false; {No es ano bisiesto}
      	if (m_i < 01) or (m_i > 12) then
		begin
				repeat
					clrscr;
					textcolor(red);
					gotoxy(31,8);writeln('El mes que ingreso es incorrecto!');
					gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
					textcolor(5);
					gotoxy(31,10);writeln('Ingrese el mes ( MM ): ');
					textcolor(10);
					gotoxy(30,11);writeln('--------------------------------------------------');
					gotoxy(30,12);writeln('|');
					gotoxy(80,12);writeln('|');
					textcolor(5);
					gotoxy(31,12);write('#');textcolor(white);write(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);read(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_i);
					textcolor(white);
					gotoxy(31,13);writeln('Presione enter para guardar.');
					readkey();
					clrscr;
				until (m_i >= 01) and (m_i <= 12);
		end;
		if (bisiesto_i = false) and (m_i = 02) and (d_i > 28) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El anio no es bisiesto por lo tanto el mes 02 tiene 28 dias!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_i);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_i <= 28);

		end;
		if (bisiesto_i = true) and (m_i = 02) and (d_i > 29) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El anio es bisiesto por lo tanto el mes 02 tiene 29 dias!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_i);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_i);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_i);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_i <= 29);
			readkey();
		end;

		if (d_f > 31) or (d_f < 01) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El dia que ingreso es incorrecto!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_f);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_f);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_f <= 31) and (d_f >= 01);
		end;
		if (d_f = 31) and (m_f = 04) or (m_f = 06) or (m_f = 09) or (m_f = 11) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El dia que ingreso es incorrecto!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_f);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_f);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_f <= 30);
		end;
		bisiesto_f:=false;
		if (((a_f mod 4) = 0) and ((a_f mod 100) <> 0)) or ((a_f mod 400) = 0) then
      		bisiesto_f:=true {Es ano bisiesto}
   		else
      		bisiesto_f:=false; {No es ano bisiesto}
      	if (m_f < 01) or (m_f > 12) then
		begin
				repeat
					clrscr;
					textcolor(red);
					gotoxy(31,8);writeln('El mes que ingreso es incorrecto!');
					gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
					textcolor(5);
					gotoxy(31,10);writeln('Ingrese nuevamente el mes ( MM ): ');
					textcolor(10);
					gotoxy(30,11);writeln('--------------------------------------------------');
					gotoxy(30,12);writeln('|');
					gotoxy(80,12);writeln('|');
					textcolor(5);
					gotoxy(31,12);write('#');textcolor(white);write(d_f);textcolor(5);gotoxy(34,12);write('/');textcolor(white);read(m_f);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_f);
					textcolor(white);
					gotoxy(31,13);writeln('Presione enter para guardar.');
					readkey();
					clrscr;
				until (m_f >= 01) and (m_f <= 12);
		end;
		textcolor(green);
		if (bisiesto_f = false) and (m_f = 02) and (d_f > 28) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El anio no es bisiesto por lo tanto el mes 02 tiene 28 dias!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				textcolor(5);
				gotoxy(31,10);writeln('Ingrese nuevamente el dia ( DD ): ');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_f);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_f);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_f <= 28);
			readkey();
		end;
		if (bisiesto_f = true) and (m_f = 02) and (d_f > 29) then
		begin
			repeat
				clrscr;
				textcolor(red);
				gotoxy(31,8);writeln('El anio es bisiesto por lo tanto el mes 02 tiene 29 dias!');
				gotoxy(31,9);writeln('Por favor ingreselo nuevamente');
				gotoxy(31,10);writeln('Ingrese nuevamente el dia (DD)');
				textcolor(10);
				gotoxy(30,11);writeln('--------------------------------------------------');
				gotoxy(30,12);writeln('|');
				gotoxy(80,12);writeln('|');
				textcolor(5);
				gotoxy(31,12);write('#');textcolor(white);read(d_f);textcolor(5);gotoxy(34,12);write('/');textcolor(white);write(m_f);textcolor(5);gotoxy(37,12);write('/');textcolor(white);write(a_f);
				textcolor(white);
				gotoxy(31,13);writeln('Presione enter para guardar.');
				readkey();
				clrscr;
			until (d_f <= 29);
			readkey();
		end;
		clrscr;
		gotoxy(2,3);textcolor(5);write('Fecha inicial: ');textcolor(white);write(d_i);textcolor(5);write('/');textcolor(white);write(m_i);textcolor(5);write('/');textcolor(white);write(a_i);
		textcolor(11);
		gotoxy(2,5);textcolor(5);write('Fecha final: ');textcolor(white);write(d_f);textcolor(5);write('/');textcolor(white);write(m_f);textcolor(5);write('/');textcolor(white);writeln(a_f);
		textcolor(5);
		gotoxy (2,7);writeln('Presione enter para ver los proyectos.');
		readkey();		
end;

procedure rango_de_fechas(var f_proyecto:fichero_proyec);

var
	x,y:word;
	cont_enter,k: Integer;
	aux_fecha, aux_dia, aux_mes, aux_fecha_inicial, aux_fecha_final: string;
	validar:boolean;
	d_i,m_i, a_i, d_f, m_f, a_f: integer;
begin
		abrir_proyecto(f_proyecto);
		validacion(d_i,m_i, a_i, d_f, m_f, a_f);	
		textbackground(black);clrscr;
		validar:=false;
		cont_enter:=0;
		textcolor(5);
		gotoxy(10,2);writeln('Proyectos entre la fecha inicial y la fecha final: ');
		k:=0;
		x:=10;
		y:=0;
		for k := 0 to filesize(f_proyecto)-1 do
		begin
			// CONVERTIMOS LA FECHA EN STRING
			cerrar_proyecto(f_proyecto);
			ordenar_titulo(f_proyecto);
			abrir_proyecto(f_proyecto);
			seek(f_proyecto,k);
			read(f_proyecto,reg_proyecto);
			aux_fecha:='';
			aux_dia:='';
			aux_mes:='';
			aux_dia:= inttostr(reg_proyecto.dia);
			aux_mes:= inttostr(reg_proyecto.mes);
			aux_fecha:=inttostr(reg_proyecto.anio);
			//Acumulamos el dia el mes y el año en una variable

			if length(aux_mes) < 2 then                    //Si ingresa solamente un digito le agregamos 0 
				aux_fecha:= aux_fecha + '0' + aux_mes
			else
				aux_fecha:= aux_fecha + aux_mes;
			if length (aux_dia) < 2 then
				aux_fecha:= aux_fecha + '0' + aux_dia
			else 
				aux_fecha := aux_fecha + aux_dia;          //Acumulamos la fecha del registro

			aux_dia:='';
			aux_mes:='';
			aux_fecha_inicial:='';
			aux_dia:= inttostr (d_i);
			aux_mes:= inttostr (m_i);
			aux_fecha_inicial:=inttostr(a_i);

			if length(aux_mes) < 2 then
				aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_mes    
			else
				aux_fecha_inicial:= aux_fecha_inicial + aux_mes;
			if length (aux_dia) < 2 then
				aux_fecha_inicial:= aux_fecha_inicial + '0' + aux_dia
			else 
				aux_fecha_inicial := aux_fecha_inicial + aux_dia;     //Acumulamos la fecha inicial

			aux_dia:='';
			aux_mes:='';
			aux_fecha_final:='';
			aux_dia:= inttostr (d_f);
			aux_mes:= inttostr(m_f);
			aux_fecha_final:=inttostr(a_f);

			if length(aux_mes) < 2 then
				aux_fecha_final:= aux_fecha_final + '0' + aux_mes
			else
				aux_fecha_final:= aux_fecha_final + aux_mes;
			if length (aux_dia) < 2 then
				aux_fecha_final:= aux_fecha_final + '0' + aux_dia
			else 
				aux_fecha_final := aux_fecha_final + aux_dia;       //Acumulamos la fecha final


			if (aux_fecha >= aux_fecha_inicial) and (aux_fecha <= aux_fecha_final) then  //Comparamos si la fecha esta entre f_i y f_f
			begin
				if reg_proyecto.vigente then
				begin
					mostrar_proyectos_t(x,y);
					cont_enter:= cont_enter + 1;
					y:= y+2;
       				if (cont_enter = 16) then
		       		begin
		       			gotoxy(x+2,y+10);write('== Presione enter para seguir viendo los proyectos. ==');
		       			readkey;
		       			x:=10;
						y:=0;
						clrscr;
		       		end;
					validar:=true;

				end;
			end;
			
		end;
		if (validar = true) then
		begin
			writeln();
			writeln;
			gotoxy(10,y+8);writeln('No hay mas proyectos entre la fecha inicial y la fecha final');
			readkey();
		end
		else
		begin
			clrscr;
			textcolor(4);
			gotoxy(40,y+14);writeln('**************************************************************');
			gotoxy(40,y+15);writeln('* No existen proyectos entre fecha inicial y fecha final !!! *');
			gotoxy(40,y+16);writeln('**************************************************************');
			readkey();
		end;
	cerrar_proyecto(f_proyecto);
end;

end.