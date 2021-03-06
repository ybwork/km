# Celery
'''
	Celery - это инструмент, который позволяет выполнять задачи в фоновом режиме.

	Использовать всё в одном процессе веб-сервера это плохая идея, потому что время отклика приложения будет долгим.

	Для передачи задач между исполнителями лучше использовать не основную базу данных, а такие иструменты, как RabbitMQ или Redis.
'''

# Redis
'''
	Redis - это нереляционная СУБД, с данными типа ключ - значение.

	Хранит базу данных в оперативной памяти, снабжена механизмами снимков и журналирования для обеспечения постоянного хранения на диске.
'''

# Отличия реляционных субд от нереляционных
'''
	Реляционная база данных – это набор данных с определёнными связями между ними.

	Нереляционная база данных - это набор данных в виде ключ-значение. Чаще всего храниться в формате JSON.
'''