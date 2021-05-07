Program Posgrado;

var 
	
	Titulo_grado,ingles,Especificacion: String;


	function Si_Cursa(Tit, Ingl, Especific:String): String;
	begin
		if (tit='Si') and(Ingl='Si') and (Especific='S.I') then
				
			Si_Cursa:=('Si cursa');
	end;
	
begin
	write('Ingrese si posee titulo de grado(Si/No): ');
	read(Titulo_grado);
	write('¿Tiene un nivel de idioma ingles?(Si/No): ');
	read(ingles);
	
	write('Ingrese cual es su especializacion:');
	read(Especificacion);

Si_Cursa(Titulo_grado, ingles, Especificacion);

resultado:= Si_Cursa;
write(Si_Cursa);
end.