program ej5;
uses crt;
const
     n=10;
type
    t_dato= real;
    t_vector= array [1..n] of t_dato;
var
   vec: t_vector;
   posi,neg,cer: Boolean;



procedure inicializar (var vec:t_vector);
   var
      I:1..n;
   begin
      for I:=1 to n do
      begin
         vec[I]:=0;
      end;
   end;

procedure cargar (var vec:t_vector);
   var
      I:1..n;
      aux:t_dato;
   begin
      for I:=1 to n do
      begin
         write('ingresar numero: ');
         read (aux);
         vec[I]:=aux;
      end;
   end;

procedure positivo (vec:t_vector; var posi:Boolean);
   var
      I:1..n;
   begin
      posi:=false;
      for I:=1 to n do
      begin
         if (vec[I] > 0) then
            posi:=true;
      end;
   end;

procedure negativo (vec:t_vector; var neg:Boolean);
   var
      I:1..n;
   begin
      neg:=false;
      for I:=1 to n do
      begin
         if (vec[I] < 0) then
            neg:=true;
      end;
   end;

procedure cero (vec:t_vector; var cer:Boolean);
   var
      I:1..n;
   begin
      cer:=false;
      for I:=1 to n do
      begin
         if (vec[I] = 0) then
            cer:=true;
      end;
   end;


BEGIN
   writeln('ingrese el vector');
   //inicializar (vec);
   
   //cargar (vec);
   //positivo (vec,posi);
   //if (posi = true) then
     // write('el vector tiene componentes positivas');
   //negativo (vec,neg);
   //if (neg = true) then
     // write('el vector contiene componentes negativas');
   //cero (vec,cer);
   //if (cer = true) then
     // write('el vector tiene algun cero');
END.