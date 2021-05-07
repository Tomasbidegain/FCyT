Program Productoria;

uses 
crt;

const 
n=5;

type
t_dato = integer;

t_vector = array[1..n] of t_dato;

var
vector:t_vector;
lim:t_dato;
producto:real;

procedure inicializacion (var vec:t_vector);

var
i:integer;


begin

for i:=1 to n do
begin
vec[i]:=0;
end;
end;


procedure cargar(var vec:t_vector; var lim:integer);

var
aux:t_dato;

begin
writeln('Ingrese las componentes del vector');
read(aux);
while ((lim>0)and(aux > 0)) do
begin
lim:=lim+1;
vec[lim]:= aux;
read(aux);
end;
end;

procedure product (var vec:t_vector; lim:integer; var producto:real);
begin
producto:=1;
for lim:= 1 to lim do
begin
Producto:=(Producto*vec[lim]);
end;

end;



begin
inicializacion(vector);
 lim:=1;
cargar(vector,lim);

product(vector,lim,producto);
writeln('La productoria de las componentes del vector es: ', Producto:2:2);

readkey;
end.