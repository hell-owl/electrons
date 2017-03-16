unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls;

type
  TForm1 = class(TForm)
    Timer1: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure FormMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  xmin, xmax: integer;

implementation

function sign(n: real): integer; forward;

type TElectron = class
  x: integer;
  impuls: real;
  constructor Create(x: integer = 0);
  procedure force(second: TElectron);
  procedure move();
  procedure Draw();
end;

type TWire = class
  Top, Left, Width, Height: integer;
  constructor Create(Top, Left, Width, Height: integer);
  procedure Draw();
  end;

var
  electrons: array of TElectron;
  wire: TWire;

{$R *.dfm}

{ TElectron }

constructor TElectron.Create(x: integer);
begin
  self.x := x;
  self.impuls := 0;
end;

procedure TElectron.Draw;
begin
  Form1.Canvas.Brush.Color := clBlue;
  Form1.Canvas.Ellipse(wire.Left + wire.Width div 2 + self.x - 3, wire.Top + 4 - 3, wire.Left + wire.Width div 2 + self.x + 3, wire.Top + 4 + 3);
end;

procedure TElectron.force(second: TElectron);
begin
  if self.x < second.x then
    self.impuls := self.impuls - 1 / ((self.x - second.x) * (self.x - second.x))
  else
    self.impuls := self.impuls + 1 / ((self.x - second.x) * (self.x - second.x));
end;

procedure TElectron.move;
begin
  if (self.x + sign(self.impuls) > xmin) and (self.x + sign(self.impuls) < xmax) then
    self.x := self.x + sign(self.impuls)
  else if self.impuls > 0 then
    self.x := xmax
  else
    self.x := xmin;
  self.impuls := 0;
end;

function sign(n: real): integer;
begin
  if n > 0 then
    result :=  1
  else if n = 0 then
    result := 0
  else
    result := -1;
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  wireLength, err: integer;
begin
  repeat
    err := 0;
    try
      wireLength := strtoint(InputBox('wire length', 'Enter wire length', '200'));
      if wireLength < 10 then
        raise Exception.Create('');
    except
      err := 1;
    end;
  until err = 0;
  wire := TWire.Create(100, 100, wireLength, 8);
  xmin := - wire.Width div 2;
  xmax := wire.Width div 2;
  setlength(electrons, 0);
  Timer1.Enabled := True;
end;

{ TWire }

constructor TWire.Create(Top, Left, Width, Height: integer);
begin
  self.Top := Top;
  self.Left := Left;
  self.Width := Width;
  self.Height := Height;
end;

procedure TWire.Draw;
begin
  Form1.Canvas.Brush.Color := clSilver;
  Form1.Canvas.Rectangle(Left, Top, Left + Width, Top + Height);
end;

procedure TForm1.Timer1Timer(Sender: TObject);
var
  j, k: integer;
begin
  //clean screen
  wire.Draw();
  for j := 0 to length(electrons) - 1 do
  begin
    for k := 0 to length(electrons) - 1 do
    begin
      if k <> j then
        electrons[j].force(electrons[k]);
    end;
  end;
  for j := 0 to length(electrons) - 1 do
  begin
    electrons[j].move();
    electrons[j].Draw();
  end;
end;

procedure TForm1.FormMouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
var
  i: integer;
begin
  if (x > wire.Left) and (y > wire.Top) and (x < wire.Left + wire.Width) and (y < wire.Top + wire.Height) then
  begin
    for i := 0 to length(electrons) - 1 do
    begin
      if abs(x - wire.Width div 2 - wire.Left - electrons[i].x) < 6 then
      begin
        Application.MessageBox('Too near to another electron', 'Error');
        exit;
      end;
    end;
    setlength(electrons, length(electrons) + 1);
    electrons[length(electrons) - 1] := TElectron.Create(x - wire.Width div 2 - wire.Left);
  end;
end;

end.
 