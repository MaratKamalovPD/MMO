# Репозиторий курса "Методы машинного обучения" в магистратуре ИУ5 МГТУ им. Баумана

## Лабораторная работа №1 - Создание “истории о данных”

Создать "историю о данных" в виде юпитер-ноутбука, с учетом следующих
требований:
1. История должна содержать не менее 5 шагов (где 5 - рекомендуемое
количество шагов). Каждый шаг содержит график и его текстовую
интерпретацию.
2. На каждом шаге наряду с удачным итоговым графиком рекомендуется в
юпитер-ноутбуке оставлять результаты предварительных "неудачных"
графиков.
3. Не рекомендуется повторять виды графиков, желательно создать 5 графиков
различных видов.
4. Выбор графиков должен быть обоснован использованием методологии data-to-viz. 
Рекомендуется учитывать типичные ошибки построения выбранного вида графика 
по методологии data-to-viz. Если методология Вами отвергается, то просьба
обосновать Ваше решение по выбору графика.
5. История должна содержать итоговые выводы. В реальных "историях о
данных" именно эти выводы представляют собой основную ценность для
предприятия.

## Лабораторная работа №2 - Обработка признаков (часть 1)

1. Выбрать набор данных (датасет), содержащий категориальные и числовые признаки и 
пропуски в данных. Для выполнения следующих пунктов можно использовать несколько 
различных наборов данных (один для обработки пропусков, другой для категориальных 
признаков и т.д.) Просьба не использовать датасет, на котором данная задача решалась в 
лекции.
2. Для выбранного датасета (датасетов) на основе материалов лекций решить следующие 
задачи:
• устранение пропусков в данных;
• кодирование категориальных признаков;
• нормализация числовых признаков.

## Лабораторная работа №3 - Обработка признаков (часть 2)

1. Выбрать один или несколько наборов данных (датасетов) для решения следующих задач. 
Каждая задача может быть решена на отдельном датасете, или несколько задач могут быть 
решены на одном датасете. Просьба не использовать датасет, на котором данная задача 
решалась в лекции.
2. Для выбранного датасета (датасетов) на основе материалов лекций решить следующие 
задачи:
i. масштабирование признаков (не менее чем тремя способами);
ii. обработку выбросов для числовых признаков (по одному способу для удаления 
выбросов и для замены выбросов);
iii. обработку по крайней мере одного нестандартного признака (который не является 
числовым или категориальным);
iv. отбор признаков:
* один метод из группы методов фильтрации (filter methods);
* один метод из группы методов обертывания (wrapper methods);
* один метод из группы методов вложений (embedded methods)

## Лабораторная работа №4 - Алгоритм Policy Iteration

На основе рассмотренного на лекции примера реализуйте алгоритм Policy Iteration для 
любой среды обучения с подкреплением (кроме рассмотренной на лекции среды Toy Text / Frozen Lake) из библиотеки Gym (или аналогичной библиотеки)

## Лабораторная работа №5 - Обучение на основе временных различий

На основе рассмотренного на лекции примера реализуйте следующие алгоритмы:
* SARSA
* Q-обучение
* Двойное Q-обучение
для любой среды обучения с подкреплением (кроме рассмотренной на лекции среды Toy Text / Frozen Lake) из библиотеки Gym (или аналогичной библиотеки).

## Лабораторная работа №6 - Обучение на основе DQN

* На основе рассмотренных на лекции примеров реализуйте алгоритм DQN.
* В качестве среды можно использовать классические среды (в этом случае используется 
полносвязная архитектура нейронной сети).
* В качестве среды можно использовать игры Atari (в этом случае используется сверточная архитектура нейронной сети).
* В случае реализации среды на основе сверточной архитектуры нейронной сети +1 балл за экзамен.

## Лабораторная работа №7 - Алгоритмы Actor-Critic

* Реализуйте любой алгоритм семейства Actor-Critic для произвольной среды.


## Рубежный контроль №1 
* Студент — Камалов М.Р.  
* Группа — ИУ5-21М  
* Вариант — 6
* Номер задачи №1 — 6
* Номер задачи №2 — 26

Дополнительные требования для группы ИУ5-21М:
* Для студентов групп ИУ5-21М  для пары произвольных колонок данных построить график  "Диаграмма рассеяния"

Задача №6:
* Для набора данных проведите устранение пропусков для одного произвольного числового признака с использованием метода заполнения средним значением.

Задача №26:
* Для набора данных для одного произвольного числового признака проведите обнаружение и замену найденными верхними и (нижними границами выбросов на основе правила трех сигм) .

## Рубежный контроль №2 

Для одного из алгоритмов временных различий, реализованных Вами в соответствующей лабораторная работе:
* SARSA
* Q-обучение
* Двойное Q-обучение
осуществите подбор гиперпараметров. Критерием оптимизации должна являться суммарная награда
