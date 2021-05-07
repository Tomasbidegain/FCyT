Program empresas;

uses crt;

const
	n = 9;

type
	t_empresa = record
		apynom: string;
		cuidad: string;
		Clien_esp: string;
		monto_t: real;
		total_deuda:real;
	end;

	t_vector = array [1..n] of t_empresa;

var
	empre: t_empresa;
	vec: t_vector;
	buscado: string;
	lim,pos:word;

procedure inicializar_reg (var empre:t_empresa);
begin
    with empre do 
    begin
       	apynom:='';
        cuidad:='';
        Clien_esp:='';
        monto_t:=0;
        total_deuda:=0;
    end;
end;

procedure cargar_reg(var empre: t_empresa);
begin
	with empre do
	begin
		writeln('Ingrese su apellido y nombre: ');
		readln(apynom);
		writeln('Ingrese la cuidad en la que vive: ');
		readln(cuidad);
		writeln('Ingrese si es cliente especial o no: ');
		readln(Clien_esp);
		writeln('Ingrese el monto total de compra acumulada en 2018');
		readln(monto_t);
		writeln('Ingrese el total de deudas: ');
		readln(total_deuda);
	end;
end;
procedure inicializar_vec(var vec:t_vector);
var
	i: word;
begin
	for i:= 1 to n do
	inicializar_reg(vec[i]);
end;

procedure cargar_vec(var vec:t_vector; var lim:word);
var
	tecla: integer;
begin
	writeln('1. Para cargar.');
	writeln('2. Para dejar de cargar.');
	readln(tecla);
	while (tecla <> 2) and (lim < n) do
	begin
		inc(lim);
		cargar_reg (vec[lim]);
		writeln('1. Para cargar un nuevo cliente.');
		writeln('2. Para salir.');
		readln(tecla);
	end;
end;

procedure burbuja (var vec:t_vector; lim:word);

var
   i, j: word;
   aux: t_empresa;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].apynom > (vec[j+1].apynom))then
                  begin
                  aux:=vec[j];
                  vec[j]:=vec[j+1];
                  vec[j+1]:=aux;
                  end;
             end;
    end;
end;

procedure busqueda_bin (var vec:t_vector; buscado:string; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (vec[med].apynom = buscado) then
              pos:=med
           else
               begin
                    if (vec[med].apynom > buscado) then
                       ult:=med-1
                    else
                        pri:=med+1;
               end;
      end;
end;

procedure listar_reg(var empre:t_empresa);
begin
	with empre do
	begin
		writeln(apynom);
        writeln(cuidad);
        writeln(Clien_esp);
        writeln(monto_t);
      	writeln(total_deuda);
    end;
end;

procedure listar_vec(var vec:t_vector);
var
	i: word;
begin
	for i:= 1 to n do
	begin
		listar_reg(vec[i]);
	end;
end;



begin
	inicializar_vec (vec);
	writeln('Presione enter para comenzar.');
	readkey;
	clrscr;
	cargar_vec (vec,lim);
	writeln ('Para cargar un nuevo cliente primero debe verificar si ya existe.');
	burbuja (vec,lim);
	writeln('Ingrese el buscado: ');
	readln (buscado);
	busqueda_bin (vec,buscado,pos,lim);
	if pos = 0 then
	begin
		writeln('La persona que busca no se encuentra cargada.');
		cargar_vec (vec,lim);
	end
	else
	begin
		writeln('La persona que busca ya esta cargada.');
	end;	
	listar_vec (vec);
	readkey;
end.