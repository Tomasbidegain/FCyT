unit Validaciones;

interface

uses crt,registros;

procedure validar_email(var email:string; var valido_e:boolean; var x: word; var y:word );
procedure validar_telefono(var tel: string;var valida: boolean);
procedure validar_cuit(var cuit: string; var valida_c: boolean);
procedure titulo_mayus(var reg_proyecto:t_proyec);



implementation
	
procedure titulo_mayus(var reg_proyecto:t_proyec);
const
	minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
begin

	if reg_proyecto.titulo[1] in minusculas then
		reg_proyecto.titulo[1]:= upcase(reg_proyecto.titulo[1]);

end;
procedure validar_email(var email:string; var valido_e:boolean; var x: word; var y:word );
const
	validos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','.','_','-','0','1','2','3','4','5','6','7','8','9'];

var
	i,j,k,largo_e,p: integer;
	apto: boolean;

begin
	valido_e:=false;
	apto:= false;
	repeat
		for i := 1 to length(email) do 
		begin
			if (email[i] in validos) then
			begin
				apto:=true;
			end
			else 
				if not (email[i] in validos) then
				begin
					repeat
						gotoxy(x+98,y+2);write('                            ');
						gotoxy(x+98,y+2);read(email);
					until (email[i] in validos);
					apto:=true;
				end;
		end;
		j:= Pos('@',email);
		p:= pos('..',email);
		{Tiene que existir un arroba, antes del arroba tiene que haber algo y no puede haber dos puntos seguidos.}
		if (j = 0) or (j=1) or (p <> 0) then
		begin
			repeat
				gotoxy(x+98,y+2);write('                            ');
				gotoxy(x+98,y+2);readln(email);
			Until (j > 2) or (p = 0 );
		end
		else
		begin
			k:= Pos('.com',email);
			largo_e:= length(email);
			if (apto = true) and (k <> 0) and (k >= (largo_e - 4)) then
				valido_e:=true
			else
			begin
				if (k = 0) or (k < (largo_e - 4)) then
				begin
					repeat
						gotoxy(x+98,y+2);write('                            ');
						gotoxy(x+98,y+2);readln(email);
						k:= Pos('.com',email);	
					until (k <> 0);
					valido_e := true;
				end;
			end;
		end;
	until valido_e;
end;

procedure validar_telefono(var tel: string;var valida: boolean);

const validos = ['0','1','2','3','4','5','6','7','8','9'];

var
	i: Integer;
	

begin
	valida := false;
	if (length(tel) = 10) then
	begin
		for i := 1 to length(tel) do  
		begin
			 if (tel [i] in validos) then
			 	valida := true
			 else
			 	valida := false;
		end;	
	end;
end;

procedure validar_cuit(var cuit: string; var valida_c: boolean);

const validos = ['0','1','2','3','4','5','6','7','8','9','-'];

var
	i,largo: Integer;
	
begin
	largo:=0;
	largo:= length(cuit);
	valida_c:=false;
	if (largo = 13) then
	begin
        valida_c := True;
		for i := 1 to largo do  
		begin
			 if not (cuit [i] in validos) then
			 	valida_c := False
		end;	
	end;
end;

end.