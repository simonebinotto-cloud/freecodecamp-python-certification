def add_setting(setting_dictionary, setting_tuple):
    
    key, value = setting_tuple
    
    if isinstance(key, str) and isinstance(value, str):
        key = key.lower()
        value = value.lower()
    else:
        return "You must use string type."
    
    if key in setting_dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dictionary, setting_tuple):

    key, value = setting_tuple

    if isinstance(key, str) and isinstance(value, str):
        key = key.lower()
        value = value.lower()
    else:
        return "You must use string type."

    if key in setting_dictionary:
        setting_dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dictionary, key):
    
    if isinstance(key, str):
        key = key.lower()
    else:
        return "You must use string type."

    if key in setting_dictionary:
        del setting_dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(setting_dictionary):

    if len(setting_dictionary) == 0:
        return "No settings available."
    else:
        temp = "Current User Settings:\n"
        for key, value in setting_dictionary.items():
            temp += key.capitalize() + ': ' + value + "\n"
        return temp
        
test_settings = {
    'theme': 'light',
    'notifications': 'enabled',
}

action = add_setting(test_settings, ('THEME', 'dark'))
print(action)

action2 = add_setting(test_settings, ('volume', 'high'))
print(action2)

action3 = update_setting(test_settings, ('theme', 'dark'))
print(action3)

action4 = update_setting(test_settings, ('volume', 'high'))
print(action4)

action5 = delete_setting(test_settings, 'theme')
print(action)