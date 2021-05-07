Program mayorrr;

uses 
	crt;

const
	n = 5;

type
	t_dato = integer;
	t_vector = array[1..n] of t_dato;
	t_vector_2 = array[1..n] of t_dato;

var
	vector: t_vector;
	posicion:t_dato;
	mayor:t_dato;
	igual:t_dato;
	menor:t_dato;


procedure inicializar(var vec:t_vector);

var
	lim:1..n;

begin
	for lim:= 1 to n do
	begin
	vec[lim]:= 0;
	end;
end;

procedure cargar(var vec:t_vector);

	var
		lim:1..n;
		aux:t_dato;

begin
	for lim:=1 to n do
	begin
	writeln('Ingrese el componente N° ', lim,' del vector:');
	readln(aux);
	vec[lim]:=aux;
	end;
end;

procedure mayorr(var vec:t_vector;var posi: t_dato;var may:t_dato);
	var
		lim:1..n;

begin
	may:=vec[1];
	posi:=1;

	for lim := 2 to n do
	begin
	if (vec[lim] > may) then
		begin
			may:=vec[lim];
			posi:= lim;
		end;	
	end;

end;

procedure igualdad(var vec:t_vector;ig:t_dato;var men:t_dato);

var
	lim,i:1..n;

begin
	for lim:= 1 to n do
	begin
		for i:=2 to n do

			if (vec[lim]=vec[i]) and (lim <> i) then
			ig:= vec[lim];

			if  lim < i then
			begin
			menor:=lim;
			end
			else 
			menor:=i;
			
	end;
end;

begin
	inicializar(vector);
	cargar(vector);
	mayorr(vector,posicion,mayor);
	writeln('El mayor componente del vector es ', mayor,' y ocupa la posición N° ', posicion);
	igualdad(vector,igual,menor);
	writeln('El componente ',igual,' se repite, y la menor posicion del numero repetido es: ', menor);
	readkey;
end.