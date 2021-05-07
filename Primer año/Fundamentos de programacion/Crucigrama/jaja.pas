Program crucigrama_m;

uses crt,matriz;

const
	n :=11;
	m :=14;

type
	t_dato= string;
	t_matriz= array [1..n,1..m] of t_dato;

var
	opcion, lim: integer;
	salida: boolean;
	mat:t_matriz



procedure menu();

begin
	//COLOR DE FONDO
	textbackground (blue);
	clrscr;
	//COLOR DE TEXTO
	textcolor (lightgreen);
	gotoxy(15,0); writeln('-------------------------------------');
	gotoxy(15,1);writeln('|');
	gotoxy(51,1);writeln('|');
	textcolor(lightred + Blink);
	gotoxy(19,2);writeln(' BIENVENIDOS AL CRUCIGRAMA ');
	textcolor(lightgreen);
	gotoxy(15,2);writeln('|');
	gotoxy(51,2);writeln('|');
	gotoxy(15,3); writeln('------------------------------------');
	textcolor (lightgreen);
	gotoxy(15,3);writeln('|');
	gotoxy(51,3);writeln('|');
	textcolor(14+Blink);
	gotoxy(16,4);writeln('.1 ');
	textcolor(0);
	gotoxy(21,4);writeln(':Comenzar el crucigrama');
	textcolor(lightgreen);
	gotoxy(15,4);writeln('|');
	gotoxy(51,4);writeln('|');
	gotoxy(15,5); writeln('------------------------------------');
	gotoxy(15,5);writeln('|');
	gotoxy(51,5);writeln('|');
	textcolor(9+Blink);
	gotoxy(16,6);writeln('.2 ');
	textcolor(0);
	gotoxy(21,6);writeln(': Para salir          ');
	textcolor(lightgreen);
	gotoxy(15,6);writeln('|');
	gotoxy(51,6);writeln('|');
	gotoxy(16,7); writeln('-----------------------------------');
	gotoxy(15,7);writeln('|');
	gotoxy(51,7);writeln('|');
end;

procedure opciones(var opcion:integer);

begin

	case opcion of
		1 : 
		begin
			palabra_principal(mat);
		end;
		2 : 
		begin
			salida:=true;
			writeln('Usted ha salido del crucigrama.');
		end;
	end;
end;

procedure palabra_principal(var mat:t_matriz);
begin
	mat[1,8]:= 'I';
	mat[2,8]:= 'N';
	mat[3,8]:= 'F';
	mat[4,8]:= 'O';
	mat[5,8]:= 'R';
	mat[6,8]:= 'M';
	mat[7,8]:= 'A';
	mat[8,8]:= 'T';
	mat[9,8]:= 'I';
	mat[10,8]:= 'C';
	mat[11,8]:= 'A':
end;

procedure listar_palabra(var mat:t_matriz);
var
	i: Integer;
begin
for i:=1 to 11 do
	begin
		writeln(mat[i,8]);
	end;
end;

begin
	inicializar_matriz(mat);
	salida:=false;
	clrscr;
	menu();

	gotoxy(0,9); write('#Opcion: ');
	readln(opcion);
	clrscr;
			
	opciones(opcion);
	listar_palabra(mat);
end.	