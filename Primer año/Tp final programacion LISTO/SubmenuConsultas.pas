Unit SubmenuConsultas;

interface

uses crt,unit_menu_principal,submenuPro,unitproyectos, registros;

procedure SubMenu_Consultas();

implementation

procedure SubMenu_Consultas();
var
	opcion: char;
	salida: boolean;
begin
	salida:= false;
	repeat
	textbackground(black);
		clrscr;
		//COLOR DE TEXTO
		textcolor(10);
		gotoxy(33,9); writeln('---------------------------------------------------------------------------');
		gotoxy(33,9);writeln('|');
		gotoxy(108,9);writeln('|');
		textcolor(5);
		gotoxy(47,10);writeln(' CONSULTAS DE PROYECTOS SOFTWARE ');
		textcolor(10);
		gotoxy(33,10);writeln('|');
		gotoxy(108,10);writeln('|');
		gotoxy(33,11); writeln('---------------------------------------------------------------------------');
		textcolor (10);
		gotoxy(33,11);writeln('|');
		gotoxy(108,11);writeln('|');
		gotoxy(34,12);textcolor(5); write('.1 : '); textcolor(white); writeln('Listado de proyectos de software ordenado por titulo.');
		textcolor(10);
		gotoxy(33,12);writeln('|');
		gotoxy(108,12);writeln('|');
		gotoxy(33,13); writeln('---------------------------------------------------------------------------');
		gotoxy(33,13);writeln('|');
		gotoxy(108,13);writeln('|');
		gotoxy(34,14);textcolor(5); write('.2 : '); textcolor(white); writeln('Proyectos ordenados por titulo exportados en un rango de fechas');
		textcolor(10);
		gotoxy(33,14);writeln('|');
		gotoxy(108,14);writeln('|');
		gotoxy(34,15); writeln('--------------------------------------------------------------------------');
		gotoxy(33,15);writeln('|');
		gotoxy(108,15);writeln('|');
		gotoxy(34,16);textcolor(5); write('.3 : '); textcolor(white); writeln('Volver');
		textcolor(10);
		gotoxy(34,17); writeln('--------------------------------------------------------------------------');
		gotoxy(33,16);writeln('|');
		gotoxy(108,16);writeln('|');
		gotoxy(33,17);writeln('|');
		gotoxy(108,17);writeln('|');
		gotoxy(33,19); write('# Opcion: ');
		opcion:= readkey;
	    case opcion of
		 '1':begin
		 		gotoxy(34,12);textcolor(5); write('.1 : Listado de proyectos de software ordenado por titulo.');
		 		delay(250);
			  	ordenar_titulo(f_proyecto);
			  	textbackground(black);clrscr;
				mostrar_p(f_proyecto);
		  	end;
		 '2':begin
		 		gotoxy(34,14);textcolor(5); write('.2 : Proyectos ordenados por titulo exportados en un rango de fechas');
		  	    delay(250);
		  	    rango_de_fechas(f_proyecto);
		  	end;

		 '3':begin
		 		gotoxy(34,16);textcolor(5); write('.3 : Volver');
		 		delay(250);
		 		Salida:= true;
			end;
		end;  
  	Until (Salida=true);
  	ClrScr;
  	submenuProy();
  	clrscr;
  	readkey;
end;
end. 