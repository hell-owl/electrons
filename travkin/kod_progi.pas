uses
  graphABC;//���������� ����������� ������ 


function F(x1: real): real;
begin
  F := sqrt((100 / (2 * sin(3 * x1 * pi / 360))) * (100 / (2 * sin(3 * x1 * pi / 360)))); //������� 
end;

var
  x0, y0, x, y, xLeft, yLeft, xRight, yRight, n: integer; 
  a, b, fmin, fmax, x1, y1, mx, my, dx, dy, num: real; 
  i: byte; 
  s: string;

begin
  window.Maximize; 
  xLeft := 50; 
  yLeft := 50; 
  //���������� ������ ������ ������� ������� ���������: 
  xRight := window.Width - 50; 
  yRight := window.Height - 50; 
  writeln('������� ����� �� ��');
  readln(b);
  writeln(b);
  writeln('������� ����� �� �� (-)');
  readln(a);
  writeln(a);
  writeln('��� �� ��');
  readln(dx);
  writeln(dx);
  //a := 0;b := 360 ;dx := 30; 
  writeln('������� ����� �� ��');
  readln(fmax);
  writeln(fmax);
  writeln('������� ����� �� �� (-)');
  readln(fmin);
  writeln(fmin);
  writeln('��� �� ��');
  readln(dy);
  writeln(dy);
  //fmin := -20;fmax := 600;dy := 70; 
  //������������� �������: 
  mx := (xRight - xLeft) / (b - a); //������� �� � 
  my := (yRight - yLeft) / (fmax - fmin); //������� �� Y 
  //������ ���������: 
  x0 := trunc(abs(a) * mx) + xLeft; 
  y0 := yRight - trunc(abs(fmin) * my); 
  //������ ��� ���������: 
  setpenwidth(4); 
  line(xLeft, y0, xRight + 10, y0); //��� �� 
  line(x0, yLeft - 10, x0, yRight); //��� �Y 
  SetFontSize(20); //������ ������ 
  SetFontColor(clBlue); //���� ������ 
  TextOut(xRight + 20, y0 - 15, 'X'); //����������� ��� OX 
  TextOut(x0 - 10, yLeft - 30, 'Y'); //����������� ��� OY 
  SetFontSize(12); //������ ������ 
  SetFontColor(clRed); //���� ������ 
  { ������� �� ��� OX: } 
  n := round((b - a) / dx) + 1; //���������� ������� �� �� 
  for i := 1 to n do 
  begin
    num := a + (i - 1) * dx; //���������� �� ��� �� 
    x := xLeft + trunc(mx * (num - a)); //���������� num � ���� 
    Line(x, y0 - 3, x, y0 + 3); //������ ������� �� ��� OX 
    str(Num:0:1, s); 
    if abs(num) > 1E-15 then //��������� 0 �� ��� OX 
      TextOut(x - TextWidth(s) div 2, y0 + 10, s)
  end; 
  { ������� �� ��� OY: } 
  n := round((fmax - fmin) / dy) + 1; //���������� ������� �� �Y 
  for i := 1 to n do 
  begin
    num := fMin + (i - 1) * dy; //���������� �� ��� �Y 
    y := yRight - trunc(my * (num - fmin)); 
    Line(x0 - 3, y, x0 + 3, y); //������ ������� �� ��� Oy 
    str(num:0:0, s); 
    if abs(num) > 1E-15 then //��������� 0 �� ��� OY 
      TextOut(x0 + 7, y - TextHeight(s) div 2, s)
  end; 
  TextOut(x0 - 10, y0 + 10, '0'); //������� ����� 
  { ������ ������� ������ �� ������: } 
  x1 := a; //��������� �������� ��������� 
  while x1 <= b do 
  begin
    begin
      SetPenwidth(3); 
      setpencolor(clgreen); 
      y1 := F(x1); //��������� �������� ������� 
      try 
        x := x0 + round(x1 * mx); //���������� � � ����������� ���� 
        y := y0 - round(y1 * my);//���������� Y � ����������� ���� 
      except 
        y := window.Height; 
      end; 
      //���� y �������� � ������� [yLeft; yRight], �� ������ �����: 
      if (y >= yLeft) and (y <= yRight) and (y >= 0) then begin SetPixel(x, y, clGreen);circle(x, y, 2); end; 
      x1 := x1 + 0.001; //����������� �������� 
    end; 
  end; 
end.