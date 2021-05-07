Program Anios;

var 
	anio: integer;
	texto: String;
	NumeroACadena: String;

begin
	
	Write('ingrese el año en que nacio:');
	read(anio);

	str (anio, texto);

	NumeroACadena:= texto;

	Write('el año en que nacio es:', NumeroACadena);

end.