unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  ecount, i: integer;
  goodnumber: boolean;

implementation

{$R *.dfm}

const eradius = 5;
const radius = 50;

procedure TForm1.Button1Click(Sender: TObject);
begin
  repeat
    try
      ecount := strtoint(InputBox('Electrons', 'How many electrons', '3'));
      goodnumber := True;
    except
      goodnumber := False;
    end;
  until goodnumber;
  i := 0;
  while i < ecount do
  begin
    //print('Electron', i + 1, 'angle:', 360 / ecount * i);
    Form1.Canvas.Ellipse(100 + trunc(radius * (cos(2 * Pi / ecount * i))) - eradius, 100 - trunc(radius * (sin(2 * Pi / ecount * i))) - eradius, 100 + trunc(radius * (cos(2 * Pi / ecount * i))) + eradius, 100 - trunc(radius * (sin(2 * Pi / ecount * i))) + eradius);
    i := i + 1;          
  end;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  Form1.Canvas.Brush.Color := clBlue;
  Form1.Canvas.Pen.Color := clBlue;
end;

end.
 