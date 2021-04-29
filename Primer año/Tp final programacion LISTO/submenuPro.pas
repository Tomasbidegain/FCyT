unit submenuPro;

Interface

uses crt,unit_menu_principal,unitproyectos,registros;

procedure submenuProy();
procedure Carga_correcta_proyecto();

implementation 

uses 
	SubmenuConsultas;
	
procedure submenuProy();
var 
	opcion: char;
	salida: boolean;
begin
	salida:= false;
	repeat
	textbackground (black);
		clrscr;
		//COLOR DE TEXTO
		textcolor (10);
		gotoxy(38,9); writeln('-------------------------------------------------------');
		gotoxy(37,9);writeln('|');
		gotoxy(92,9);writeln('|');
		textcolor(5);
		gotoxy(50,10);writeln('    PROYECTOS DE SOFTWARE ');
		textcolor(10);
		gotoxy(37,10);writeln('|');
		gotoxy(92,10);writeln('|');
		gotoxy(37,11); writeln('-------------------------------------------------------');
		gotoxy(37,11);writeln('|');
		gotoxy(92,11);writeln('|');
		gotoxy(38,12);textcolor(5);write('.1 :');textcolor(white);write(' Alta proyecto.');
		textcolor(10);
		gotoxy(37,12);writeln('|');
		gotoxy(92,12);writeln('|');
		gotoxy(37,13); writeln('-------------------------------------------------------');
		gotoxy(37,13);writeln('|');
		gotoxy(92,13);writeln('|');
		gotoxy(38,14);textcolor(5);write('.2 :');textcolor(white);write(' Modificar proyecto.');
		textcolor(10);
		gotoxy(37,14);writeln('|');
		gotoxy(92,14);writeln('|');
		gotoxy(38,15); writeln('------------------------------------------------------');
		gotoxy(37,15);writeln('|');
		gotoxy(92,15);writeln('|');
		gotoxy(38,16);textcolor(5);write('.3 :');textcolor(white);write(' Consultas.');
		textcolor(10);
		gotoxy(38,17); writeln('------------------------------------------------------');
		gotoxy(37,16);writeln('|');
		gotoxy(92,16);writeln('|');
		gotoxy(37,17);writeln('|');
		gotoxy(92,17);writeln('|');
		gotoxy(38,18);textcolor(5);write('.4 :');textcolor(white);write(' Dar de baja un proyecto.');
		textcolor(10);
		gotoxy(38,19); writeln('------------------------------------------------------');
		gotoxy(37,18);writeln('|');
		gotoxy(92,18);writeln('|');
		gotoxy(37,19);writeln('|');
		gotoxy(92,19);writeln('|');
		gotoxy(38,20);textcolor(5);write('.5 :');textcolor(white);write(' Volver al menu principal.');
		textcolor(10);
		gotoxy(38,21); writeln('------------------------------------------------------');
		gotoxy(37,20);writeln('|');
		gotoxy(92,20);writeln('|');
		gotoxy(37,21);writeln('|');
		gotoxy(92,21);writeln('|');
		gotoxy(37,23); write('# Opcion: ');
		opcion := readkey();
	    case opcion of
		'1'	:begin
				gotoxy(38,12);textcolor(5);write('.1 : Alta proyecto.');
				delay(250);
		  		Alta_Proyecto(f_proyecto);
		  	end;
		'2':begin
				gotoxy(38,14);textcolor(5);write('.2 : Modificar proyecto.');
				delay(250);
				modificacion_proyectos(f_proyecto, id_buscado);	 
			end;

		'3':begin
				gotoxy(38,16);textcolor(5);write('.3 : Consultas.');
				delay(250);
				SubMenu_Consultas();
			end;
		'4':begin
				gotoxy(38,18);textcolor(5);write('.4 : Dar de baja un proyecto.');
				delay(250);
				bajas(f_proyecto);
			end;
		'5':begin
				gotoxy(38,20);textcolor(5);write('.5 : Volver al menu principal.');
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
procedure Carga_correcta_proyecto();
begin
	gotoxy(28,12);writeln('************************************************************');
	gotoxy(28,13);writeln('*');								   gotoxy(88,13);writeln('*');
	gotoxy(30,13);writeln(' Su proyecto ha sido cargado correctamente en el sistema.');
	gotoxy(28,14);writeln('************************************************************');
end;
end.