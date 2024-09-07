# ArgentumClicker
Un script diseñado para testear la seguridad de varios servidores de Argentum Online, actualmente en Septiembre de 2024 continua siendo funcional y puede simular clicks con la tecla que configures.

Este script en Python está diseñado para automatizar la interacción con la interfaz gráfica de un sistema operativo Windows mediante el uso de teclas del teclado. Su funcionamiento se puede dividir en las siguientes partes clave:

Verificación de Privilegios de Administrador: Antes de realizar cualquier acción, el script comprueba si se está ejecutando con privilegios de administrador. Esto se hace para asegurar que el script tenga los permisos necesarios para realizar operaciones que podrían requerir elevados derechos de acceso. Si el script no tiene estos privilegios, intenta relanzarse con permisos de administrador.

Automatización de Clics: El script incluye una función que simula la acción de hacer doble clic en la pantalla. Esta función realiza dos doble clics seguidos con un breve intervalo entre ellos. Esta automatización es útil para realizar tareas repetitivas que requieren interacción con la interfaz gráfica.

Manejo de Eventos de Teclado: El script está configurado para escuchar eventos de teclado en tiempo real. Cuando detecta que la tecla 'U' es presionada, ejecuta la función de doble clic. Esta funcionalidad permite que el script responda a las entradas del usuario de manera dinámica.

Control de Ejecución: El script permanece en ejecución y espera hasta que se presione la tecla 'Esc', momento en el cual finaliza su ejecución. Durante su funcionamiento, maneja posibles errores que pueden surgir tanto de la interacción del teclado como de la automatización de clics.

En resumen, el script automatiza la simulación de clics en la pantalla basándose en la entrada del teclado, y gestiona la ejecución con privilegios adecuados para garantizar que pueda llevar a cabo sus tareas sin problemas de permisos.




# Kevin Korduner
Un script creado para evaluar la seguridad de múltiples servidores de Argentum Online sigue siendo funcional en septiembre de 2024. Este script puede simular clics utilizando la tecla que configures.
