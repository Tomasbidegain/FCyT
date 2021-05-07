Program guardias;
var
	apynom,obra_social,diagnostico,medico: string;
	cont_obra_socialx,cont_obra_sociale, cont_obra_socialz, contiosper,cont_pacientesx,cont_pacientese,cont_pacientesz, dni: integer;
	suma, montox,montoe,montoz,costo_consulta: real;
	tecla:char;
begin
	write('Presione cualquier tecla para continuar.');
	read(tecla);
	while tecla <> '' do
	begin
		write('Ingrese su nombre y apellido: '); read(apynom);
		write('Ingrese su dni'); read(dni);
		write('Ingrese su obrea social: '); readln(obra_social);
		write('Ingrese cual es su diagnostico'); read(diagnostico);
		write('Ingrese el costo de su consulta'); read(costo_consulta);
		write('Ingrese cual es su medico(X/E/Z) :');  read(medico);

		if (medico = 'X') then
		begin
		cont_pacientesx:= cont_pacientesx+1;
		montox:=montox+costo_consulta;
		end

		else 
		 
			if (medico='E') then
			begin	
			 	cont_pacientese := cont_pacientese+1;
			 	montoe := montoe+costo_consulta;
			end	 
		 

		 else
		    begin
		  		cont_pacientesz := cont_pacientesz+1;
		  		montoz := montoz+costo_consulta;
			end;

		if (obra_social='IOSPER') then
			contiosper:= contiosper+1;

		if (obra_social='No tengo') and (medico='X') then
		cont_obra_socialx:=cont_obra_socialx+1;

		if (obra_social='No tengo') and (medico='E') then
		cont_obra_sociale:=cont_obra_sociale+1;

		if (obra_social='No tengo') and (medico='Z') then
		cont_obra_socialz:=cont_obra_socialz+1;

		if (medico='E') and (diagnostico='SS') then
			begin
				write('Apellido y nombre: ', apynom);
				write('DNI: ', dni);
				write('Obra social: ' ,obra_social);
				write('Diagnostico: ' ,diagnostico);
				write('Costo de su consulta', costo_consulta);
				write('Medico: ', medico);
			end;

		write('Presione cualquier tecla para continuar.');
		read(tecla);
	end;
	suma:=(montox+montoe)+montoz;
	write('el porcentaje del medico X es: ',(montox*100)/suma);
	write('el porcemtmaje del medico E es: ', (montoe*100)/suma);
	write('el porcentaje del medico Z es: ',(montoz*100)/suma);
	write('la cantidad de pacientes con obra social IOSPER son: ',contiosper);
end.