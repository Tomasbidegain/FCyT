Unit SubmenuConsultasClientes;

interface

uses crt,unit_menu_principal,SubmenuCli,unitclientes_tp, registros;

procedure SubMenu_Consultas_c();

implementation

procedure SubMenu_Consultas_c();
var
	opcion: char;
	salida: boolean;
begin
	salida:= false;
	repeat
		textbackground(black);
		clrscr;
		//COLOR DE TEXTO
		textcolor (red);
		gotoxy(33,9); writeln('---------------------------------------------------------------------------');
		gotoxy(33,9);writeln('|');
		gotoxy(108,9);writeln('|');
		textcolor(green);
		gotoxy(47,10);writeln(' CONSULTAS DE CLIENTES ');
		textcolor(red);
		gotoxy(33,10);writeln('|');
		gotoxy(108,10);writeln('|');
		gotoxy(33,11); writeln('---------------------------------------------------------------------------');
		textcolor (red);
		gotoxy(33,11);writeln('|');
		gotoxy(108,11);writeln('|');
		gotoxy(34,12);textcolor(Green); write('.1 : '); textcolor(white); writeln('Listado de clientes ordenado por razon social.');
		textcolor(red);
		gotoxy(33,12);writeln('|');
		gotoxy(108,12);writeln('|');
		gotoxy(33,13); writeln('---------------------------------------------------------------------------');
		gotoxy(33,13);writeln('|');
		gotoxy(108,13);writeln('|');
		gotoxy(34,14);textcolor(Green); write('.2 : '); textcolor(white); writeln('Proyectos contratados por un cliente');
		textcolor(red);
		gotoxy(33,14);writeln('|');
		gotoxy(108,14);writeln('|');
		gotoxy(34,15); writeln('--------------------------------------------------------------------------');
		gotoxy(33,15);writeln('|');
		gotoxy(108,15);writeln('|');
		gotoxy(34,16);textcolor(Green); write('.3 : '); textcolor(white); writeln('Volver .');
		textcolor(red);
		gotoxy(33,16);writeln('|');
		gotoxy(108,16);writeln('|');
		gotoxy(33,17); writeln('--------------------------------------------------------------------------');
		gotoxy(33,19); write('# Opcion: ');
		opcion := readkey();
	    case opcion of
		 '1':begin
		  		ordenar(cliente);
		  		mostrar_c(reg_cliente, cliente);
		  	end;
		'2':begin
				textbackground(black);clrscr;
		 		p_contratados(cliente);
			end;

		'3':begin
				Salida:= true;
			end;
		end;  
  	Until (Salida=true);
  	ClrScr;
  	submenuClien();
  	clrscr;
  	readkey;
end;
end.
