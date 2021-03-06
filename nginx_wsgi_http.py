# nginx
'''
	nginx - это веб сервер.

	Для загрузки и просмотра веб-страниц используются специальные программы — браузеры. Браузер это клиент.

	Веб-сервер — это компьютерная программа, запускаемая на подключённом к сети компьютере и использующая протокол HTTP для передачи данных. В простейшем виде такая программа получает по сети HTTP-запрос на определённый ресурс, находит соответствующий файл на локальном жёстком диске и отправляет его по сети запросившему компьютеру. Более сложные веб-серверы способны в ответ на HTTP-запрос динамически генерировать документы с помощью шаблонов и сценариев.
'''

# wsgi
'''
	wsgi - интерфейс между большинством веб-серверов и веб-приложениями написанными на python.
'''

# http
'''
	HTTP (HyperText Transfer Protocol) — протокол передачи гипертекста. В настоящий момент используется и для передачи произвольных данных.

    В HTTP используется технология клиент - сервер.

    Основой HTTP является ресурс, на который указывает URI в запросе клиента. Обычно такими ресурсами являются хранящиеся на сервере файлы.

    Особенностью протокола HTTP является возможность указать в запросе и ответе способ представления ресурса. Для этого используется HTTP-заголовок. Именно благодаря возможности указания способа кодирования сообщения, клиент и сервер могут обмениваться двоичными данными, хотя данный протокол является текстовым.

    HTTP не сохраняет своего состояния. Это означает отсутствие сохранения промежуточного состояния между парами запрос - ответ.

    Каждое HTTP-сообщение состоит из трёх частей, которые передаются в указанном порядке:

        Стартовая строка (Starting line)

            Метод URI HTTP/Версия

        Заголовки (Headers). Это строки. В заголовках указываются параметры передачи и прочие сведения.

            Server: Apache/2.2.11 (Win32) PHP/5.3.0
            Last-Modified: Sat, 16 Jan 2010 21:16:42 GMT
            Content-Type: text/plain; charset=windows-1251
            Content-Language: ru

            Все заголовки разделяются на четыре основных группы:

            	General Headers («Основные заголовки») — могут включаться в любое сообщение клиента и сервера.

            	Request Headers («Заголовки запроса») — используются только в запросах клиента.

            	Response Headers («Заголовки ответа») — только для ответов от сервера.

            	Entity Headers («Заголовки сущности») — сопровождают каждую сущность сообщения.

        Тело сообщения (Message Body). В теле сообщения передают данные. Обязательно должно отделяться от заголовков пустой строкой.

    Тело сообщения может отсутствовать, но стартовая строка и заголовок являются обязательными элементами.

    Основные методы HTTP: GET, POST, PUT, DELETE.

    Помимо этого есть такие методы как: OPTIONS (Используется для определения возможностей веб-сервера или параметров соединения для конкретного ресурса. В ответ серверу следует включить заголовок Allow со списком поддерживаемых методов), HEAD (обычно применяется для извлечения метаданных, то есть данных, относящиеся к дополнительной информации о содержимом или объекте), PATCH (аналогично PUT, но применяется только к фрагменту ресурса), TRACE, CONNECT.

    Первой строкой ответа сервера на запрос клиента является код состояния. За кодом состояния обычно следует отделённая пробелом поясняющая фраза. Например: 200 OK

    Клиент узнаёт по коду ответа о результатах его запроса и определяет, какие действия ему предпринимать дальше.

    Коды состояния:

    	1xx (информационные)

    	2xx (успех)

    	3xx (перенаправление)

    	4xx (ошибка клиента)

    	5xx (ошибка сервера)
'''