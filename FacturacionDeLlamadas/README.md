## Proyecto
A Bob le ha llegado la factura de su teléfono celular y, previo a abonarla, le surgen ciertas dudas respecto a si le han facturado correspondiente las llamadas que ha realizado durante ese mes. En consecuencia, Bob se comunica con la empresa de telecomunicaciones solicitándole el criterio (junto con las determinadas reglas) con el cual la empresa factura cada una de las llamadas. No obstante, Bob ha realizado muchísimas llamadas y le es demasiado impráctico realizar el cálculo manual, además que Bob no es muy ágil con las operaciones aritméticas.

Crear un proyecto que ayude a Bob a calcular la correcta facturación de las llamadas realizadas.

Las reglas de facturación que la empresa aplica a cada una de las llamadas, son las siguientes:

1. Si la llamada tiene una duración menor a 5 minutos, se cobrará 3 centavos por cada segundo.  Por ejemplo: Una llamada de 3 minutos y 30 segundos, realizando la transformación a segundos, equivaldría a 210 segundos. Por ende, la llamada se cobrará 630 centavos ( Ya que 210 segundos multiplicado por 3 centavos --> 210 * 3 = 630 )

2. Si la llamada tiene una duración mayor o igual a 5 minutos, se cobrará 150 centavos por cada minuto. Si la llamada posee segundos, se redondeará al minuto inmediato superior.
	- Ejemplo 1: Una llamada de 6 minutos se cobrará 900 centavos ( Ya que 6 minutos multiplicado por 150 centavos --> 6 * 150 = 900 )
	- Ejemplo 2: Una llamada de 6 minutos y 30 segundos, se redondearía hacia un minuto arriba. Por ende, se transformaría en una llamada de 7 minutos y se cobraría 1050 centavos ( Ya que 7 minutos multiplicado por 150 centavos --> 7 * 150 = 1050 )

3. Las llamadas que pertenezcan al número de teléfono que mayor duración acumulada en segundos posea, son GRATIS, es decir, no serán facturadas. 
Por ejemplo: A Federico se le realizó 3 llamadas con una duración de 30, 40 y 50 segundos respectivamente. A Sabrina se le realizó 3 llamadas con una duración de 10, 20 y 30 segundos respectivamente. A Pedro se le realizó 3 llamadas con una duración de 10, 10 y 20 segundos respectivamente. Federico tiene una duración acumulada en segundos total de: 30 + 40 + 50 = 120 segundos. Sabrina tiene una duración acumulada en segundos total de: 10 + 20 + 30 = 60 segundos. Pedro tiene una duración acumulada en segundos total de: 10 + 10 + 20 = 40 segundos. Por ende, las llamadas realizadas a Federico NO se facturarán, serán GRATIS.
