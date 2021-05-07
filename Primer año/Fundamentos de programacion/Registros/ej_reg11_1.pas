Program ej_1;

uses crt;

const
    n=10;

type
    t_personas= record
        nom:string;
        edad:integer;
        peso:real;
        sexo:string;
        altura:real;
        piel:string;
        ojos:string;
        nac:string;
    end;
    
    t_vector=array [1..n] of t_personas;

var
    r:t_personas;
    v:t_vector;
    c_60,c_arg,c_cub,c_kilos,c_muj,c_ojos:integer;

//PROCEDIMIENTOS

procedure inicializar_reg (r:t_personas);
begin
    with r do 
    begin
        nom:='';
        edad:=0;
        peso:=0;
        sexo:='';
        altura:=0;
        piel:='';
        ojos:='';
        nac:='';
    end;
end;

procedure cargar_reg (r:t_personas);
begin
    with r do
    begin
        write('nombre: ');
        readln(nom);
        write('edad: ');
        readln(edad);
        write('peso: ');
        readln(peso);
        write('sexo: ');
        readln(sexo);
        write('altura: ');
        readln(altura);
        write('color de piel: ');
        readln(piel);
        write('color de ojos: ');
        readln(ojos);
        write('nacionalidad: ');
        readln(nac);
    end;
end;

procedure inicializar_vec (v:t_vector);
var
    i:integer;
begin
    for i:= 1 to n do
    begin  
        inicializar_reg (v[i]);
    end;
end;

procedure cargar_vec (v:t_vector);
var
    i:integer;
begin
    for i:= 1 to n do
    begin  
        cargar_reg (v[i]);
    end;
end;

procedure sesenta (var v:t_vector; var c_60:integer);

var
    i:integer;

begin
    c_60:=0;
    for i:=1 to n do
    begin
        if (v[I].edad > 60) then
            inc (c_60);
    end;
end;

procedure mujeres (var v:t_vector; var c_muj:integer);
var
    i:integer;
Begin
    c_muj:=0;
    for i:=1 to n do
    begin
        if (v[i].altura >= 170) and (v[i].sexo ='mujer') then
            inc (c_muj);
    end;
End;

procedure kilos (var v:t_vector; var c_kilos:integer);
var
    i:integer;
Begin
    c_kilos:=0;
    for I:=1 to n do
    begin
        if (v[i].peso <= 50) then
            inc (c_kilos);
    end;
End;

procedure cubanos (var v:t_vector; var c_cub:integer);
var
    i:integer;
Begin
    c_cub:=0;
    for I:=1 to n do
    begin
        if (v[i].nac ='Cubano') and (v[i].sexo ='hombre') then
            inc (c_cub);
    end;
End;

procedure argentinas (var v:t_vector; var c_arg:integer);
var
    i:integer;
Begin
    c_arg:=0;
    for i:=1 to n do
    begin
        if (v[i].nac ='Argentina') and (V[i].sexo ='mujer') then
            inc (c_arg);
    end;
End;

procedure ojosv (var v:t_vector; var c_ojos:integer);
var
    i:integer;
begin
    c_ojos:=0;
    for i:=1 to n do
    begin
        if (v[i].ojos ='violeta') and (v[i].edad <= 30) then
            inc (c_ojos);
    end;
end;

//Cuerpo principal

begin
    inicializar_vec (v);
    cargar_vec (v);
    sesenta (v,c_60);
    writeln ('cantidad de personas mayores de 60 años: ',c_60);
    mujeres (v,c_muj);
    writeln ('cantidad de mujeres mayores de 1,70 cm: ',c_muj);
    kilos (v,c_kilos);
    writeln ('porcentaje de personas con menos de 50 kg: ', (c_kilos*100)/n);
    cubanos (v,c_cub);
    writeln ('porcentaje de hombres de origen Cubano: ', (c_cub*100)/n);
    argentinas (v,c_arg);
    writeln ('porcentaje de mujeres de origen Argentino: ', (c_arg*100)/n);
    ojosv (v,c_ojos);
    writeln ('porcentaje de personas con menos de 30 años y ojos violetas: ', (c_ojos*100)/n);
    readkey;  
end.