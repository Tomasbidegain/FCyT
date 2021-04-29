Unit SubmenuCli;

Interface

uses crt,unit_menu_principal,registros;

var
	opcion:integer;
	salida:boolean;

procedure submenuClien();

Implementation
uses 
	unitclientes_tp,SubmenuConsultasClientes;

procedure submenuClien();
	var opcion:char;
		salida:boolean;
begin
	salida:= false;
	repeat
	textbackground (black);
		clrscr;
		//COLOR DE TEXTO
		textcolor (red);
		gotoxy(38,9); writeln('-------------------------------------------------------');
		gotoxy(37,9);writeln('|');
		gotoxy(92,9);writeln('|');
		textcolor(green);
		gotoxy(60,10);writeln(' CLIENTES  ');
		textcolor(red);
		gotoxy(37,10);writeln('|');
		gotoxy(92,10);writeln('|');
		gotoxy(37,11); writeln('-------------------------------------------------------');
		gotoxy(37,11);writeln('|');
		gotoxy(92,11);writeln('|');
		gotoxy(38,12);textcolor(Green); write('.1 : '); textcolor(white); writeln('Dar de alta un cliente.');
		textcolor(red);
		gotoxy(37,12);writeln('|');
		gotoxy(92,12);writeln('|');
		gotoxy(37,13); writeln('-------------------------------------------------------');
		gotoxy(37,13);writeln('|');
		gotoxy(92,13);writeln('|');
		textcolor(white);
		gotoxy(38,14);textcolor(green); write('.2 : '); textcolor(white); writeln('Dar de baja un cliente.');
		textcolor(red);
		gotoxy(37,14);writeln('|');
		gotoxy(92,14);writeln('|');
		gotoxy(38,15); writeln('------------------------------------------------------');
		gotoxy(37,15);writeln('|');
		gotoxy(92,15);writeln('|');
		gotoxy(38,16);textcolor(green); write('.3 : '); textcolor(white); writeln('Modificar un cliente.');
		textcolor(red);
		gotoxy(38,17); writeln('------------------------------------------------------');
		gotoxy(37,16);writeln('|');
		gotoxy(92,16);writeln('|');
		gotoxy(37,17);writeln('|');
		gotoxy(92,17);writeln('|');
		gotoxy(38,18);textcolor(green); write('.4 : '); textcolor(white); writeln('Consultas de clientes.');
		textcolor(red);
		gotoxy(38,19); writeln('------------------------------------------------------');
		gotoxy(37,18);writeln('|');
		gotoxy(92,18);writeln('|');
		gotoxy(37,19);writeln('|');
		gotoxy(92,19);writeln('|');
		gotoxy(38,20);textcolor(green); write('.5 : '); textcolor(white); writeln('Volver al menu principal.');
		textcolor(red);
		gotoxy(38,21); writeln('------------------------------------------------------');
		gotoxy(37,20);writeln('|');
		gotoxy(92,20);writeln('|');
		gotoxy(37,21);writeln('|');
		gotoxy(92,21);writeln('|');
		gotoxy(37,23); write('# Opcion: ');
		opcion:= readkey;
	    case opcion of
		 '1':begin
		 		gotoxy(38,12);textcolor(Green); write('.1 : Dar de alta un cliente.');
		 		delay(250);
		  		Alta_cliente(cliente);
		  		textbackground(black);clrscr;
		  		gotoxy(28,12);writeln('***************************************************************');
				gotoxy(28,13);writeln('*');								   gotoxy(90,13);writeln('*');
				gotoxy(30,13);writeln('Usted ha sido cargado correctamente en el sistema.');
				gotoxy(28,14);writeln('***************************************************************');
				readkey();
		  		menu_principal();
		  	end;
		'2':begin
				gotoxy(38,14);textcolor(green); write('.2 : Dar de baja un cliente.');
				delay(250);
		 		bajas_clientes(cliente);
			end;
		'3':begin
		 		gotoxy(38,16);textcolor(green); write('.3 : Modificar un cliente.');
		 		delay(250);
		 		modificacion_cliente(cliente);
			end;
		'4':begin
				gotoxy(38,18);textcolor(green); write('.4 : Consultas de clientes.');
				delay(250);
		  		SubMenu_Consultas_c();
		  	end;

		'5':begin
		 		gotoxy(38,20);textcolor(green); write('.5 : Volver al menu principal.');
		 		delay(250);
		 		Salida:= true;
			end;
		end;  
  	Until (Salida=true);
  	ClrScr;
  	menu_principal();
  	clrscr;
  	readkey;
end;
end.
