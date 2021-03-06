# Обиженные пассажиры

В одной компании, предоставляющей услуги такси, решили раздать бонусы для повышения лояльности N пользователей с самыми большими суммарными опозданиями по вине компании за последний месяц. Для решения этой задачи необходимо проанализировать логи событий, связанных с заказами такси.

Каждое событие в логах описывается одной строкой, содержащей несколько слов, разделенных пробельными символами (слово является непустой последовательностью строчных латинских букв, цифр, нижних подчеркиваний и дефисов). Первое слово в строке всегда определяет тип события.

Всего есть 4 типа событий:

1. ordered —событие заказа такси. Описывается словами
1.1. order_id (идентификатор заказа, строка),
1.2. user_id (идентификатор пользователя, строка),
1.3. ordered_at (время заказа в Unix time*, целое число),
1.4. X (ожидаемое время подачи машины в минутах, целое число),
1.5. Y (ожидаемая длительность поездки в минутах, целое число)
2. arrived — машина подана пользователю. Описывается словами
2.1. order_id (идентификатор заказа, строка),
2.2. arrived_at (время подачи машины, в Unix time, целое число)
3. started — пользователь сел в машине и началась поездка. Описывается словами order_id и started_at аналогично событию arrived.
4. finished — поездка завершилась. Описывается словами order_id и finished_at аналогично событию started.

момент времени в Unix time — это целое число секунд, прошедших с полуночи 1 января 1970 года.

Считается, что пользователь опоздал, если поездка закончилась позже, чем ориентировочное время окончание поездки, рассчитанное исходя из предполагаемого времени подачи машины X, бесплатного времени ожидания K (измеряется в минутах) и предполагаемой длительности поездки Y.

При этом важно учитывать только опоздания, произошедшие по вине компании: если пользователь не садился в машину дольше K минут после подачи, мы считаем его виноватым в своем опоздании, даже если сама поездка тоже оказалась дольше, чем прогнозировалось.

Обратите внимание, что логи пишутся на разных компьютерах и сливаются в единое хранилище несинхронно, поэтому события никак не упорядочены.

## Ограничения

Все числа неотрицательные и не превышают 2147483647. Каждая строка входных данных по длине не превышает 1000 символов.

Суммарное количество строк во наборах входных данных не превышает 10^7.

Гарантируется, что ordered_at <= arrived_at <= started_at <= finished_at.

## Примеры

Для примера 1 требуется вывести не более 10 пользователей с наибольшим суммарным опозданием.

Единственный пользователь alex действительно опоздал (по прогнозу время прибытия было 100+3*60+0*60+25*60=1780), однако он слишком долго садился в машину (ему понадобилось 20 секунд, но бесплатное время ожидания --- 0 минут), поэтому мы не считаем его опоздавшим по вине такси.

В примере 2 bob опоздал (ожидаемое время прибытия было 0+2*60+1*60+10*60=780, а фактическое время прибытия было 823). Пользователь alice же не опоздал: несмотря на то, что машина была подана позже, чем было спрогнозировано при оформлении заказа, время прибытия на точку назначения (1035) все равно оказалось раньше спрогнозированного (0+2*60+1*60+15*60=1080). Таким образом единственным опоздавшим по вине компании пассажиром был bob.

В примере 3 все поездки завершились с опозданием по вине такси. Пользователь biba опоздал дважды на 20 и 110 секунд соответственно, таким образом его суммарное опоздание по вине такси составило 130 секунд. Пользователь kuka совершил всего одну поездку с опозданием 420 секунд. Таким образом, его суммарное опоздание больше, чем у пользователя biba, несмотря на то, что он совершил меньше поездок с опозданием. Поэтому в выходных данных kuka расположен первым, а — вторым.