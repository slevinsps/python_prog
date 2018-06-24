
var A:array[1..100] of integer;
    max:integer;//размер массива
procedure ShakerSort;
    var
      l, r, j : Integer;
      x : integer;
    begin
      l := 2; //левый край =2
      r := max; //правый край=конец
      while l <= r do //пока на сомкнулись
        begin
          { "Пузырек" слева направо }//идем сначала до конца
          for j := l to r do
          if A[j] < A[j - 1] then //если следующий меньше
            begin
              x := A[j];
              A[j] := A[j - 1]; //обмениваем
              A[j - 1] := x;
            end;
          r := r - 1; //сдвигаем правй край влево
          { "Пузырек" справа налево }//идем с конца к началу
          for j := r downto l do
          if A[j] < A[j - 1] then //впереди меньше
            begin
              x := A[j];
              A[j] := A[j - 1]; //обмениваем
              A[j - 1] := x;
            end;
          l := l + 1; //левый край сдвигаем вправо
        end;
    end;
var i:byte;
begin
randomize;
write('Размер массива до 100 max=');
read(max);
writeln('Исходный массив:');
for i:=1 to max do
 begin
  A[i]:=random(100);
  write(A[i]:4);
 end;
writeln;
ShakerSort;
writeln('Сортировка:');
for i:=1 to max do
write(A[i]:4);
end.