Program Ej1;

uses crt,matriz;

const
	n=25;
	m=4;

type
	t_dato = integer;
	t_matriz = array [1..n, 1..m] of t_dato;

var
	mat:t_matriz;
	suma: real;
	prome: real;

 procedure sumar(var mat:t_matriz; var promed:real; suma:real);
 var
 	i,j: t_dato;

begin

	for i:= 1 to m do
	begin
		for j := 1 to n do
		begin
			suma:= (suma + mat[i,j]);
			promed:= (suma/(n*m));
		end;
	end;

end;

begin
	inicializar_matriz (mat);
	cargar_matriz(mat);
	sumar(mat,prome,suma);
	writeln('La media es: ', prome);

end.