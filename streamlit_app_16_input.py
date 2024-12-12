import streamlit as st
import pandas as pd
import pickle
import os
from streamlit_chat import message  # Убедитесь, что эта библиотека установлена: pip install streamlit-chat
# import pdb; pdb.set_trace()

# Функции для сохранения и загрузки данных
def save_data():
    with open('data.pkl', 'wb') as f:
        pickle.dump({
            'structure': st.session_state['structure'],
            'previous_data': st.session_state['previous_data'],
            'risk_data': st.session_state['risk_data'],
            'processes': st.session_state['processes']  # Add this line
        }, f)

def load_data():
    if os.path.exists('data.pkl'):
        with open('data.pkl', 'rb') as f:
            data = pickle.load(f)
            st.session_state['structure'] = data.get('structure', {})
            st.session_state['previous_data'] = data.get('previous_data', {})
            st.session_state['risk_data'] = data.get('risk_data', {})
            st.session_state['processes'] = data.get('processes', {})  # Add this line
    # ... (rest of your load_data function)
    else:
        # Инициализация данных, если файла нет
        st.session_state['structure'] = {
            'Департамент IT': {
                'is_archived': False,
                'Управление разработки': {
                    'is_archived': False,
                    'Отдел фронтенда': {
                        'is_archived': False,
                        'Команда A': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Иван Иванов': {'is_archived': False},
                                'Петр Петров': {'is_archived': False},
                            },
                        },
                        'Команда B': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Сергей Смирнов': {'is_archived': False},
                                'Алексей Титов': {'is_archived': False},
                            },
                        }
                    },
                    'Отдел бэкенда': {
                        'is_archived': False,
                        'Команда C': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Алексей Сидоров': {'is_archived': False},
                                'Николай Николаев': {'is_archived': False},
                            },
                        },
                        'Команда D': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Мария Сергеева': {'is_archived': False},
                                'Елена Алексеева': {'is_archived': False},
                            },
                        }
                    }
                },
                'Управление инфраструктуры': {
                    'is_archived': False,
                    'Отдел серверов': {
                        'is_archived': False,
                        'Команда E': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Мария Смирнова': {'is_archived': False},
                                'Владимир Кузнецов': {'is_archived': False},
                            },
                        },
                        'Команда F': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Олег Петров': {'is_archived': False},
                                'Дмитрий Сидоров': {'is_archived': False},
                            },
                        }
                    },
                    'Отдел сети': {
                        'is_archived': False,
                        'Команда G': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Александр Иванов': {'is_archived': False},
                                'Наталья Алексеева': {'is_archived': False},
                            },
                        },
                        'Команда H': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Игорь Романов': {'is_archived': False},
                                'Александр Смирнов': {'is_archived': False},
                            },
                        }
                    }
                }
            },
            'Финансовый департамент': {
                'is_archived': False,
                'Управление бухгалтерии': {
                    'is_archived': False,
                    'Отдел налогов': {
                        'is_archived': False,
                        'Команда I': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Анна Сергеева': {'is_archived': False},
                                'Ольга Петрова': {'is_archived': False},
                            },
                        },
                        'Команда J': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Ирина Иванова': {'is_archived': False},
                                'Евгения Смирнова': {'is_archived': False},
                            },
                        }
                    },
                    'Отдел отчетности': {
                        'is_archived': False,
                        'Команда K': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Сергей Морозов': {'is_archived': False},
                                'Наталья Соколова': {'is_archived': False},
                            },
                        },
                        'Команда L': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Дмитрий Морозов': {'is_archived': False},
                                'Людмила Павлова': {'is_archived': False},
                            },
                        }
                    }
                },
                'Управление финансов': {
                    'is_archived': False,
                    'Отдел платежей': {
                        'is_archived': False,
                        'Команда M': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Андрей Кузнецов': {'is_archived': False},
                                'Елена Сергеева': {'is_archived': False},
                            },
                        },
                        'Команда N': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Николай Петров': {'is_archived': False},
                                'Екатерина Смирнова': {'is_archived': False},
                            },
                        }
                    },
                    'Отдел казначейства': {
                        'is_archived': False,
                        'Команда O': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Иван Сидоров': {'is_archived': False},
                                'Елена Иванова': {'is_archived': False},
                            },
                        },
                        'Команда P': {
                            'is_archived': False,
                            'Сотрудники': {
                                'Марина Кузнецова': {'is_archived': False},
                                'Александр Титов': {'is_archived': False},
                            },
                        }
                    }
                }
            }
        }
        st.session_state['previous_data'] = {}
        st.session_state['risk_data'] = {}

# Загрузка данных при запуске приложения
if 'data_loaded' not in st.session_state:
    load_data()
    
    # Modified data structure for processes (using a dictionary)
    if 'processes' not in st.session_state:
        st.session_state['processes'] = {}  # Initialize an empty dictionary

    # Примерные данные для Иван Иванов
    if 'Иван Иванов' not in st.session_state['previous_data']:
        st.session_state['previous_data']['Иван Иванов'] = [
            {
                '№': 1,
                'ФИО': 'Иван Иванов',
                'Подразделение': 'Отдел фронтенда',
                'Наименование процесса': 'Разработка интерфейса',
                'Описание процесса': 'Создание пользовательского интерфейса для веб-приложения',
                'Значимость процесса': '1',
                'Классификация процесса': 'Supporting process',
                'Категория': '8. Документооборот и управление документацией',
                'Обработка ПДн': 'Да'
            },
            {
                '№': 2,
                'ФИО': 'Иван Иванов',
                'Подразделение': 'Отдел фронтенда',
                'Наименование процесса': 'Оптимизация производительности',
                'Описание процесса': 'Улучшение скорости загрузки страниц',
                'Значимость процесса': '1',
                'Классификация процесса': 'Supporting process',
                'Категория': '8. Документооборот и управление документацией',
                'Обработка ПДн': 'Да'
            }
        ]
        st.session_state['risk_data']['Иван Иванов'] = [
            {
                '№': 1,
                'ФИО': 'Иван Иванов',
                'Подразделение': 'Отдел фронтенда',
                'Процесс': 'Разработка интерфейса',
                'Наименование риска': 'Потеря данных пользователя',
                '1 уровень': 'Технический риск',
                '2 уровень': 'Потеря данных',
                '3 уровень': 'Ошибка системы',
                'Оценка тяжести потенциальных потерь': 'Высокая',
                'Оценка вероятности потенциальных потерь': 'Средняя'
            },
            {
                '№': 2,
                'ФИО': 'Иван Иванов',
                'Подразделение': 'Отдел фронтенда',
                'Процесс': 'Оптимизация производительности',
                'Наименование риска': 'Задержки в загрузке страниц',
                'Оценка вероятности потенциальных потерь': 'Высокая',
                'Оценка тяжести потенциальных потерь': 'Средняя',
                '1 уровень': 'Операционный риск',
                '2 уровень': 'Низкая производительность',
                '3 уровень': 'Плохой UX',
            },
            {
                '№': 3,
                'ФИО': 'Иван Иванов',
                'Подразделение': 'Отдел фронтенда',
                'Процесс': 'Разработка интерфейса',
                'Наименование риска': 'Несоответствие стандартам UI/UX',
                'Оценка вероятности потенциальных потерь': 'Высокая',
                'Оценка тяжести потенциальных потерь': 'Средняя',
                '1 уровень': 'Регуляторный риск',
                '2 уровень': 'Неправильный дизайн',
                '3 уровень': 'Недовольство пользователей',
            }
        ]

    st.session_state['data_loaded'] = True
    save_data()  # Сохраняем изменения

# Остальная часть вашего кода
structure = st.session_state['structure']
previous_data = st.session_state['previous_data']
risk_data = st.session_state['risk_data']

# Функции для работы с данными
def get_process_dataframe(employee_data):
    return pd.DataFrame(employee_data)

def get_risk_dataframe(employee_data):
    return pd.DataFrame(employee_data)

# Функция для получения отображаемого названия с учетом архивации
def get_display_name(name, data):
    return f"{name} (архив)" if data.get('is_archived', False) else name

# Функция для фильтрации элементов по признаку архивации
def filter_items(items, show_archived):
    return {k: v for k, v in items.items() if not v.get('is_archived', False) or show_archived}

# Функция для получения списка ключей с учетом фильтрации и отображаемых названий
def get_filtered_keys(items, show_archived):
    return [get_display_name(k, items[k]) for k in items if not items[k].get('is_archived', False) or show_archived]

# Обновленная функция для фильтрации сотрудников с учетом архивации и корректной обработки данных
def get_filtered_employees(employees, show_archived):
    if isinstance(employees, dict):
        return [
            get_display_name(emp, employees[emp])
            for emp in employees
            if emp != 'is_archived' and (not employees[emp].get('is_archived', False) or show_archived)
        ]
    return []

# Обновленная рекурсивная функция для установки статуса архивации
def set_archive_status(item, status):
    if isinstance(item, dict):
        if 'is_archived' in item and not isinstance(item['is_archived'], dict):
            item['is_archived'] = status
        for key, value in item.items():
            if key != 'Сотрудники' and isinstance(value, dict):
                set_archive_status(value, status)
            elif key == 'Сотрудники' and isinstance(value, dict):
                for emp_key, emp_value in value.items():
                    if isinstance(emp_value, dict):
                        set_archive_status(emp_value, status)

# Выбор отображения архивных записей
show_archived = st.sidebar.checkbox("Показывать архивные записи", value=False)

# Заголовок и сворачиваемая форма в сайдбаре
with st.sidebar.expander("Добавить подразделение", expanded=False):
    # Начало формы внутри сворачиваемого элемента
    with st.form("levels_form"):
        # Поля ввода
        level_1 = st.text_input("Уровень 1 (департамент)")
        level_2 = st.text_input("Уровень 2 (управление)")
        level_3 = st.text_input("Уровень 3 (отдел)")
        level_4 = st.text_input("Уровень 4 (команда)")
        level_5 = st.text_input("Уровень 5 (сотрудник)")

        # Кнопка для отправки формы
        submit_button = st.form_submit_button("Отправить")

# Обработка отправки формы
if submit_button:
    if not level_1:
        st.error("Пожалуйста, заполните хотя бы уровень 1 (департамент).")
    else:
        # Инициализация текущего уровня структуры
        current_structure = st.session_state['structure']

        # Уровень 1: департамент
        if level_1 not in current_structure:
            current_structure[level_1] = {'is_archived': False}
        current_structure = current_structure[level_1]

        # Уровень 2: управление
        if level_2:
            if level_2 not in current_structure:
                current_structure[level_2] = {'is_archived': False}
            current_structure = current_structure[level_2]

        # Уровень 3: отдел
        if level_3:
            if level_3 not in current_structure:
                current_structure[level_3] = {'is_archived': False}
            current_structure = current_structure[level_3]

        # Уровень 4: команда
        if level_4:
            if level_4 not in current_structure:
                current_structure[level_4] = {'is_archived': False}
            current_structure = current_structure[level_4]

        # Уровень 5: сотрудник
        if level_5:
            if 'Сотрудники' not in current_structure:
                current_structure['Сотрудники'] = {}
            if level_5 not in current_structure['Сотрудники']:
                current_structure['Сотрудники'][level_5] = {'is_archived': False}

        st.success("Новое подразделение успешно добавлено!")
        save_data()
        st.rerun()

# Заголовок приложения
st.header('Система учета бизнес-процессов и рисков: ввод данных')

# Выбор подразделения
st.subheader("Выберите подразделение")

departments = filter_items(structure, show_archived)
department_names = get_filtered_keys(departments, show_archived)
selected_department_display = st.selectbox("Уровень 1", [''] + department_names, key='current_department')

if selected_department_display:
    # Получаем реальное название департамента без пометки "(архив)"
    selected_department = selected_department_display.replace(" (архив)", "")
    dept_data = structure[selected_department]

    # Чекбокс для архивирования департамента
    with st.expander("Опции архивирования"):
        archive_dept = st.checkbox(f"Архивировать '{selected_department}'", value=dept_data.get('is_archived', False), key=f'archive_dept_{selected_department}')
        if archive_dept != dept_data.get('is_archived', False):
            set_archive_status(dept_data, archive_dept)
            status = "помещен в архив" if archive_dept else "восстановлен из архива"
            st.success(f"Департамент '{selected_department}' {status}.")
            save_data()
            st.rerun()

    # Выбор управления
    managements = {k: v for k, v in dept_data.items() if k != 'is_archived'}
    managements = filter_items(managements, show_archived)
    management_names = get_filtered_keys(managements, show_archived)
    selected_management_display = st.selectbox("Уровень 2", [''] + management_names, key='current_management')

    if selected_management_display:
        selected_management = selected_management_display.replace(" (архив)", "")
        mgmt_data = dept_data[selected_management]

        # Чекбокс для архивирования управления
        with st.expander("Опции архивирования"):
            archive_mgmt = st.checkbox(f"Архивировать '{selected_management}'", value=mgmt_data.get('is_archived', False), key=f'archive_mgmt_{selected_management}')
            if archive_mgmt != mgmt_data.get('is_archived', False):
                set_archive_status(mgmt_data, archive_mgmt)
                status = "помещено в архив" if archive_mgmt else "восстановлено из архива"
                st.success(f"Управление '{selected_management}' {status}.")
                save_data()
                st.rerun()

        # Выбор отдела
        divisions = {k: v for k, v in mgmt_data.items() if k != 'is_archived'}
        divisions = filter_items(divisions, show_archived)
        division_names = get_filtered_keys(divisions, show_archived)
        selected_division_display = st.selectbox("Уровень 3", [''] + division_names, key='current_division')

        if selected_division_display:
            selected_division = selected_division_display.replace(" (архив)", "")
            div_data = mgmt_data[selected_division]

            # Чекбокс для архивирования отдела
            with st.expander("Опции архивирования"):
                archive_div = st.checkbox(f"Архивировать '{selected_division}'", value=div_data.get('is_archived', False), key=f'archive_div_{selected_division}')
                if archive_div != div_data.get('is_archived', False):
                    set_archive_status(div_data, archive_div)
                    status = "помещен в архив" if archive_div else "восстановлен из архива"
                    st.success(f"Отдел '{selected_division}' {status}.")
                    save_data()
                    st.rerun()

            # Выбор команды
            teams = {k: v for k, v in div_data.items() if k != 'is_archived'}
            teams = filter_items(teams, show_archived)
            team_names = get_filtered_keys(teams, show_archived)
            selected_team_display = st.selectbox("Уровень 4", [''] + team_names, key='current_team')

            if selected_team_display:
                selected_team = selected_team_display.replace(" (архив)", "")
                team_data = div_data[selected_team]

                # Чекбокс для архивирования команды
                with st.expander("Опции архивирования"):
                    archive_team = st.checkbox(f"Архивировать '{selected_team}'", value=team_data.get('is_archived', False), key=f'archive_team_{selected_team}')
                    if archive_team != team_data.get('is_archived', False):
                        set_archive_status(team_data, archive_team)
                        status = "помещена в архив" if archive_team else "восстановлена из архива"
                        st.success(f"Команда '{selected_team}' {status}.")
                        save_data()
                        st.rerun()

                # Выбор сотрудника
                employees = team_data.get('Сотрудники', {})
                employees_filtered = get_filtered_employees(employees, show_archived)
                selected_employee_display = st.selectbox("Уровень 5", [''] + employees_filtered, key='current_employee')

                if selected_employee_display:
                    selected_employee = selected_employee_display.replace(" (архив)", "")
                    employee_data = employees.get(selected_employee, {})

                    # Чекбокс для архивирования сотрудника
                    with st.expander("Опции архивирования"):
                        archive_emp = st.checkbox(f"Архивировать '{selected_employee}'", value=employee_data.get('is_archived', False), key=f'archive_emp_{selected_employee}')
                        if archive_emp != employee_data.get('is_archived', False):
                            employee_data['is_archived'] = archive_emp
                            status = "помещен в архив" if archive_emp else "восстановлен из архива"
                            st.success(f"Сотрудник '{selected_employee}' {status}.")
                            save_data()
                            st.rerun()

                    # Раздел для текущих записей
                    with st.expander("Свернуть / развернуть процессы", expanded=True):
                        st.markdown("""
                            <style>
                            .stButton > button {
                                background-color: green !important;
                                color: white !important;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        if st.button("Добавить процесс"):
                            with st.form("add_process_form"):
                                st.write("Добавить новый бизнес-процесс")

                                process_options = {}  # Initialize the options dictionary
                                for dept, processes in st.session_state.get('processes', {}).items(): # Use .get() to handle missing 'processes'
                                    process_options[dept] = list(processes.keys())  # get process names by department

                                process_number = st.number_input("№", min_value=1, step=1)
                                full_name = st.text_input("ФИО", value=selected_employee)
                                department = st.text_input("Подразделение", value=selected_division)
                                process_description = st.text_area("Описание процесса")
                                preceding_process = st.selectbox("Предшествующий процесс (ы)", [''] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs])  # Correct options formatting
                                process_name = st.text_input("Наименование процесса")
                                following_process = st.selectbox("Последующий процесс (ы) [if no add new]", [''] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs])
                                process_significance = st.text_input("Значимость процесса") # Don't initialize with selected_process here
                                process_classification = st.text_input("Классификация процесса")
                                category_20 = st.text_input("Категория")
                                personal_data_processing = st.selectbox("Обработка ПДн", ['Да', 'Нет'])

                                submitted = st.form_submit_button("Добавить")

                                if submitted:
                                    new_process = {  # Create new_process *before* adding it to session_state
                                        '№': process_number,
                                        'ФИО': full_name,
                                        'Подразделение': department,
                                        'Описание процесса': process_description,
                                        'Предшествующий процесс (ы)': preceding_process,
                                        'Наименование процесса': process_name,
                                        'Последующий процесс (ы) [if no add new]': following_process,
                                        'Значимость процесса': process_significance,
                                        'Классификация процесса': process_classification,
                                        'Категория': category_20,
                                        'Обработка ПДн': personal_data_processing
                                    }
                                    st.session_state['processes'].setdefault(department, {})[process_name] = new_process # Now add it

                                    if full_name in st.session_state['previous_data']:
                                        st.session_state['previous_data'][full_name].append(new_process)
                                    else:
                                        st.session_state['previous_data'][full_name] = [new_process]
                                    st.success("Новый процесс успешно добавлен!")
                                    save_data()
                                    st.rerun()

                        st.markdown("<h4 style='font-weight: normal;'>Ваши бизнес-процессы</h4>", unsafe_allow_html=True)
                        if selected_employee in previous_data:
                            df = get_process_dataframe(previous_data[selected_employee])
                            st.dataframe(df)

                            # Выбор процесса для редактирования
                            selected_process_number = st.selectbox("Выберите процесс для редактирования или удаления", df['№'])
                            st.write(f"Выбран процесс номер: {selected_process_number}")
                            selected_process = next((p for p in previous_data[selected_employee] if p['№'] == selected_process_number), None)

                            if selected_process:
                                with st.form("edit_process_form"):
                                    st.write("Редактировать бизнес-процесс")

                                    process_options = {}  # Recreate process_options every time the form is rendered
                                    for dept, processes in st.session_state.get('processes', {}).items():
                                        process_options[dept] = list(processes.keys())

                                    # Set default values in selectbox for the preceding and following processes
                                    default_preceding = next((f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs if proc == selected_process.get('Предшествующий процесс (ы)', '')), "")
                                    default_following = next((f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs if proc == selected_process.get('Последующий процесс (ы) [if no add new]', '')), "")

                                    process_number = st.number_input("№", value=selected_process['№'], min_value=1, step=1)
                                    full_name = st.text_input("ФИО", value=selected_process['ФИО'])
                                    department = st.text_input("Подразделение", value=selected_process['Подразделение'])
                                    process_description = st.text_area("Описание процесса", value=selected_process['Описание процесса'])
                                    preceding_process = st.selectbox("Предшествующий процесс (ы)", [''] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs], index=([""] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs]).index(default_preceding) if default_preceding in ([""] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs]) else 0)
                                    process_name = st.text_input("Наименование процесса", value=selected_process['Наименование процесса'])
                                    following_process = st.selectbox("Последующий процесс (ы) [if no add new]", [''] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs], index=([""] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs]).index(default_following) if default_following in ([""] + [f"{dept} - {proc}" for dept, procs in process_options.items() for proc in procs]) else 0)
                                    process_significance = st.text_input("Значимость процесса",value=selected_process['Значимость процесса'])
                                    process_classification = st.text_input("Классификация процесса", value=selected_process['Классификация процесса'])
                                    category_20 = st.text_input("Категория", value=selected_process['Категория'])
                                    personal_data_processing = st.selectbox("Обработка ПДн", ['Да', 'Нет'], index=['Да', 'Нет'].index(selected_process['Обработка ПДн']), key='personal_data_processing')



                                    col1, col2 = st.columns(2)
                                    with col1:
                                        submitted = st.form_submit_button("Сохранить изменения")
                                    with col2:
                                        delete_submitted = st.form_submit_button("Удалить процесс", help="Удалить текущий процесс", use_container_width=True)

                                    if submitted:
                                        updated_process = {  # Use updated_process for updated values
                                            '№': int(process_number), # convert to int
                                            'ФИО': full_name,
                                            'Подразделение': department,
                                            'Описание процесса': process_description,
                                            'Предшествующий процесс (ы)': preceding_process,
                                            'Наименование процесса': process_name,
                                            'Последующий процесс (ы) [if no add new]': following_process,
                                            'Значимость процесса': process_significance,
                                            'Классификация процесса': process_classification,
                                            'Категория': category_20,
                                            'Обработка ПДн': personal_data_processing,
                                        }
                                        st.session_state['processes'].setdefault(department, {})[process_name] = updated_process #update process

                                            # Update the process also in previous_data
                                        for i, p in enumerate(st.session_state['previous_data'][selected_employee]):
                                            if p['Наименование процесса'] == selected_process['Наименование процесса']:
                                                st.session_state['previous_data'][selected_employee][i] = updated_process
                                                break


                                        st.write("Изменения сохранены")
                                        save_data()
                                        st.rerun()

                                    if delete_submitted:
                                        st.session_state['previous_data'][selected_employee] = [
                                            p for p in st.session_state['previous_data'][selected_employee] if p['№'] != selected_process_number
                                        ]
                                        st.write(f"Процесс № {selected_process_number} был удален")
                                        save_data()
                                        st.rerun()
                        else:
                            st.write('Нет данных о ранее введенных процессах')

                    with st.expander("Свернуть / развернуть риски", expanded=True):
                        st.markdown("""
                            <style>
                            .stButton > button {
                                background-color: green !important;
                                color: white !important;
                            }
                            </style>
                        """, unsafe_allow_html=True)
                        if st.button("Добавить риск"):
                            with st.form("add_risk_form"):
                                st.write("Добавить новый риск")
                                risk_number = st.number_input("№", min_value=1, step=1)
                                full_name = st.text_input("ФИО", value=selected_employee)
                                department = st.text_input("Подразделение", value=selected_division)
                                process = st.text_input("Процесс")
                                risk_name = st.text_input("Наименование риска")
                                probability_assessment = st.selectbox("Оценка вероятности потенциальных потерь", ['Высокая', 'Средняя', 'Низкая'])
                                severity_assessment = st.selectbox("Оценка тяжести потенциальных потерь", ['Высокая', 'Средняя', 'Низкая'])
                                level_1 = st.text_input("1 уровень")
                                level_2 = st.text_input("2 уровень")
                                level_3 = st.text_input("3 уровень")

                                submitted = st.form_submit_button("Добавить")

                                if submitted:
                                    new_risk = {
                                        '№': risk_number,
                                        'ФИО': full_name,
                                        'Подразделение': department,
                                        'Процесс': process,
                                        'Наименование риска': risk_name,
                                        'Оценка вероятности потенциальных потерь': probability_assessment,
                                        'Оценка тяжести потенциальных потерь': severity_assessment,
                                        '1 уровень': level_1,
                                        '2 уровень': level_2,
                                        '3 уровень': level_3,
                                    }
                                    if full_name in st.session_state['risk_data']:
                                        st.session_state['risk_data'][full_name].append(new_risk)
                                    else:
                                        st.session_state['risk_data'][full_name] = [new_risk]
                                    st.success("Новый риск успешно добавлен!")
                                    save_data()
                                    st.rerun()
                        st.markdown("<h4 style='font-weight: normal;'>Ваши риски</h4>", unsafe_allow_html=True)
                        if selected_employee in risk_data:
                            risk_df = get_risk_dataframe(risk_data[selected_employee])
                            st.dataframe(risk_df)

                            # Выбор риска для редактирования
                            selected_risk_number = st.selectbox("Выберите риск для редактирования или удаления", risk_df['№'])
                            st.write(f"Выбран риск номер: {selected_risk_number}")
                            selected_risk = next((r for r in risk_data[selected_employee] if r['№'] == selected_risk_number), None)

                            if selected_risk:
                                # st.write(f"Редактирование риска: {selected_risk}")
                                # Форма для редактирования риска
                                with st.form("edit_risk_form"):
                                    st.write("Редактировать риск")
                                    risk_number = st.text_input("№", value=str(selected_risk['№']))
                                    full_name = st.text_input("ФИО", value=selected_risk['ФИО'])
                                    department = st.text_input("Подразделение", value=selected_risk['Подразделение'])
                                    process = st.text_input("Процесс", value=selected_risk['Процесс'])
                                    risk_name = st.text_input("Наименование риска", value=selected_risk['Наименование риска'])
                                    level_1 = st.text_input("1 уровень", value=selected_risk['1 уровень'])
                                    level_2 = st.text_input("2 уровень", value=selected_risk['2 уровень'])
                                    level_3 = st.text_input("3 уровень", value=selected_risk['3 уровень'])

                                    probability_assessment = st.selectbox(
                                        "Оценка вероятности потенциальных потерь",
                                        ['Высокая', 'Средняя', 'Низкая'],
                                        index=['Высокая', 'Средняя', 'Низкая'].index(selected_risk['Оценка вероятности потенциальных потерь'])
                                    )
                                    severity_assessment = st.selectbox(
                                        "Оценка тяжести потенциальных потерь",
                                        ['Высокая', 'Средняя', 'Низкая'],
                                        index=['Высокая', 'Средняя', 'Низкая'].index(selected_risk['Оценка тяжести потенциальных потерь'])
                                    )

                                    col1, col2 = st.columns(2)
                                    with col1:
                                        submitted = st.form_submit_button("Сохранить изменения")
                                    with col2:
                                        delete_risk_submitted = st.form_submit_button("Удалить риск")

                                    if submitted:
                                        st.write("Сохранение изменений в риске")
                                        selected_risk['№'] = int(risk_number)
                                        selected_risk['ФИО'] = full_name
                                        selected_risk['Подразделение'] = department
                                        selected_risk['Процесс'] = process
                                        selected_risk['Наименование риска'] = risk_name
                                        selected_risk['Оценка вероятности потенциальных потерь'] = probability_assessment
                                        selected_risk['Оценка тяжести потенциальных потерь'] = severity_assessment
                                        selected_risk['1 уровень'] = level_1
                                        selected_risk['2 уровень'] = level_2
                                        selected_risk['3 уровень'] = level_3
                                        st.write("Изменения сохранены")
                                        save_data()
                                        st.rerun()

                                    if delete_risk_submitted:
                                        st.session_state['risk_data'][selected_employee] = [
                                            r for r in st.session_state['risk_data'][selected_employee] if r['№'] != selected_risk_number
                                        ]
                                        st.write(f"Риск № {selected_risk_number} был удален")
                                        save_data()
                                        st.rerun()
                        else:
                            st.write('Нет данных о ранее введенных рисках')

# Раздел для Чат-бота
st.sidebar.title("Чат-помощник")

# Инициализация сессии для хранения сообщений
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []

def submit():
    """
    Функция, вызываемая при отправке формы.
    Обрабатывает пользовательский ввод и генерирует ответ.
    """
    user_input = st.session_state.input_field
    if user_input:
        # Здесь можно интегрировать модель ИИ для генерации ответа
        response = "Это пример ответа на ваш вопрос."  # Замените на реальный ответ от ИИ
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        # Очистка поля ввода
        st.session_state.input_field = ""

# Форма для ввода сообщения
with st.sidebar.form(key='chat_form'):
    user_input = st.text_input("Введите ваш вопрос:", key="input_field")
    submit_button = st.form_submit_button(label='Отправить', on_click=submit)

# Отображение истории сообщений
if st.session_state["generated"]:
    with st.sidebar:
        for i in range(len(st.session_state["generated"]) - 1, -1, -1):
            message(st.session_state["past"][i], is_user=True, key=f"{i}_user")
            message(st.session_state["generated"][i], key=str(i))