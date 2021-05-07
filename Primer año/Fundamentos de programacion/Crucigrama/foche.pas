program crucigramas_m;
uses
    crt,kadenas;
const
     u=12;
     v=50;
type
    t_matriz= array[1..u,1..v] of char;
var
   matriz:t_matriz;
   posi,ingresar,errores,completas,rec_final:word;
   perdio,completo_todo,validar_l,validar_p:boolean;
   letra_usuario,jugar:char;
   vector_palabras,vector_pistas,vector_usuario,letras_usadas:t_vector_s;
   espacios_izq,espacios_der,ya_completada:t_vector;
   intento_palabra,palabra_final:string;

   procedure shift(var cadena: string); //No permite que se sobreescriban las letras usadas al mostrarlas
   begin
        cadena := copy(cadena, 3, length(cadena)-2);
   end;

   procedure crear_matriz(var vector_usuario:t_vector_s; VAR matriz:t_matriz; espacios_izq,espacios_der:t_vector);
   var
   i,j,k,L,aux:word;
   begin
        for i:=1 to 12 do
        begin
             aux:=length(vector_usuario[i]);
             for j:= 1 to espacios_izq[i] do
             begin
                  matriz[i,j]:=' ';
             end;

             for k:=1 to length(vector_usuario[i]) do
             begin
                  matriz[i,espacios_izq[i]+k]:=vector_usuario[i][k];
             end;

             for L:= 1 to espacios_der[i] do
             begin
                  matriz[i,espacios_izq[i]+aux+L]:= ' ';
             end;
        end;
   end;

   procedure mostrar_matriz(var matriz:t_matriz;posi:word; completas:word; letras_usadas:t_vector_s);
   var
      rec,rec2:word;
   begin
        clrscr;
        textcolor(red);
        writeln('-------------------------------------------------------------------');
        write('-----------------------------');
        textcolor(lightred);
        write('CRUCIGRAMA');
        textcolor(red);
        writeln('----------------------------');
        writeln('-------------------------------------------------------------------');
        for rec:=1 to u do
        begin
             gotoxy(55,8);
             textcolor(12);
             writeln('Errores: ',errores,' de: ',3+completas);
             gotoxy(1,27);
             textcolor(black);
             textbackground(yellow);
             writeln('Ultimas letras usadas(20):',letras_usadas[posi]);
             gotoxy(1,17);
             textcolor(black);
             textbackground(yellow);
             write('Pistas:');
             normvideo;
             writeln(' ',vector_pistas[posi]);
             gotoxy(1,19);
             textcolor(11);
             writeln('Ingrese 1 para probar una letra o 2 para arriesgar con una palabra:');
             for rec2:= 1 to v do
             begin
                  if rec = posi then
                  begin
                       textcolor(1);
                       gotoxy(rec2,3+rec);
                       write(matriz[rec,rec2]);

                  end
                  else
                  begin
                       textcolor(10);
                       gotoxy(rec2,3+rec);
                       write(matriz[rec,rec2]);
                  end;
             end;
        end;
        gotoxy(68,19);
   end;

   procedure tecla_usuario(var perdio:boolean; ya_completada:t_vector; var letras_usadas:t_vector_s; var intento_palabra:string; var letra_usuario:char; var ingresar,posi:word; var validar_l,validar_p:boolean);
   var                                                   //control dentro de la interfaz
      num_tecla:integer;
      tecla:char;

   begin
        validar_l:=False;
        validar_p:=False;
        tecla:=readkey;
        num_tecla:=ord(tecla);
        case num_tecla of
             80: begin
                      if posi <12 then
                         inc(posi);
                 end;
             72: begin
                      if posi>1 then
                         posi:=posi-1;
                 end;
             13: ingresar:=posi;
             49:begin
                     if ya_completada[posi] = 0 then
                     begin
                          gotoxy(1,21);
                          textcolor(11);
                          write('Ingrese la letra: ');
                          textcolor(white);
                          readln(letra_usuario);
                          if(length(letras_usadas[posi]) > 40) then
                          begin
                          shift(letras_usadas[posi]);
                          end;
                          letras_usadas[posi]:=letras_usadas[posi]+' '+letra_usuario;
                          validar_l:=True;
                      end;
                end;
             50:begin
                    if ya_completada[posi] = 0 then
                    begin
                         gotoxy(1,21);
                         textcolor(11);
                         write('Ingrese la palabra: ');
                         textcolor(white);
                         readln(intento_palabra);
                         validar_p:=True;
                     end;
               end;
             27: perdio:=True;
        end;
   end;
   procedure validacion_letra_usuario(var ya_completada:t_vector; letra_usuario:char; vector_palabras:t_vector_s;  var vector_usuario:t_vector_s; posi:word; var errores:word);
   var                                               //comprobar si la letra ingresada es correcta
      i,completa3:word;
      le_pego:boolean;
   begin
        completa3:=0;
        le_pego:= False;
        for i:=1 to length(vector_palabras[posi]) do
        begin
             if vector_palabras[posi][i] = letra_usuario then
             begin
                  le_pego:=True;
                  vector_usuario[posi][i*2-1]:= letra_usuario;
             end;
             if vector_palabras[posi][i] = vector_usuario[posi][i*2-1] then
                inc(completa3);
        end;
        if le_pego=False then
           inc(errores);
        if completa3 = length(vector_palabras[posi]) then
           ya_completada[posi]:=1;
   end;
   procedure validar_palabra_usuario(var ya_completada:t_vector; posi:word; intento_palabra:string;vector_palabras:t_vector_s; var vector_usuario:t_vector_s; var completas:word);
   var                                                         //comprobar si la palabra ingresada es correcta
      reco:integer;
   begin
        if vector_palabras[posi] <> intento_palabra then
        begin
           perdio:=True;
        end
        else
        begin
             inc(completas);
             ya_completada[posi]:=1;
             for reco:=1 to length(intento_palabra) do
             begin
                  vector_usuario[posi][reco*2-1]:= intento_palabra[reco];
             end;
        end;
   end;
   procedure letras_completas(posi:word;vector_palabras,vector_usuario:t_vector_s;var completas:word);
   var                                                     //comprueba si faltan encontrar letras
      reco:word;
      faltan:boolean;
   begin
        faltan:=False;
        for reco:=1 to length(vector_palabras[posi]) do
        begin
             if vector_palabras[posi][reco]<>vector_usuario[posi][reco*2-1] then
                faltan:= True;
        end;
        if not faltan then
           inc(completas);
   end;

begin
     inicializar_s(letras_usadas);                     //cuerpo principal
     inicializar(ya_completada);
     palabra_final:='PROGRAMACION';
     completas:=0;
     errores:=0;
     posi:=1;
     completo_todo:=False;
     perdio:=False;
     espacios_izq[1]:=14;                                                                         //inicializa vectores
     espacios_izq[2]:=12;
     espacios_izq[3]:=12;
     espacios_izq[4]:=14;
     espacios_izq[5]:=14;
     espacios_izq[6]:=8;
     espacios_izq[7]:=12;
     espacios_izq[8]:=2;
     espacios_izq[9]:=20;
     espacios_izq[10]:=2;
     espacios_izq[11]:=18;
     espacios_izq[12]:=10;
     espacios_der[1]:=20;
     espacios_der[2]:=24;
     espacios_der[3]:=26;
     espacios_der[4]:=18;
     espacios_der[5]:=22;
     espacios_der[6]:=26;
     espacios_der[7]:=20;
     espacios_der[8]:=26;
     espacios_der[9]:=22;
     espacios_der[10]:=26;
     espacios_der[11]:=16;
     espacios_der[12]:=28;
     vector_palabras[1]:='compilar';
     vector_palabras[2]:='memoria';
     vector_palabras[3]:='vector';
     vector_palabras[4]:='algoritmo';
     vector_palabras[5]:='burbuja';
     vector_palabras[6]:='interfaz';
     vector_palabras[7]:='parametro';
     vector_palabras[8]:='subprograma';
     vector_palabras[9]:='char';
     vector_palabras[10]:='inalambrica';
     vector_palabras[11]:='conexion';
     vector_palabras[12]:='python';
     vector_pistas[1]:='traducir lenguaje de alto nivel a lenguaje de maquina';
     vector_pistas[2]:='dispositivo que almacena datos informaticos';
     vector_pistas[3]:='lugar donde se almacenan datos del mismo tipo';
     vector_pistas[4]:='conjunto ordenado de operaciones que permite hallar la solucion a un tipo de problema';
     vector_pistas[5]:='es un secillo algortimo de ordenamiento';
     vector_pistas[6]:='medio por el que un usuario interactua con un programa';
     vector_pistas[7]:='variable utilizada para ingresar valores de entrada/salida en un procedimiento';
     vector_pistas[8]:='(procedimiento/funcion)=...';
     vector_pistas[9]:='tipo de dato';
     vector_pistas[10]:='una conexion sin cable';
     vector_pistas[11]:='enlace entre dos elementos';
     vector_pistas[12]:='lenguaje de programacion';
     guiones_vectores(vector_palabras,vector_usuario);
     repeat
     gotoxy(20,6);                                   //primera interfaz
     textcolor(11);
     textbackground(1);
     writeln('=================================================================================');
     gotoxy(20,7);
     writeln('=================================================================================');
     gotoxy(20,8);
     writeln('========    Quiere hacer un crucigrama? S para jugar o ESC para salir    ========');
     gotoxy(20,9);
     writeln('=================================================================================');
     gotoxy(20,10);
     writeln('=================================================================================');
     jugar:= readkey;
     jugar:=upcase(jugar);
     normvideo;
     if jugar='S'then                                 //dentro del juego
     begin
          completo_todo:=False;
     repeat
           crear_matriz(vector_usuario,matriz,espacios_izq,espacios_der);
           mostrar_matriz(matriz,posi,completas,letras_usadas);
           //color_letras(vector_usuario,posi,completas,letras_usadas);
           tecla_usuario(perdio,ya_completada,letras_usadas,intento_palabra,letra_usuario,ingresar,posi,validar_l,validar_p);
           if validar_l then
           begin
              validacion_letra_usuario(ya_completada,letra_usuario,vector_palabras,vector_usuario,posi,errores);
              letras_completas(posi,vector_palabras,vector_usuario,completas);
           end
           else if validar_p then
           begin
                   validar_palabra_usuario(ya_completada,posi, intento_palabra, vector_palabras, vector_usuario, completas);
               end;
           if errores > 3+completas then
              perdio:=True;
           if completas = 12 then
              completo_todo:= True;
     until (perdio=True) or (completo_todo=True);
     if perdio then
     begin
          clrscr;
          gotoxy(50,8);
          textcolor(1);
          writeln('PERDISTE :C');
     end
     else
     if completo_todo then                 //final con todo completado
     begin
          clrscr;
          for rec_final:=1 to 12 do
          begin
               gotoxy(30+espacios_izq[rec_final],5+rec_final);
               writeln(vector_usuario[rec_final]);
          end;
          for rec_final:=1 to 12 do
          begin
               delay(500); 
               gotoxy(48,5+rec_final);
               textcolor(red);
               writeln(palabra_final[rec_final]);
          end;
          gotoxy(44,20);
          textcolor(10);
          writeln('GANASTE!!!');
     end;


     end
     else if jugar=#27 then                      //si no quieren jugar
          begin
               clrscr;
               perdio:=True;
               gotoxy(50,8);
               textcolor(1);
               writeln('Adios :C');
          end
          else
          begin
              gotoxy(50,12);                       //tecla erronea en primera interfaz
              textcolor(red);
              writeln('Respuesta invalida');
              delay(500);
              clrscr;
          end;
     until (completo_todo=True) or (perdio=True);
     readkey;
end.