Program facturas;

uses crt;

const
	n =3 ;

type
	t_documentos=record
		razon_s: string;
		monto:real;
	end;
	t_vector = array[1..n] of t_documentos;
var 
	doc:t_documentos;
	vec:t_vector;

procedure inicializar_reg(var doc: t_documentos);

begin
	with doc Do
	begin
		razon_s:='';
		monto:=0;
	end;
end;

procedure cargar_reg(var doc: t_documentos);

begin
	with doc Do
	begin
		write('Ingrese su razon social:');
		readln(razon_s);
		writeln('Ingrese su monto:');
		readln(monto);
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

procedure burbuja (var doc:t_documentos; var vec:t_vector; lim:integer);

var
   i, j, aux: word;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (vec[j].razon_s > (vec[j+1].razon_s) then
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
           if (vec[med].razon_s = buscado) then
              pos:=med;
           else
               begin
                    if (vec[med].razon_s > buscado) then
                       ult:=med-1;
                    else
                        pri:=med+1;
               end;
      end;
end;

procedure dar_alta(var vec:t_vector;documento:real;lim:integer);
begin
	busqueda_bin (vec,buscado,pos,lim);
	if pos <> 0 then
	begin
		if (documento < 0 ) then
		begin
			vec[pos].monto:= vec[pos].monto - documento;
		end
		else
		    vec[pos].monto:=vec[pos].monto + documento;
	end
	else 
	begin
	if (pos = 0) and (lim < n) then
	begin
		inc(lim);
		cargar_reg(doc);
		burbuja(doc,vec,lim);
	end;
end;

burbuja(doc,vec,lim);

procedure listado_clientes_neg();
begin
	
end;

		
