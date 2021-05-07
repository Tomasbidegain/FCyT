Program crucigrama_m;

uses crt;

const
	n =11;
	m =51;

type
	t_dato1=integer;
	t_dato= string;
	t_matriz= array [1..n,1..m] of t_dato;
	t_vector= array[1..n] of t_dato;
	t_vector1 = array[1..n] of t_dato1;

var
	palabra,letra:string;
	error,posicion: word;
	opcion: integer;
	mat:t_matriz;
	op:char;
	vec_palabras, vec_usuario,palabras_:t_vector;
	vec_espacios_derecha, vec_espacios_izquierda:t_vector1;

procedure inicializar(var vec_palabras,vec_usuario,palabras_:t_vector;var vec_espacios_derecha,vec_espacios_izquierda:t_vector1);									//INICIALIZAR VECTOR
var
   i: 1..n ;

begin
for i:= 1 to n do
	begin
		vec_palabras[i]:='';
		vec_usuario[i]:='';
		palabras_[i]:='';
	end;
end;

procedure vector_palabras (var vec_palabras:t_vector);							    //VECTOR PALABRAS
begin
	vec_palabras[1]:= 'binario';
	vec_palabras[2]:= 'inteligencia';
	vec_palabras[3]:= 'firewall';
	vec_palabras[4]:= 'formato';
	vec_palabras[5]:= 'compilar';
	vec_palabras[6]:= 'matriz';
	vec_palabras[7]:= 'hardware';
	vec_palabras[8]:= 'tecnologia';
	vec_palabras[9]:= 'periferico';
	vec_palabras[10]:= 'almacenamiento';
	vec_palabras[11]:= 'software';
end;

procedure vector_espacios(var vec_espacios_izquierda:t_vector1; var vec_espacios_derecha:t_vector1);
begin
	vec_espacios_izquierda[1]:=26;
	vec_espacios_izquierda[2]:=26;
	vec_espacios_izquierda[3]:=27;
	vec_espacios_izquierda[4]:=26;
	vec_espacios_izquierda[5]:=20;
	vec_espacios_izquierda[6]:=27;
	vec_espacios_izquierda[7]:=26;
	vec_espacios_izquierda[8]:=27;
	vec_espacios_izquierda[9]:=24;
	vec_espacios_izquierda[10]:=23;
	vec_espacios_izquierda[11]:=22;
	vec_espacios_derecha[1]:=5;
	vec_espacios_derecha[2]:=0;
	vec_espacios_derecha[3]:=3;
	vec_espacios_derecha[4]:=5;
	vec_espacios_derecha[5]:=10;
	vec_espacios_derecha[6]:=5;
	vec_espacios_derecha[7]:=4;
	vec_espacios_derecha[8]:=1;
	vec_espacios_derecha[9]:=4;
	vec_espacios_derecha[10]:=1;
	vec_espacios_derecha[11]:=8;

end;

procedure vec_usua(var vec_usuario:t_vector; var vec_palabras:t_vector);
var
	i,j,aux: Integer;

begin
	for i:= 1 to n do
	begin
		aux := Length(vec_palabras[i]);
		for j := 1 to aux do
		begin
			insert('_', vec_usuario[i], i);
		end;
	end;
end;

procedure inicializar_matriz (var mat:t_matriz);						            //INICIO DE MATRIZ
	var
		i,j:integer;

begin
	for i:=1 to n do
		begin
		for j := 1 to m do
			begin
			mat[i,j]:='';	
			end;
		end;	
end;

procedure menu();																	//MENU

begin
	textbackground (blue);															//COLOR DE FONDO
	clrscr;
	textcolor (lightgreen);															//COLOR DE TEXTO
	gotoxy(15,1); writeln('-------------------------------------');
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

procedure cargar_matriz(var vec_usuario:t_vector; var mat:t_matriz; vec_espacios_derecha,vec_espacios_izquierda: t_vector1);
var
	i,j,k,l,aux: Integer;

begin
	for i:= 1 to n do
	begin
		aux:= Length(vec_usuario[i]);
		for j := 1 to vec_espacios_izquierda[i] do
		begin
			mat[i,j]:=' ';
		end;
		for k := 1 to aux do
		begin
			mat[i,vec_espacios_izquierda[i]+k] := vec_usuario[i][k]; 
		end;
		for l:= 1 to vec_espacios_derecha[i] do
		begin
			mat[i,vec_espacios_izquierda[i]+aux+l] := ' ';
		end;
	end;
end;

procedure palabra_principal(var mat:t_matriz);
begin
	mat[1,28]:= 'I';
	mat[2,28]:= 'N';            												//CARGO LA PALABRA PRINCIPAL EN LA MATRIZ
	mat[3,28]:= 'F';
	mat[4,28]:= 'O';
	mat[5,28]:= 'R';
	mat[6,28]:= 'M';
	mat[7,28]:= 'A';
	mat[8,28]:= 'T';
	mat[9,28]:= 'I';
	mat[10,28]:= 'C';
	mat[11,28]:= 'A';
end;

procedure listar_palabra(var mat:t_matriz);
var
	i,j: Integer;
begin
	gotoxy(22,1); textcolor(lightred);writeln('--------------');
	gotoxy(24,2);textcolor(lightgreen + blink);writeln('CRUCIGRAMA');		//MUESTRO LA PALABRA EN PANTALLA
	gotoxy(22,2);textcolor(lightred);writeln('|');
	gotoxy(35,2); writeln('|');
	gotoxy(22,3); writeln('--------------');
	for i:=1 to n do
	begin
		for j := 1 to m do
		begin
			textcolor(yellow);
			write(mat[i,j]);
			if (j=51) then
			writeln();
		end;
	end;
end;

procedure opciones(var opcion:integer);

begin

	case opcion of		
		1 : 																//OPCIONES							
		begin
			cargar_matriz(vec_usuario,mat,vec_espacios_derecha,vec_espacios_izquierda);
			palabra_principal(mat);
			listar_palabra(mat);
		end;
		2 : 
		begin
			writeln('Usted ha salido del crucigrama.');
		end;
	end;
end;

procedure letra_usuario(var vec_palabras,vec_usuario:t_vector; var error: word; posicion:word; var letra:string);
var
	i,j,aux: integer;
	aciertos: boolean;
begin
	aux:=0;
	aciertos:=false;
	for posicion:= 1 to n do
	begin
		for i:= 1 to Length(vec_palabras[posicion]) do
		begin
			if (vec_palabras[posicion][i] = letra) then
			begin
				aciertos:=true;
				delete (vec_usuario[posicion],i,1);
                 insert(letra,vec_usuario[posicion],i);
			end
			else
			if vec_usuario[posicion][i]=vec_palabras[posicion][i] then
			begin
				inc(aux);
			end;
		end;
	end;

	if (aciertos=false) then
	inc (error);
end;

procedure palabra_usuario(var vec_palabras:t_vector; var vec_usuario:t_vector; var palabra:string);
var
	i:integer;
	posicion:word;

begin
	i:=0;
	for posicion:= 1 to n do
	if (vec_palabras[posicion] <> palabra) then
	begin
		clrscr;
		writeln('PERDISTE Dx');
	end;
	if (vec_palabras[posicion][i] = palabra) then
	begin
		vec_usuario[posicion][i] := palabra[i];
	end;
end;

procedure jugar();
begin
	gotoxy(1,20);writeln('Presione "L" para ingresar por letras, o presione "P" para arriesgar una palabra.');
	readln(op);
	case op of
	'L' : 
		begin
			read(letra);
			letra_usuario(vec_palabras,vec_usuario,error,posicion,letra);
		end;
	'P' :
		begin
			palabra_usuario(vec_palabras, vec_usuario,palabra);
		end;
	end;
end;

//CUERPO PRINCIPAL

begin
	inicializar(vec_palabras,vec_usuario,palabras_,vec_espacios_izquierda,vec_espacios_derecha);
	vector_palabras(vec_palabras);
	vector_espacios(vec_espacios_izquierda,vec_espacios_derecha);
	vec_usua(vec_usuario,vec_palabras);
	inicializar_matriz(mat);
	clrscr;
	menu();
	gotoxy(1,9); write('#Opcion: ');
	readln(opcion);
	clrscr;
	opciones(opcion);
	jugar();
end.
