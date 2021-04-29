unit unit_menu_principal;

Interface

Uses crt;

var
	opcion:char;
	salida:boolean;

procedure menu_principal();

Implementation

Uses 
	submenuPro,SubmenuCli,unitproyectos;

procedure menu_principal();
var opcion: char;
	salida: boolean;
begin
	Salida:= false;

  	Repeat
	    ClrScr;
		//COLOR DE FONDO
		textbackground (black);
		clrscr;
		//COLOR DE TEXTO
		textcolor (blue);
		gotoxy(38,9); writeln('-------------------------------------------------------');
		gotoxy(37,9);writeln('|');
		gotoxy(92,9);writeln('|');
		textcolor(red);
		gotoxy(48,10);writeln(' GESTION DE PROYECTOS DE SOFTWARE ');
		textcolor(blue);
		gotoxy(37,10);writeln('|');
		gotoxy(92,10);writeln('|');
		gotoxy(37,11); writeln('-------------------------------------------------------');
		textcolor (blue);
		gotoxy(37,11);writeln('|');
		gotoxy(92,11);writeln('|');
		textcolor(white);
		gotoxy(38,12);textcolor(red);write('.1 ');textcolor(white);write(': Proyectos de software');
		textcolor(blue);
		gotoxy(37,12);writeln('|');
		gotoxy(92,12);writeln('|');
		gotoxy(37,13); writeln('-------------------------------------------------------');
		gotoxy(37,13);writeln('|');
		gotoxy(92,13);writeln('|');
		textcolor(white);
		gotoxy(38,14);textcolor(red);write('.2 ');textcolor(white);write(': Clientes          ');
		textcolor(blue);
		gotoxy(37,14);writeln('|');
		gotoxy(92,14);writeln('|');
		gotoxy(38,15); writeln('------------------------------------------------------');
		gotoxy(37,15);writeln('|');
		gotoxy(92,15);writeln('|');
		textcolor(white);
		gotoxy(38,16);textcolor(red);write('.3 ');textcolor(white);write(': Salir          ');
		textcolor(blue);
		gotoxy(38,17); writeln('------------------------------------------------------');
		gotoxy(37,16);writeln('|');
		gotoxy(92,16);writeln('|');
		gotoxy(37,17);writeln('|');
		gotoxy(92,17);writeln('|');
		gotoxy(37,18); write('# Opcion: ');
		opcion:= readkey;
	    case opcion of
		'1':begin
				gotoxy(38,12);textcolor(red);write('.1 : Proyectos de software');
				delay(250);
		  		submenuProy();
		  	end;
		'2':begin
				gotoxy(38,14);textcolor(red);write('.2 : Clientes');
				delay(250);
				submenuClien();	 
		  	end;
		'3':begin
				gotoxy(38,16);textcolor(red);write('.3 : Salir');
				delay(250);
			 	Salida:= true;
			end;
		end;  
	Until (Salida=true);
end;
end.