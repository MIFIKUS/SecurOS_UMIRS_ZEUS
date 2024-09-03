class CommunicationBytes:
    """Байты команд"""
    server_hello =                  0x0  #Приветствие сервера
    client_hello =                  0x1  #Приветствие клиента

    ask_for_alias_condition =       0x20 #Запросить состояние отдельного Алиаса у сервера (не чаще чем раз в 1 секунду)
    alias_condition_answer =        0x30 #Запросить детализацию отдельного Алиаса у сервера (не чаще чем раз в 1 секунду)

    ask_for_alias_detalisation =    0x21 #Ответ состояния отдельного Алиаса на клиент
    alias_detalisation_answer =     0x31 #Ответ детализации отдельного Алиаса на клиент

    ask_for_all_alias_condition =   0x4  #Запросить состояние всех Алиасов у сервера (не чаще чем раз в 10 секунд)
    all_alias_condition_answer =    0x5  #Ответ состояний всех Алиасов на клиент

    switch_off_security_on_alias =  0x6  #Снять с охраны Алиас
    switch_on_security_on_alias =   0x7  #Поставить на охрану Алиас

    turn_off_alias =                0x80 #Отключить Алиас на сервере
    turn_on_alias =                 0x81 #Включить Алиас На сервере

    ask_for_amount_of_aliases =     0x9  #Запросить общее количество Алиасов
    amount_of_aliases_answer =      0xA  #Ответ общего количества Алиасов

    switch_ask_state =              0xB  #Остановить\запустить работу (опрос датчиков) на сервере

    client_activity =               0xF0 #Активность клиента


class AliasConditionsBytes:
    """Байты состояния"""
    turned_off =                    0x10 #Отключен
    security_off =                  0x20 #Снят с охраны
    normal =                        0x30 #Норма
    alarm =                         0x40 #Тревога
    overcoming =                    0x50 #Преодоление
    position =                      0x60 #Положение
    gap =                           0x70 #Разрыв
    closure =                       0x80 #Замыкание
    failure =                       0x90 #Неисправность
    low_power =                     0xA0 #Низкое напряжение
    remote_control =                0xB0 #Удаленный контроль
    opened =                        0xC0 #Вскрытие
    no_signal =                     0xD0 #Нет связи
    miss =                          0xE0 #Отсутствует
    rele_closure =                  0xF0 #Реле замкнуто
    rele_not_closure =              0xF1 #Реле разомкнуто


class HardwareBytes:
    """Байты индентификатора оборудования"""
    murena_murena_k_pautina =       0x00 #Мурена\Мурена-К\Паутина
    dhunt =                         0x30 #ДиХант
    agat =                          0x02 #Агат
    panthera =                      0x06 #Пантера
    PORP_1 =                        0x05 #ПОРП-1
    KEMZU_portal =                  0x50 #КЭМЗУ Портал
    uzel_M =                        0x21 #Узел-M
    PSTM =                          0x20 #ПСТМ
    UST_container =                 0x0F #Контейнер UST


class EntersBytes:
    """Байты входов"""
    enter_1 =                       0x00 #Вход 1
    enter_2 =                       0x01 #Вход 2
    enter_3 =                       0x02 #Вход 3
    enter_4 =                       0x03 #Вход 4
    enter_5 =                       0x04 #Вход 5
    enter_6 =                       0x05 #Вход 6
    enter_7 =                       0x06 #Вход 7


class SensorsTypesBytes:
    """Байты типов датчиков"""
    vibro =                         0x00 #Вибродатчик
    freq_detector =                 0x01 #Частоточный детектор
    seismic =                       0x02 #Сейсмический
    electrocontact =                0x03 #Электроконтактный
    transmitter =                   0x04 #Передатчик
    receiver =                      0x05 #Приемник
    monitor =                       0x06 #Монитор
    rele =                          0x07 #Реле


class SensorEntersBytes:
    """Байты входов для датчиков"""
    sensor_1 =                      0x00 #Датчик 1
    sensor_2 =                      0x01 #Датчик 2
    sensor_3 =                      0x02 #Датчик 3
    sensor_4 =                      0x03 #Датчик 4
    sensor_5 =                      0x04 #Датчик 5
    sensor_6 =                      0x05 #Датчик 6
    sensor_7 =                      0x06 #Датчик 7
    sensor_8 =                      0x07 #Датчик 8
    sensor_9 =                      0x08 #Датчик 9
    sensor_10 =                     0x09 #Датчик 10
    sensor_11 =                     0x0A #Датчик 11
    sensor_12 =                     0x0B #Датчик 12
    sensor_13 =                     0x0C #Датчик 13
    sensor_14 =                     0x0D #Датчик 14
    sensor_15 =                     0x0E #Датчик 15
    sensor_16 =                     0x0F #Датчик 16
    sensor_17 =                     0x10 #Датчик 17
    sensor_18 =                     0x11 #Датчик 18
    sensor_19 =                     0x12 #Датчик 19
    sensor_20 =                     0x13 #Датчик 20




