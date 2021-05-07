unit uvectores;
interface
uses crt;
const
n=2800;

type
t_dato=real;
t_vector=array [1..n] of t_dato;

procedure inicializar (var v:t_vector);
procedure cargar (var v:t_vector);
procedure cargar_2 (var v:t_vector; var lim:word);
procedure listado (var v:t_vector; lim:word);
procedure ordenamiento_burbuja (var v:t_vector; lim:word);
procedure busqueda_sec_mejorada (var v:t_vector; buscado:t_dato; var pos:word; lim:word);
procedure busqueda_bin (var v:t_vector; buscado:t_dato; var pos:word; lim:word);

implementation

procedure inicializar(var v:t_vector);
var
   i: 1..n ;

begin
for i:= 1 to n do
v[i]:=0;
end;

procedure cargar(var v:t_vector);
var
   i:1..n;

begin
for i:= 1 to n do
readln(v[i]);
end;

procedure cargar_2 (var v:t_vector; var lim:word);
var
   i:word;
   aux:t_dato;

begin
i:=0;
readln(aux);
while (i<n) and (aux<>0) do
      begin
           i:=i+1;
           v[i]:=aux;
           readln(aux);
      end;
    lim:=i;
end;

procedure listado (var v:t_vector; lim:word);
var
   i:word;

begin
for i:= 1 to lim do
writeln(v[i]);
end;

procedure ordenamiento_burbuja (var v:t_vector; lim:word);
var
   i, j, aux: word;

begin
for i:= 1 to lim-1 do
    begin
         for j:= 1 to lim-i do
             begin
                  if (v[j]>v[j+1]) then
                  aux:=v[j];
                  v[j]:=v[j+1];
                  v[j+1]:=aux;
             end;
    end;
end;

procedure busqueda_sec_mejorada (var v:t_vector; buscado:t_dato; var pos:word; lim;word);
var
   i:word;

begin
i:=1;
while (i<=lim) and (pos=0) do
      begin
           if (v[i]=buscado) then
              pos:=i;
           else
               i:=i+1;
      end;
end;

procedure busqueda_bin (var v:t_vector; buscado:t_dato; var pos:word; lim:word);
var
   pri, ult, med: word;

begin
pri:=1;
ult:=lim;
pos:=0;
while (pri<=ult) and (pos=0) do
      begin
           med:=(pri+ult)div 2;
           if (v[med]=buscado) then
              pos:=med;
           else
               begin
                    if (v[med]>buscado) then
                       ult:=med-1;
                    else
                        pri:=med+1;
               end;
      end;
end;

end.