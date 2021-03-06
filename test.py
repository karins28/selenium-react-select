from react_select.ReactSelect import ReactSelect
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://jedwatson.github.io/react-select/')
react_select = ReactSelect(driver.find_element_by_class_name('Select'), 1)
react_select.open_menu()
react_select._close_menu()
react_select.select_by_visible_text('Western Australia')
react_select.deselect_all()
react_select = ReactSelect(driver.find_element_by_class_name('Select--multi'), 1)
react_select.select_by_visible_text("Vanilla")
react_select.deselect_by_index(0)
driver.close()
