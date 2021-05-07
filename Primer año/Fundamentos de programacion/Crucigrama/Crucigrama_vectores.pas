Program menu;

uses crt;

const
	n = 3;

type
     t_dato=string;
     t_vector=array [1..n] of t_dato;  

var 
	opcion, lim: integer;
	salida: boolean;
	vec, vec_pistas: t_vector;  
 

procedure menu();

begin
	//COLOR DE FONDO
	textbackground (5);
	clrscr;
	//COLOR DE TEXTO
	textcolor (3);
	gotoxy(15,0); writeln('----------------------------');
	gotoxy(15,1);writeln('|');
	gotoxy(43,1);writeln('|');
	textcolor(lightred + Blink);
	gotoxy(16,2);writeln(' BIENVENIDOS AL CRUCIGRAMA ');
	textcolor(3);
	gotoxy(15,2);writeln('|');
	gotoxy(43,2);writeln('|');
	gotoxy(15,3); writeln('----------------------------');
	textcolor (3);
	gotoxy(15,3);writeln('|');
	gotoxy(43,3);writeln('|');
	textcolor(yellow);
	gotoxy(16,4);writeln('.1 : Comenzar el crucigrama');
	textcolor(3);
	gotoxy(15,4);writeln('|');
	gotoxy(43,4);writeln('|');
	gotoxy(15,5); writeln('----------------------------');
	gotoxy(15,5);writeln('|');
	gotoxy(43,5);writeln('|');
	textcolor(yellow);
	gotoxy(16,6);writeln('.2 : Para salir          ');
	textcolor(3);
	gotoxy(15,6);writeln('|');
	gotoxy(43,6);writeln('|');
	gotoxy(16,7); writeln('---------------------------');
	gotoxy(15,7);writeln('|');
	gotoxy(43,7);writeln('|');
end;

procedure cargar_palabra (var vec:t_vector; var vec_pistas:t_vector; var lim:Integer);
var
     aux_palabra:t_dato;
     aux_pista:t_dato;
begin
lim:=0;
Write('Palabra: ');
readln(aux_palabra);
Write('Pista: ');
ReadLn(aux_pista);
     while (aux_palabra <> '') and (lim < n) do
          begin
               inc (lim);
               vec[lim]:=aux_palabra;
               vec_pistas[lim]:=aux_pista;
               Write('Palabra: ');
               readln(aux_palabra);
               Write('Pista: ');
               ReadLn(aux_pista);
          end;
end;      

procedure opciones(var opcion:integer);

begin

	case opcion of
		1 : 
		begin
			cargar_palabra(vec,vec_pistas,lim);
		end;
		2 : 
		begin
			salida:=true;
			writeln('Usted ha salido del crucigrama.');
		end;
	end;
end;

begin
	salida:=false;
	clrscr;
	menu();

	gotoxy(0,9); write('#Opcion: ');
	readln(opcion);
	clrscr;
			
	opciones(opcion);
end.	