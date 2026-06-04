kickoff asistente de soporte - martes

estuvimos con gabi y diego viendo lo del asistente para el cliente de retail. la idea es un bot que conteste tickets de soporte nivel 1 usando la base de docs interna que tienen (como 4000 articulos en confluence, un desastre, mitad desactualizados)

gabi dice que arranquemos con RAG simple, embeddings + busqueda vectorial sobre los articulos, nada de fine tuning por ahora. diego tiene dudas con la calidad de los docs, dice que si indexamos basura el bot va a contestar basura. quedamos en hacer un piloto con una sola categoria de tickets (devoluciones) que es la que mas volumen tiene, como 30% del total

pendiente ver que hacemos con los articulos desactualizados, gabi propuso un score de frescura o algo asi

el cliente quiere demo en 3 semanas. presupuesto aprobado para el piloto nomas, si funciona se escala

ojo: el cliente usa zendesk, hay que ver la api
