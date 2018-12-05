from react_select.ReactSelect import ReactSelect
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://react-select.com/home')
react_select = ReactSelect(driver.find_element_by_class_name('basic-single'))
react_select.open_menu()
react_select._close_menu()
react_select.select_by_visible_text('Blue')
react_select.deselect_all()
react_select = ReactSelect(driver.find_element_by_class_name('basic-multi-select'))
react_select.select_by_visible_text("Ocean")
react_select.deselect_by_index(0)
driver.close()
