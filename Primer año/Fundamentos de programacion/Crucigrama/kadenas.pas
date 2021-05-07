unit kadenas;
interface
         const
              n=12;
         type
             t_vector_s=array[1..n] of string;
             t_vector=array[1..n] of integer;

         procedure guiones_vectores(vector_base:t_vector_s; var vector_usuario:t_vector_s);
         procedure inicializar_s (var s_vector:t_vector_s);
         procedure inicializar(var v:t_vector);

implementation
              procedure guiones_vectores(vector_base:t_vector_s; var vector_usuario:t_vector_s);
              var
                 i,i2,aux:word;
              begin
                   for i := 1 to n do
                   begin
                        aux:=length(vector_base[i]);
                        for i2:=1 to aux do
                        begin
                             vector_usuario[i]:=vector_usuario[i]+'_ ';
                        end;
                   end;
              end;
              procedure inicializar_s (var s_vector:t_vector_s);
              var i:integer;
              begin
                   for i:= 1 to N do
                   begin
                        s_vector[i]:='';
                   end;
              end;
              procedure inicializar(var v:t_vector);
              var
                 rec:integer;
              begin
                   for rec:= 1 to N do
                   begin
                        v[rec]:=0;
                   end;
              end;
begin
end.

