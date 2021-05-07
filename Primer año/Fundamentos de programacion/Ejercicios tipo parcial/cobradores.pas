program cobradores;

uses crt;

const
	n = 5;

type
	t_cob = record
		cod_cobrador : real;
		barrio: string;
		apynom_socio: string;
		cuota: real;
	end;

	t_vector = array[1..n] of t_cob;

var
	cob: t_cob;
	vec: t_vector;
	lim: integer;
	buscado:string;
	cuo:real;
	pos:word;

procedure inicializar_reg(var cob: t_cob);

begin
	with cob Do
	begin
		cod_cobrador :=0;
		barrio:='';
		apynom_socio:='';
		cuota:=0;
	end;
end;

procedure cargar_reg(var cob: t_cob);

begin
	with cob Do
	begin
		write('Ingrese el codigo de comprador:');
		readln(cod_cobrador);
		write('Ingrese el barrio:');
		readln(barrio);
		writeln('Ingrese el apellido y nombre del socio:');
		readln(apynom_socio);
		write('Ingrese la cuota: ');
		readln(cuota);
	end;
end;

procedure inicializar_vec(var vec: t_vector);

var
	i: integer;
begin
	for i:= 1 to n do
	begin
		inicializar_reg(vec[i]);
	end;
end;

procedure cargar_vec(var vec: t_vector; var lim:integer);
var
	tecla: string;

begin
	writeln('Ingrese una tecla para comenzar a cargar.');
	readln(tecla);
	lim:=0;
	while (lim<n) and (tecla <> '') do
	begin
		cargar_reg(vec[lim]);
		inc (lim);		
		read(tecla);
	end;	
end;

procedure burbuja (var cob:t_cob; var vec:t_vector; lim:integer);

var
   i, j, aux: word;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].barrio + vec[j].apynom_socio) > (vec[j+1].barrio + vec[j+1].apynom_socio) then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure listar_vec(var cob:t_cob);
var
	i: Integer;

begin
	for i:= 1 to n Do
	begin
		with cob do
		begin
		writeln (barrio + apynom_socio);
	end;
	end;
end;

procedure busqueda_bin (var vec:t_vector; buscado:string; var pos:word; lim:word; var cuo:real;);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
buscado:='Puerto viejo';
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].barrio = buscado) then
              pos:=med;
              cuo:= vec[med].cuota
           else
               begin
                    if (vec[med].barrio > buscado) then
                       ult:=med-1;
                       cuo:= vec[med-1].cuota
                    else
                        pri:=med+1;
                        cuo:= vec[med+1].cuota
               end;
      end;
end;

