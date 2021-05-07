Program Fecha;
Var dia,mes,anio: Integer;

begin
	writeln('ingrese el dia');
	readln(dia);
	writeln('ingrese el mes');
	readln(mes);
	writeln('ingrese año');
	readln(anio);

	if mes=02 then
	begin
	 if (anio mod 4)=0 then
		begin
		   if dia=29 then
			begin
				dia:=1;
				mes:=mes+1;
			end
            	else
             	 begin
                 dia:=dia+1
             	 end
		end
	    else
	    begin
		 if dia=28 then
			begin
	         dia:=1;
	         mes:=mes+1;
	         end
	        else
	         dia:=dia+1
	         end;
	     writeln (dia,'/',mes,'/',anio)
	    end
     else
	 
	  if (mes=04) or (mes=06) or (mes=09) or (mes=011) then
	  begin
	  	 if dia=30 then
	  		begin
	  	      dia:=1;
	  	      mes:=mes+1;
	        end
	        else
	        begin 
	         dia:=dia+1
	        end;
	     writeln(dia,'/', mes,'/', anio);
	   end
	    else
         begin
	    	 if dia=31 then
	    	 				begin
	    	 	             dia:=1;
             
	    	 	    			begin
                     			if mes=12 then
                     	 		 begin 
                 	 	 			mes:=1;
                 	 	 			anio:=anio+1;
                    			end
                 				else
                     			begin
                    	 			mes:=mes+1
                        		end
                    		end       
                   
                  
              				else
               				begin
                			 dia:=dia+1
               			 	end
            end

                   
	     writeln(dia,mes,año)
	    
	    end	


end.