Каждое пояснение к конкретному примеру начинается заключено в скобки со звездочкой  *(пояснение)

# одной строкой: группировка таблицы spb_general по столбцу 'genre', 
# подсчёт числа значений 'genre' в этой группировке методом count(), 
# сортировка получившегося Series в порядке убывания и сохранение в spb_genres
*(заменить все три комментария на более короткий и понятный - группировка в СПБ по жанру, сортировка по количеству)
spb_genres = spb_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# одной строкой: группировка таблицы moscow_general по столбцу 'genre',
# подсчёт числа значений 'genre' в этой группировке методом count(), 
# сортировка получившегося Series в порядке убывания и сохранение в moscow_genres
*(заменить все три комментария на более короткий и понятный - группировка в МСК по жанру, сортировка по количеству)
moscow_genres = moscow_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# вызов функции для утра понедельника в Москве (вместо df — таблица moscow_general)
# объекты, хранящие время, являются строками и сравниваются как строки
# пример вызова: genre_weekday(moscow_general, 'Monday', '07:00', '11:00')
*(заменить все три комментария на более короткий и понятный - вызов функции для утра понедельника в Москве)
genre_weekday(moscow_general, 'Monday', '07:00', '11:00')


*(В данном примере все комментарии до метода нужно убрать genre_weekday. Их слишком много)
# Объявление функции genre_weekday() с параметрами table, day, time1, time2,
# которая возвращает информацию о самых популярных жанрах в указанный день в
# заданное время:
# 1) в переменную genre_df сохраняются те строки переданного датафрейма table, для
#    которых одновременно:
#    - значение в столбце day равно значению аргумента day
#    - значение в столбце time больше значения аргумента time1
#    - значение в столбце time меньше значения аргумента time2
#    Используйте последовательную фильтрацию с помощью логической индексации.
# 2) сгруппировать датафрейм genre_df по столбцу genre, взять один из его
#    столбцов и посчитать методом count() количество записей для каждого из
#    присутствующих жанров, получившийся Series записать в переменную
#    genre_df_count
# 3) отсортировать genre_df_count по убыванию встречаемости и сохранить
#    в переменную genre_df_sorted
# 4) вернуть Series из 10 первых значений genre_df_sorted, это будут топ-10
#    популярных жанров (в указанный день, в заданное время)
def genre_weekday(df, day, time1, time2):
    # последовательная фильтрация
    # оставляем в genre_df только те строки df, у которых день равен day  *(лишний комментарий - нужно убрать)
    genre_df = df[df['day'] == day]
    # оставляем в genre_df только те строки genre_df, у которых время меньше time2  *(лишний комментарий - нужно убрать)
    genre_df = genre_df[genre_df['time'] < time2] 
    # оставляем в genre_df только те строки genre_df, у которых время больше time1  *(лишний комментарий - нужно убрать)
    genre_df = genre_df[genre_df['time'] > time1] 
    # сгруппируем отфильтрованный датафрейм по столбцу с названиями жанров, возьмём столбец genre и посчитаем кол-во строк для каждого жанра методом count() *(заменить на более короткий комментарий - сортируем по жанру с подсчётом количества)
    genre_df_grouped = genre_df.groupby('genre')['genre'].count()
    # отсортируем результат по убыванию (чтобы в начале Series оказались самые популярные жанры) *(заменить на более короткий - сортируем по убыванию)
    genre_df_sorted = genre_df_grouped.sort_values(ascending=False)
    # вернём Series с 10 самыми популярными жанрами в указанный отрезок времени заданного дня *(лишний комментарий - нужно убрать)
    return genre_df_sorted[:10]

# получение таблицы moscow_general из тех строк таблицы df,  для которых значение в столбце 'city' равно 'Moscow' 
*(лишний комментарий - нужно убрать)
moscow_general = df[df['city'] == 'Moscow']


*(В данном примере все комментарии до метода нужно убратьnumber_tracks. Их слишком много. Заменить на -  Функция для подсчёта прослушиваний для конкретного города и дня)
# <создание функции number_tracks()>
# Объявляется функция с двумя параметрами: day, city.
# В переменной track_list сохраняются те строки таблицы df, для которых 
# значение в столбце 'day' равно параметру day и одновременно значение
# в столбце 'city' равно параметру city (используйте последовательную фильтрацию
# с помощью логической индексации или сложные логические выражения в одну строку, если вы уже знакомы с ними).
# В переменной track_list_count сохраняется число значений столбца 'user_id',
# рассчитанное методом count() для таблицы track_list.
# Функция возвращает число - значение track_list_count.
# С помощью последовательной фильтрации с логической индексацией она 
# сначала получит из исходной таблицы строки с нужным днём,
# затем из результата отфильтрует строки с нужным городом,
# методом count() посчитает количество значений в колонке user_id. 
# Это количество функция вернёт в качестве результата
def number_tracks(day, city):
    day_city_df = df.loc[(df['day'] == day) & (df['city'] == city)]
    count_user_id = day_city_df['user_id'].count()
    return count_user_id


    def replacing_outlier_to_average_value(self, row_mistake, rows_correct):
        for row_cor in rows_correct:
            self.df.loc[self.df[row_mistake] == 1, row_cor] = \
            round(self.df[row_cor].mean())
        return self.df
        # df - датафрейм *(лишний комментарий, нужно убрать. Суть должна быть ясна из правильного имени переменной)
        # row_mistake - поле с данными об ошибке *(лишний комментарий, нужно убрать. Суть должна быть ясна из правильного имени переменной)
        # rows_correct - список полей, где нужно вносить корректировки *(лишний комментарий, нужно убрать. Суть должна быть ясна из правильного имени переменной)
