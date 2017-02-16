type
  TElectron = class
    x: real;
    force: real;
    function distance(e2: TElectron): real;
    begin
      result := abs(self.x - e2.x);
    end;
    function calculateForce(e2: TElectron): real;
    begin
      result := 1 / sqr(distance(e2));
    end;
  end;

var
  electrons: array of TElectron;
  i: integer;

begin
  electrons := new TElectron[2](new TElectron(), new TElectron());
  for i := 0 to length(electrons) do
  begin
    
  end;
end.