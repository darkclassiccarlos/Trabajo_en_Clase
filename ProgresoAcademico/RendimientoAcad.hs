--Suma de notas de una lista
sumnotas :: [Float] -> Float
sumnotas [] = 0 
sumnotas (x:xs) = x + sumnotas xs

--dividir el total de la suma de notas en el valor total de cursos
division::Float -> Float -> Float
division a 0 = a
division a b = a/b

--calcular tamaño del vector
length' :: [Float] -> Float
length' xs = sum [1 | _ <- xs]

--Promedio de las notas
promedio :: [Float] -> Float
promedio [] =  0
promedio x = division (sumnotas x)  (length' x)

--Calcular promedio rendimiento
rendimiento :: [Float] -> String 
rendimiento [] = "no hay valores"
rendimiento v = if promedio v <= 3 then "malo" 
                else if promedio v <=4 then "bueno"
                else "Muy bueno"                

--Multiplicacion
mult ::Float -> Float -> Float
mult a b = a * b

--Indice de rendimiento IRA
-- a notas b creditos
ira :: [Float] -> [Float] -> Float
ira [] [] = 0
ira a b = division (mult (sumnotas a ) (sumnotas b)) (sumnotas b )

