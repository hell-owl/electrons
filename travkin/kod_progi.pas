uses
  graphABC;//Подключаем графический модуль 


function F(x1: real): real;
begin
  F := sqrt((100 / (2 * sin(3 * x1 * pi / 360))) * (100 / (2 * sin(3 * x1 * pi / 360)))); //Функция 
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
  //Координаты правой нижней границы системы координат: 
  xRight := window.Width - 50; 
  yRight := window.Height - 50; 
  writeln('крайняя точка по Ох');
  readln(b);
  writeln(b);
  writeln('крайняя точка по Ох (-)');
  readln(a);
  writeln(a);
  writeln('шаг по Ох');
  readln(dx);
  writeln(dx);
  //a := 0;b := 360 ;dx := 30; 
  writeln('крайняя точка по Оу');
  readln(fmax);
  writeln(fmax);
  writeln('крайняя точка по Оу (-)');
  readln(fmin);
  writeln(fmin);
  writeln('шаг по Оу');
  readln(dy);
  writeln(dy);
  //fmin := -20;fmax := 600;dy := 70; 
  //Устанавливаем масштаб: 
  mx := (xRight - xLeft) / (b - a); //масштаб по Х 
  my := (yRight - yLeft) / (fmax - fmin); //масштаб по Y 
  //начало координат: 
  x0 := trunc(abs(a) * mx) + xLeft; 
  y0 := yRight - trunc(abs(fmin) * my); 
  //Рисуем оси координат: 
  setpenwidth(4); 
  line(xLeft, y0, xRight + 10, y0); //ось ОХ 
  line(x0, yLeft - 10, x0, yRight); //ось ОY 
  SetFontSize(20); //Размер шрифта 
  SetFontColor(clBlue); //Цвет шрифта 
  TextOut(xRight + 20, y0 - 15, 'X'); //Подписываем ось OX 
  TextOut(x0 - 10, yLeft - 30, 'Y'); //Подписываем ось OY 
  SetFontSize(12); //Размер шрифта 
  SetFontColor(clRed); //Цвет шрифта 
  { Засечки по оси OX: } 
  n := round((b - a) / dx) + 1; //количество засечек по ОХ 
  for i := 1 to n do 
  begin
    num := a + (i - 1) * dx; //Координата на оси ОХ 
    x := xLeft + trunc(mx * (num - a)); //Координата num в окне 
    Line(x, y0 - 3, x, y0 + 3); //рисуем засечки на оси OX 
    str(Num:0:1, s); 
    if abs(num) > 1E-15 then //Исключаем 0 на оси OX 
      TextOut(x - TextWidth(s) div 2, y0 + 10, s)
  end; 
  { Засечки на оси OY: } 
  n := round((fmax - fmin) / dy) + 1; //количество засечек по ОY 
  for i := 1 to n do 
  begin
    num := fMin + (i - 1) * dy; //Координата на оси ОY 
    y := yRight - trunc(my * (num - fmin)); 
    Line(x0 - 3, y, x0 + 3, y); //рисуем засечки на оси Oy 
    str(num:0:0, s); 
    if abs(num) > 1E-15 then //Исключаем 0 на оси OY 
      TextOut(x0 + 7, y - TextHeight(s) div 2, s)
  end; 
  TextOut(x0 - 10, y0 + 10, '0'); //Нулевая точка 
  { График функции строим по точкам: } 
  x1 := a; //Начальное значение аргумента 
  while x1 <= b do 
  begin
    begin
      SetPenwidth(3); 
      setpencolor(clgreen); 
      y1 := F(x1); //Вычисляем значение функции 
      try 
        x := x0 + round(x1 * mx); //Координата Х в графическом окне 
        y := y0 - round(y1 * my);//Координата Y в графическом окне 
      except 
        y := window.Height; 
      end; 
      //Если y попадает в границы [yLeft; yRight], то ставим точку: 
      if (y >= yLeft) and (y <= yRight) and (y >= 0) then begin SetPixel(x, y, clGreen);circle(x, y, 2); end; 
      x1 := x1 + 0.001; //Увеличиваем абсциссу 
    end; 
  end; 
end.