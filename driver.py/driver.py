from src.v2 import MagicBricksService

def main_function():
    """Test Driver/Client function"""
    driver_obj = MagicBricksService()
    driver_obj.launch_driver()
    driver_obj.login_complete()
    driver_obj.setup_filters()
    driver_obj.adjust_sqft_slider()
    driver_obj.view_properties()
    driver_obj.scroll_till_end()
    driver_obj.select_all_cards()
    driver_obj.process_all_cards()
    driver_obj.LoggingDriver()
    driver_obj.export_data_to_excel()
    driver_obj.driver_close()


if __name__ == "__main__":
    main_function()