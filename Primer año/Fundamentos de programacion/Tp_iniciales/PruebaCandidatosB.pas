program elecciones2;

uses crt;

var

   I,cvoto,totc1,totc2,totc3,totbl:Integer;

   voto,c1,c2,c3,cbl:Integer;

   porcentaje: real;

BEGIN

   c1:=0;

   c2:=0;

   c3:=0;

   cbl:=0;

   totc1:=0;

   totc2:=0;

   totc3:=0;

   totbl:=0;

    for I:= 1 to 3 do

    begin

      Write('candidato numero: ');

      Read(voto);
          
          while (voto>0) do
          
          begin
   
            case voto of
            
            1: 
            begin
              
            
            c1:=c1+1;

            totc1:=totc1+1;
            
            end;

            2:begin
            
            c2:=c2+1;

            totc2:=totc2+1

            end;
            
            3: begin
            
            c3:=c3+1;
            
            totc3:=totc3+1

            end;

            else
            
            cbl:= cbl+1;
            
            totbl:=totbl+1;

            end;
           
           Write('candidato numero: ');
            
            Read(voto);
            
            end;
            
            WriteLn('----');
            
            WriteLn('depto: ',I);
              
      if (c1>c2) and (c1>c3) then
               
      WriteLn('#ganador: candidato 1')
                  
      else
                    
      if (c2>c3) then
                    
       WriteLn('#ganador: candidato 2')
                   
        else
                    
          WriteLn('#ganador: candidato 3');
                     
         WriteLn('----');

      cvoto:=cvoto+1;
                    
        end;

WriteLn('provincia: ');

 if (totc1>totc2) and (totc1>totc3) then
               
      WriteLn('#ganador: candidalto 1')
                  
      else
                    
      if (totc2>totc3) then
                    
       WriteLn('#ganador: candidato 2')
                   
        else
                    
          WriteLn('#ganador: candidato 3');
                     
         WriteLn('----');

porcentaje:= (totbl*100)/cvoto;

write('el porcentaje de voto en blanco es: ', porcentaje:4:2 )

END.
