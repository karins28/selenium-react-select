from ReactSelect import ReactSelect
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://jedwatson.github.io/react-select/')
react_select = ReactSelect(driver.find_element_by_class_name('Select'))
react_select.select_by_visible_text('Western Australia')
react_select.deselect_all()
react_select = ReactSelect(driver.find_element_by_class_name('Select--multi'))
react_select.select_by_visible_text("Vanilla")
react_select.deselect_by_index(0)
driver.close()
